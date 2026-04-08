"""
Convert daily ASCII magnetometer data files into miniSEED using ObsPy.

:copyright:
    2026, Conor A. Bacon
:license:
    CC0 1.0 Universal License
    (https://creativecommons.org/publicdomain/zero/1.0/legalcode)

"""

import argparse
import pathlib
from datetime import datetime as dt, timedelta as td

import obspy
import pandas as pd


HEADERS = [
    "year",
    "month",
    "day",
    "hour",
    "minute",
    "second",
    "BX",
    "BY",
    "BZ",
    "TE",
    "TF",
    "E1",
    "E2",
    "E3",
    "E4",
    "voltage",
    "elevation",
    "latitude",
    "N",
    "longitude",
    "W",
    "12",
    "2",
    "0",
]

CHANNEL_MAPPING = {
    "BZ": "LFZ",
    "BX": "LFN",
    "BY": "LFE",
    "TE": "LKO",
    "TF": "LKD",
    "voltage": "LEV",
}

ARCHIVE_PATH_FMT = "{year}/{network}/{station}/{channel}.D"
FILENAME_FMT = "{network}.{station}.{location}.{channel}.D.{year}.{julday:03d}"

MONTH_LOOKUP = {
    0: 0,
    1: 31,
    2: 62,
    3: 91,
    4: 122,
    5: 152,
    6: 183,
    7: 213,
    8: 244,
    9: 275,
    10: 305,
    11: 336,
}


def check_for_gaps(df: pd.DataFrame) -> bool:
    """
    Detect gaps in 1 Hz data by inspecting the "second" column.

    Parameters
    ----------
    df:
        DataFrame containing recorded data.

    Returns
    -------
     :
        True if any gaps were found, otherwise False.

    """

    seconds = df.second.values
    gap_count = 0
    for i in range(1, len(seconds)):
        if (seconds[i] - seconds[i - 1]) % 60 != 1:
            print(f"   Gap detected around index {i}:")
            print(f"       Previous: {df.iloc[i - 1]}")
            print(f"       Current:  {df.iloc[i]}")
            gap_count += 1

    return gap_count > 0


def write_trace(
    df: pd.DataFrame,
    channel: str,
    archive: pathlib.Path,
    station: str,
    network: str,
    pivot_date: dt | None = None,
) -> None:
    """
    Construct an ObsPy Trace object and write it to disk as miniSEED.

    Parameters
    ----------
    df:
        Data for one day.
    channel:
        Column name in df (e.g. "BX").
    archive:
        Path to root of miniSEED archive.
    station:
        Station code.
    network:
        Network code.
    pivot_date:
        Optional pivot date for if there were issues with timing.

    """

    tr = obspy.Trace()
    tr.data = df[channel].values
    tr.stats.sampling_rate = 1

    tr.stats.network = network
    tr.stats.station = station
    tr.stats.location = ""
    tr.stats.channel = CHANNEL_MAPPING[channel]

    year, month, day = df.year[0], df.month[0], df.day[0]
    if year == 0 and pivot_date is not None:
        pivot_date = dt.strptime(pivot_date, "%Y-%m-%d")
        date = pivot_date + td(days=int(day + MONTH_LOOKUP[month]))
        year, month, day = date.year, date.month, date.day
    hour, minute, second = df.hour[0], df.minute[0], df.second[0]

    starttime = obspy.UTCDateTime(f"{year}-{month}-{day}T{hour}:{minute}:{second}")
    tr.stats.starttime = starttime

    filepath = (
        archive
        / ARCHIVE_PATH_FMT.format(
            year=year,
            network=network,
            station=station,
            channel=tr.stats.channel,
        )
        / FILENAME_FMT.format(
            network=network,
            station=station,
            location="",
            channel=tr.stats.channel,
            year=year,
            julday=starttime.julday,
        )
    )
    filepath.parent.mkdir(exist_ok=True, parents=True)

    tr.write(filepath, format="MSEED")


def process_file(
    file_path: pathlib.Path,
    archive: pathlib.Path,
    station: str,
    network: str,
    pivot_date: str,
) -> None:
    """
    Process one ASCII text file and convert all channels to miniSEED.

    Parameters
    ----------
    file_path:
        Path to raw .txt data file to be converted.
    archive:
        Path to root of miniSEED archive.
    station:
        Station code.
    network:
        Network code.
    pivot_date:
        Optional pivot date for if there were issues with timing.

    """

    print(f"Processing {file_path.name}")
    df = pd.read_csv(file_path, names=HEADERS, sep=r"\s+")

    # Basic validation
    if len(df) != 86400:
        print("   WARNING: file does not contain 86400 samples.")
        if check_for_gaps(df):
            print("     Skipping due to detected gaps.")
            return

    for channel in CHANNEL_MAPPING.keys():
        write_trace(df, channel, archive, station, network, pivot_date)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--station",
        required=True,
        help="Station code.",
    )
    parser.add_argument(
        "-n",
        "--network",
        required=True,
        help="Network code",
    )
    parser.add_argument(
        "-i",
        "--input-dir",
        dest="input_dir",
        required=True,
        type=pathlib.Path,
        help="Directory containing input text files.",
    )
    parser.add_argument(
        "-a",
        "--archive",
        required=True,
        type=pathlib.Path,
        help="Root output directory for SDS-formatted miniSEED.",
    )
    parser.add_argument(
        "--pivot",
        type=str,
        help="An optional pivot date if there were issues with timing.",
    )
    args = parser.parse_args()

    pivot_date = args.pivot if args.pivot is not None else None

    files = sorted(args.input_dir.glob(f"{args.station}/*.txt"))
    for file_path in files:
        process_file(file_path, args.archive, args.station, args.network, pivot_date)


if __name__ == "__main__":
    main()

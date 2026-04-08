"""
Build an overview figure for Lemi magnetometer data stored in an SDS-formatted miniSEED
archive.

The script:
  - Reads BX, BY, BZ, TF, TE, and voltage channels from the archive
  - Down-samples to 60-second intervals
  - Computes rolling averages over a user-defined window
  - Detects data gaps and visualises each continuous segment
  - Produces a 6-panel summary figure

:copyright:
    2026, Conor A. Bacon
:license:
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.html)

"""

import argparse
import pathlib
from datetime import datetime as dt, timedelta as td

import matplotlib.pyplot as plt
import numpy as np
import obspy
import pandas as pd
from pmtk.utils import find_project_root


plt.style.use(find_project_root() / "basic_style.mplstyle")

TEMP_LABELS = {
    "TF": "Fluxgate",
    "TE": "Digitiser",
}

Y_AXLABELS = [
    "B$_{X}$ [nT]",
    "B$_{Y}$ [nT]",
    "B$_{Z}$ [nT]",
    "|B| [nT]",
    "Temperature [°C]",
    "Voltage [V]",
]

COLOUR_LOOKUP = {
    "BX": "k",
    "BY": "k",
    "BZ": "k",
    "ABS_B": "#008080",
    "TE": "#fb9a99",
    "TF": "#cab2d6",
    "voltage": "#007624",
}

TRACE_LOOKUP = {
    "BZ": "LFZ",
    "BX": "LFN",
    "BY": "LFE",
    "TE": "LKO",
    "TF": "LKD",
    "voltage": "LEV",
}


def compute_averages(df: pd.DataFrame, window: str = "h") -> pd.DataFrame:
    """Compute rolling averages of data in specified chunks."""

    for key in ["BX", "BY", "BZ", "TF", "TE", "ABS_B", "voltage"]:
        df[f"average_{key}"] = df.rolling(
            window=window, min_periods=30, center=True, on="times", closed="left"
        )[key].mean()

    return df


def read_data(archive: str, station: str) -> pd.DataFrame:
    """
    Read in station data for all channels and convert to DataFrame for processing.

    Note: Datastreams are automatically decimated to 1/60th of the original sample rate,
          e.g., if originally sampled at 1 Hz, this will become 1 sample / minute.
    Note: Data are assumed to be stored in an SDS-formatted archive.

    Parameters
    ----------
    archive:
        Path to miniSEED archive.
    station:
        Name of the station to be visualised.

    Returns
    -------
    df:
        A DataFrame containing the raw and rolling-averaged data.

    """

    archive = pathlib.Path(archive)

    df = pd.DataFrame()
    for column, channel in TRACE_LOOKUP.items():
        files = sorted(
            [str(file) for file in archive.glob(f"*/*/{station}/{channel}.D/*")]
        )

        times, channel_data = [], []
        for file in files:
            stream = obspy.read(file)
            stream.merge(method=-1)
            if len(stream) > 1:
                print(stream)
            trace = stream[0]
            times.extend([time.datetime for time in trace.times("utcdatetime")[::60]])
            channel_data.extend(list(trace.data[::60]))
        df[column] = channel_data
        if "times" not in df.columns:
            df["times"] = times

    df["ABS_B"] = np.sqrt(df["BY"] ** 2 + df["BX"] ** 2 + df["BZ"] ** 2)
    df = df.reset_index(drop=True)

    return df


def main(args: dict | None = None) -> None:
    df = read_data(args.archive, args.station)
    df = compute_averages(df, args.window)

    # Break dataframe into chunks based on gaps
    deltas = df.times.diff()[1:]
    gaps = deltas[deltas > td(minutes=1)]
    idx = np.cumsum(np.isin(np.arange(len(df.index)), gaps.index))

    fig, axes = plt.subplots(
        nrows=6, ncols=1, figsize=(18.5 / 2.54, 20 / 2.54), constrained_layout=True
    )

    for i, chunk in df.groupby(idx):
        j_ = 0
        for j, key in enumerate(["BX", "BY", "BZ", "ABS_B", "TF", "TE", "voltage"]):
            ax = axes[j_]
            label = TEMP_LABELS.get(key)
            ax.plot(chunk.times, chunk[key].values, c="#838383", alpha=0.7, lw=0.5)
            ax.plot(
                chunk.times,
                chunk[f"average_{key}"].values,
                c=COLOUR_LOOKUP[key],
                label=(label if i == 0 else None),
                lw=0.7,
            )
            if j != 6:
                ax.set_xticks([])

            if key != "TF":
                j_ += 1

    for i, y_axlabel in enumerate(Y_AXLABELS):
        axes[i].set_ylabel(y_axlabel)
    axes[5].set_xlabel("Datetime")

    axes[4].legend(loc=1)

    axes[5].set_ylim([11.0, 15.0])
    axes[5].axhline(11.3, linestyle="--", c="k")
    for ax in axes:
        ax.set_xlim(
            [
                dt.strptime("2023-08-20", "%Y-%m-%d"),
                dt.strptime("2025-08-20", "%Y-%m-%d"),
            ]
        )

    output_path = pathlib.Path.cwd() / "plots"
    output_path.mkdir(exist_ok=True, parents=True)
    fig.savefig(output_path / f"{args.station}-{args.window}-summary.png", dpi=400)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s",
        "--station",
        help="Specify the station to visualise.",
        required=True,
    )
    parser.add_argument(
        "-w",
        "--window",
        help="Specify the window size to use for averaging.",
        default="1D",
    )
    parser.add_argument(
        "-a",
        "--archive",
        help="Specify the location of the data archive to use.",
        required=True,
    )

    args = parser.parse_args()

    main(args)

"""
Compute the data recovery percentage at the daily scale.

:copyright:
    2026, Conor A. Bacon
:license:
    CC0 1.0 Universal License
    (https://creativecommons.org/publicdomain/zero/1.0/legalcode)

"""

from datetime import datetime as dt

from pmtk.utils import find_project_root


STATIONS = {
    "DYFM": ("20230816", "20250822"),
    "KAFM": ("20230817", "20250819"),
    "MOFM": ("20230818", "20250818"),
    "OLFM": ("20230825", "20250801"),
    "RIFM": ("20230816", "20250818"),
    "STFM": ("20230823", "20250820"),
}
BASEPATH = find_project_root() / "data/internal/archive"


def main():
    overall_files = overall_days = 0
    for station, deployment_dates in STATIONS.items():
        files = sorted(
            [file.name for file in BASEPATH.glob(f"202*/6D/{station}/LFZ.D/*.*")]
        )
        total_files = len(set(files))

        start_date = dt.strptime(deployment_dates[0], "%Y%m%d")
        end_date = dt.strptime(deployment_dates[1], "%Y%m%d")
        total_days = (end_date - start_date).days + 1

        overall_files += total_files
        overall_days += total_days

        print(
            f"{station}: {total_files} / {total_days} = "
            f"{(total_files / total_days) * 100:5.2f} %"
        )

    print(
        f"Overall: {overall_files} / {overall_days} = "
        f"{(overall_files / overall_days) * 100:5.2f} %"
    )


if __name__ == "__main__":
    main()

import os
import pandas as pd
from loguru import logger
from rich.progress import track
from husfort.qutility import qtimer
from husfort.qcalendar import CCalendar
from husfort.qlog import define_logger


@qtimer
def load_csv(root_dir: str, bgn_date: str, stp_date: str, calendar: CCalendar) -> pd.DataFrame:
    dfs: list[pd.DataFrame] = []
    for trade_date in track(calendar.get_iter_list(bgn_date, stp_date), description="load data from csv"):
        data_file = f"tushare_futures_md_{trade_date}.csv.gz"
        data_path = os.path.join(root_dir, "by_date", trade_date[0:4], trade_date, data_file)
        df = pd.read_csv(data_path)
        dfs.append(df)
    loaded_data = pd.concat(dfs, axis=0, ignore_index=True)
    return loaded_data


@qtimer
def load_h5(path_lib: str, bgn_date: str, stp_date: str, calendar: CCalendar) -> pd.DataFrame:
    dfs: list[pd.DataFrame] = []
    with pd.HDFStore(path_lib, mode="r") as store:
        for trade_date in track(calendar.get_iter_list(bgn_date, stp_date), description="load data from csv"):
            key = f"Y{trade_date[0:4]}/M{trade_date[4:6]}/D{trade_date[6:8]}/md"
            df: pd.DataFrame = store.select(key=key)  # type:ignore
            dfs.append(df)
    loaded_data = pd.concat(dfs, axis=0, ignore_index=True)
    return loaded_data


def main(root_dir: str, path_lib: str, bgn_date: str, stp_date: str, calendar: CCalendar):
    df_csv = load_csv(root_dir, bgn_date, stp_date, calendar)
    logger.info(f"Shape of csv = {df_csv.shape}")
    df_h5 = load_h5(path_lib, bgn_date, stp_date, calendar)
    logger.info(f"Shape of h5  = {df_h5.shape}")
    return 0


if __name__ == "__main__":
    define_logger()
    app_calendar = CCalendar(r"E:\Deploy\Data\Calendar\cne_calendar.csv")
    main(
        root_dir=r"D:\OneDrive\Data\tushare",
        path_lib=r"D:\OneDrive\Data\tushare\tushare_futures_by_date.h5",
        bgn_date="20120104",
        stp_date="20240805",
        calendar=app_calendar,
    )

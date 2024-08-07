import pandas as pd


def test_fut_daily(pro_api, trade_date: str) -> pd.DataFrame:
    df = pro_api.fut_daily(
        trade_date=trade_date,
        fields="ts_code,trade_date,pre_close,pre_settle,open,high,low,close,settle,vol,amount,oi",
    )
    return df


def test_fut_wsr(pro_api, trade_date: str) -> pd.DataFrame:
    df = pro_api.fut_wsr(trade_date=trade_date, symbol="ZN")
    return df


def test_fut_holding(pro_api, trade_date: str) -> pd.DataFrame:
    # df = pro_api.fut_holding(trade_date=trade_date, symbol="C2409", exchange="DCE")
    # df = pro_api.fut_holding(trade_date=trade_date, symbol="C2409")
    df = pro_api.fut_holding(trade_date=trade_date, exchange="DCE")
    return df

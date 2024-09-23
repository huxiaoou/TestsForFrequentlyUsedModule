import numpy as np
import pandas as pd
import talib as ta

pd.set_option("display.max_rows", None)


def print_functions() -> None:
    print("\nFunctions")
    print(pd.Series(ta.get_functions()))


def print_function_groups() -> None:
    print("\nFunction groups")
    for k, v in ta.get_function_groups().items():
        print(f"--- {k}:")
        print(pd.Series(v))


def test_sma(close: pd.Series | np.ndarray) -> None:
    sma = ta.SMA(close)
    df = pd.DataFrame({
        "close": close,
        "sma": sma,
    })
    print(df)


def test_macd(close: pd.Series | np.ndarray) -> None:
    fast = close.ewm(alpha=2 / (1 + 10)).mean()
    slow = close.ewm(alpha=2 / (1 + 20)).mean()
    diff = fast - slow
    ewdf = diff.ewm(alpha=2 / (1 + 9)).mean()
    hist = diff - ewdf
    macd, macdsignal, macdhist = ta.MACD(close, fastperiod=10, slowperiod=20, signalperiod=9)
    macd_data = pd.DataFrame({
        "close": close,
        "fast": fast,
        "slow": slow,
        "diff": diff,
        "ta.macd": macd,
        "ewdf": ewdf,
        "ta.signal": macdsignal,
        "hist": hist,
        "ta.hist": macdhist,

    })
    print(macd_data.tail(20))


def test_bbands(close: pd.Series | np.ndarray) -> None:
    upper, middle, lower = ta.BBANDS(close, timeperiod=10, nbdevup=2, nbdevdn=2, matype=0)
    bbands = pd.DataFrame({
        "close": close,
        "ta.upper": upper,
        "ta.mid": middle,
        "ta.lower": lower,
    })
    bbands["sma"] = bbands["close"].rolling(window=10).mean()
    bbands["std"] = bbands["close"].rolling(window=10).std(ddof=0)
    bbands["upper"] = bbands["sma"] + 2 * bbands["std"]
    bbands["lower"] = bbands["sma"] - 2 * bbands["std"]
    print(bbands.head(20))


def test_sar(high: pd.Series | np.ndarray, low: pd.Series | np.ndarray) -> None:
    real = ta.SAR(high, low, acceleration=0.02, maximum=0.2)
    macd_data = pd.DataFrame({
        "high": high,
        "low": low,
        "ta.sar": real,

    })
    print(macd_data.tail(20))


def test_adx(high: pd.Series | np.ndarray, low: pd.Series | np.ndarray, close: pd.Series | np.ndarray) -> None:
    adx = ta.ADX(high, low, close, timeperiod=10)
    adxr = ta.ADXR(high, low, close, timeperiod=10)
    data = pd.DataFrame({
        "high": high,
        "low": low,
        "close": close,
        "ta.adx": adx,
        "ta.adxr": adxr,
    })
    print(data.tail(20))


def test_bop(
        opn: pd.Series | np.ndarray,
        high: pd.Series | np.ndarray,
        low: pd.Series | np.ndarray,
        close: pd.Series | np.ndarray
) -> None:
    bop = ta.BOP(opn, high, low, close)
    data = pd.DataFrame({
        "open": opn,
        "close": close,
        "high": high,
        "low": low,
        "ta.bop": bop,
    })
    print(data.tail(20))

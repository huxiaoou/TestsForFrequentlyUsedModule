if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    from module_talib import print_functions, print_function_groups
    from module_talib import test_sma, test_macd, test_bbands,  test_sar, test_adx

    print_functions()
    print_function_groups()

    n = 200
    price = pd.DataFrame(
        data=np.random.randn(n, 4) * 3 + 100,
        columns=["open", "p0", "p1", "close"],
    )
    price["high"] = price[["open", "p0", "p1", "close"]].max(axis=1)
    price["low"] = price[["open", "p0", "p1", "close"]].min(axis=1)
    print(price)
    high, low, close = price["high"], price["low"], price["close"]

    test_sma(close)
    test_macd(close)
    test_bbands(close)
    test_sar(high=high, low=low)
    test_adx(high=high, low=low, close=close)

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    from module_talib import print_functions, print_function_groups
    from module_talib import test_sma, test_bbands, test_macd, test_sar

    print_functions()
    print_function_groups()

    n = 200
    close = pd.Series(np.random.random(size=n) * 2 + 99)
    price = pd.DataFrame({
        "p0": pd.Series(np.random.random(size=n) * 2 + 99),
        "p1": pd.Series(np.random.random(size=n) * 2 + 99),
    })
    price["high"] = price[["p0", "p1"]].max(axis=1)
    price["low"] = price[["p0", "p1"]].min(axis=1)
    print(price)

    test_sma(close)
    test_bbands(close)
    test_macd(close)
    test_sar(high=price["high"], low=price["low"])

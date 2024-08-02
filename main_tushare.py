import tushare as ts
from module_tushare import test_fut_daily, test_fut_wsr, test_fut_holding
import sys

# ts.set_token("write your token here")

pro_api = ts.pro_api()

trade_date = sys.argv[1]
print(trade_date)

df = test_fut_daily(pro_api=pro_api, trade_date=trade_date)
print(df)

df = test_fut_wsr(pro_api=pro_api, trade_date=trade_date)
print(df)

df = test_fut_holding(pro_api=pro_api, trade_date=trade_date)
print(df.head())

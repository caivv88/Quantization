import tushare as ts

ts.set_token('1516cda7ec78094604e39ddb55cd2ff7304ff251df9e5c5c863ecc27')  # set token
pro = ts.pro_api()

# 日线行情
df = pro.daily(ts_code='000001.SZ', start_date='20160701', end_date='20190322')

df1 = ts.get_operation_data(2018, 4)

df2 = ts.get_today_all()

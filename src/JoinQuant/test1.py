"""说明书
https://www.joinquant.com/help/api/help?name=JQData"""
from jqdatasdk import *
from sqlalchemy import *

auth('13530976495', 'hao122')  # 认证

q = query(finance.STK_FIN_FORCAST).filter(finance.STK_FIN_FORCAST.code == '600519.XSHG',
                                          finance.STK_FIN_FORCAST.pub_date >= '2018-01-01').limit(10)
df = finance.run_query(q)

"""动态情景多因子Alpha模型
https://www.joinquant.com/view/community/detail/13717"""

q = query(
    valuation
).filter(
    valuation.code == '000001.XSHE'
)
df = get_fundamentals(q, '2018-10-15')
# 打印出总市值
print(df['market_cap'][0])
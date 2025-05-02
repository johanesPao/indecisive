from classes.env import Env
from classes.data import Data
from tvDatafeed import Interval
from talib.abstract import SMA

env = Env()
data = Data(env.tv_user, env.tv_pass)

df = data.get_data('1000SHIBUSDT.P', 'Binance', Interval.in_daily, 1400)
output = SMA(df, timeperiod=7)

print(output, type(output))
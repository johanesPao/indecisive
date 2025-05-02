from tvDatafeed import TvDatafeed, Interval
import polars as pl


class Data:
    def __init__(self, username: str, password: str):
        self.tv = TvDatafeed(username, password)

    def get_data(
        self,
        symbol: str,
        market: str,
        interval: Interval,
        n_bars: int
    ) -> pl.DataFrame:
        return pl.from_pandas(
            self.tv.get_hist(symbol, market, interval, n_bars)
        )
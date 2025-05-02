from talib.abstract import SMA
import polars as pl


class TechnicalAnalysis:
    def sma(data: pl.Series, period: int | None = None):
        return SMA(data, period)
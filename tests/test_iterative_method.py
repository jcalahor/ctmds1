import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../ctmds1"))
)
from constants import Countries, CountryDefaultPriceBase, GranularityParam, Commodity
from rand_nums import country_date


def test_iterative_method():
    prices = country_date(
        Commodity.power, "2025-01-01", Countries.DE, GranularityParam.h
    )

    assert len(prices.values()) == 24

    prices = country_date(
        Commodity.crude, "2024-11-30", Countries.GB, GranularityParam.hh
    )
    assert len(prices.values()) == 48

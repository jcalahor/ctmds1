from enum import Enum


class Countries(Enum):
    GB = "GB"
    FR = "FR"
    NL = "NL"
    DE = "DE"


class Commodity(str, Enum):
    power = "power"
    natgas = "natgas"
    crude = "crude"


class GranularityParam(str, Enum):
    h = "h"
    hh = "hh"


CountryDefaultPriceBase = {
    "GB": 61,
    "FR": 58,
    "NL": 52,
    "DE": 57,
}

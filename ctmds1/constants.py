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
    Countries.GB: 61,
    Countries.FR: 58,
    Countries.NL: 52,
    Countries.DE: 57,
}

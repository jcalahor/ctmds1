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
    (Countries.GB, Commodity.crude): 91,
    (Countries.GB, Commodity.natgas): 19,
    (Countries.GB, Commodity.power): 70,
    (Countries.FR, Commodity.crude): 90,
    (Countries.FR, Commodity.natgas): 21,
    (Countries.FR, Commodity.power): 55,
    (Countries.NL, Commodity.crude): 89,
    (Countries.NL, Commodity.natgas): 22,
    (Countries.NL, Commodity.power): 76,
    (Countries.DE, Commodity.crude): 79,
    (Countries.DE, Commodity.natgas): 20,
    (Countries.DE, Commodity.power): 67,
}

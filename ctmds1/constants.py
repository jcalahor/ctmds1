from enum import Enum


class Countries(Enum):
    GB = "GB"
    FR = "FR"
    NL = "NL"
    DE = "DE"


class Commodity(Enum):
    power = "power"
    natgas = "natgas"
    crude = "crude"

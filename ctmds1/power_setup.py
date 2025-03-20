from enum import Enum
from .constants import Countries, Commodity
import logging

logger = logging.getLogger()


class PowerSource(str, Enum):
    Wind = "Wind"
    Solar = "Solar"
    Hydro = "Hydro"
    Gas = "Gas"
    Coal = "Coal"
    Nuclear = "Nuclear"


class Demand(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


COUNTRY_POWER_SOURCES = {
    Countries.GB: {
        Demand.Low: {
            PowerSource.Wind: 0.4,
            PowerSource.Gas: 0.4,
            PowerSource.Nuclear: 0.2,
        },
        Demand.Medium: {
            PowerSource.Wind: 0.2,
            PowerSource.Gas: 0.6,
            PowerSource.Nuclear: 0.2,
        },
        Demand.High: {
            PowerSource.Wind: 0.1,
            PowerSource.Gas: 0.7,
            PowerSource.Nuclear: 0.2,
        },
    },
    Countries.FR: {
        Demand.Low: {
            PowerSource.Wind: 0.2,
            PowerSource.Gas: 0.2,
            PowerSource.Nuclear: 0.6,
        },
        Demand.Medium: {
            PowerSource.Wind: 0.1,
            PowerSource.Gas: 0.4,
            PowerSource.Nuclear: 0.5,
        },
        Demand.High: {
            PowerSource.Wind: 0,
            PowerSource.Gas: 0.5,
            PowerSource.Nuclear: 0.5,
        },
    },
    Countries.DE: {
        Demand.Low: {
            PowerSource.Wind: 0.3,
            PowerSource.Gas: 0.3,
            PowerSource.Coal: 0.4,
        },
        Demand.Medium: {
            PowerSource.Wind: 0.2,
            PowerSource.Gas: 0.4,
            PowerSource.Coal: 0.4,
        },
        Demand.High: {
            PowerSource.Wind: 0.0,
            PowerSource.Gas: 0.5,
            PowerSource.Coal: 0.5,
        },
    },
    Countries.NL: {
        Demand.Low: {
            PowerSource.Wind: 0.3,
            PowerSource.Gas: 0.7,
        },
        Demand.Medium: {
            PowerSource.Wind: 0.2,
            PowerSource.Gas: 0.8,
        },
        Demand.High: {
            PowerSource.Wind: 0.1,
            PowerSource.Gas: 0.9,
        },
    },
}

COST_FACTOR = {
    (Demand.Low, PowerSource.Coal): 1.1,
    (Demand.Low, PowerSource.Gas): 1.1,
    (Demand.Low, PowerSource.Hydro): 1.1,
    (Demand.Low, PowerSource.Nuclear): 1.1,
    (Demand.Low, PowerSource.Solar): 1.1,
    (Demand.Low, PowerSource.Wind): 1.1,
    (Demand.Medium, PowerSource.Coal): 1.2,
    (Demand.Medium, PowerSource.Gas): 1.3,
    (Demand.Medium, PowerSource.Hydro): 1.2,
    (Demand.Medium, PowerSource.Nuclear): 1.1,
    (Demand.Medium, PowerSource.Solar): 1.1,
    (Demand.Medium, PowerSource.Wind): 1.1,
    (Demand.High, PowerSource.Coal): 1.4,
    (Demand.High, PowerSource.Gas): 1.5,
    (Demand.High, PowerSource.Hydro): 1.2,
    (Demand.High, PowerSource.Nuclear): 1.2,
    (Demand.High, PowerSource.Solar): 1.1,
    (Demand.High, PowerSource.Wind): 1.1,
}


def factor_cost_by_country(commodity: Commodity, curr_hour: int, country: Countries):
    if commodity != Commodity.power:
        return 1.0
    demand = Demand.Low
    if curr_hour > 6 and curr_hour < 18:
        demand = Demand.Medium
    elif curr_hour >= 18 and curr_hour < 22:
        demand = Demand.High
    elif curr_hour >= 22 and curr_hour < 24:
        demand = Demand.Medium
    power_sources = COUNTRY_POWER_SOURCES[country][demand]
    target_power_source = max(power_sources.keys(), key=power_sources.get)

    final_cost_factor = COST_FACTOR[(demand, target_power_source)]
    entry = f"Calculating cost factor with {commodity} - {curr_hour} - {country} - {target_power_source} - {final_cost_factor}"
    logger.info(entry)
    return final_cost_factor

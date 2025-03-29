from enum import Enum
from ctmds1.constants import Countries, Commodity
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
        PowerSource.Wind: {"capacity": 150, "cost": 10},
        PowerSource.Gas: {"capacity": 600, "cost": 50},
        PowerSource.Nuclear: {"capacity": 300, "cost": 20},
    },
    Countries.FR: {
        PowerSource.Wind: {"capacity": 100, "cost": 12},
        PowerSource.Gas: {"capacity": 400, "cost": 45},
        PowerSource.Nuclear: {"capacity": 500, "cost": 15},
    },
    Countries.DE: {
        PowerSource.Wind: {"capacity": 120, "cost": 8},
        PowerSource.Gas: {"capacity": 400, "cost": 48},
        PowerSource.Coal: {"capacity": 500, "cost": 70},
    },
    Countries.NL: {
        PowerSource.Wind: {"capacity": 100, "cost": 9},
        PowerSource.Gas: {"capacity": 500, "cost": 55},
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


def allocate_power(power_sources, demand_mwh):
    sorted_sources = sorted(power_sources.items(), key=lambda x: x[1]["cost"])

    remaining_demand = demand_mwh
    total_cost = 0
    allocation = []
    max_cost = 0

    for source, data in sorted_sources:
        if remaining_demand <= 0:
            break
        supply = min(data["capacity"], remaining_demand)
        if max_cost < data["cost"]:
            max_cost = data["cost"]
        allocation.append(
            {"source": source.value, "supply": supply, "cost": data["cost"]}
        )
        remaining_demand -= supply

    if remaining_demand > 0:
        logger.info(
            f"⚠️ Warning: Demand of {demand_mwh} MWh not fully met! {remaining_demand} MWh short."
        )
    else:
        logger.info(f"Demand of {demand_mwh} MWh fully met!")

    logger.info(f"Allocation was {allocation} - max cost {max_cost}")

    for alloc in allocation:
        total_cost += alloc["supply"] * max_cost
    return total_cost


def factor_cost_by_country(commodity: Commodity, curr_hour: int, country: Countries):
    if commodity != Commodity.power:
        return 1.0
    demand = 400
    if curr_hour > 6 and curr_hour < 18:
        demand = 500
    elif curr_hour >= 18 and curr_hour < 22:
        demand = 600
    elif curr_hour >= 22 and curr_hour < 24:
        demand = 400
    power_sources = COUNTRY_POWER_SOURCES[country]

    total_cost = allocate_power(power_sources, demand)
    entry = f"Calculating cost factor with {commodity} - {curr_hour} - {country} - {total_cost}"
    logger.info(entry)
    return total_cost / 10000

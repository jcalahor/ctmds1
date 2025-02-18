from constants import Countries
from constants import Commodity


SEASON_CURVE_BY_COUNTRY_COMMODITY = {
    (Countries.GB, Commodity.crude): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.3, "Q4": 1.1},
    (Countries.GB, Commodity.natgas): {"Q1": 1.3, "Q2": 1.1, "Q3": 0.9, "Q4": 1.2},
    (Countries.GB, Commodity.power): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.2, "Q4": 1.0},
    (Countries.FR, Commodity.crude): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.3, "Q4": 1.1},
    (Countries.FR, Commodity.natgas): {"Q1": 1.3, "Q2": 1.1, "Q3": 0.9, "Q4": 1.1},
    (Countries.FR, Commodity.power): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.2, "Q4": 1.0},
    (Countries.DE, Commodity.crude): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.1, "Q4": 1.1},
    (Countries.DE, Commodity.natgas): {"Q1": 1.4, "Q2": 1.1, "Q3": 1.0, "Q4": 1.1},
    (Countries.DE, Commodity.power): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.3, "Q4": 1.0},
    (Countries.NL, Commodity.crude): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.2, "Q4": 1.1},
    (Countries.NL, Commodity.natgas): {"Q1": 1.3, "Q2": 1.1, "Q3": 0.9, "Q4": 1.2},
    (Countries.NL, Commodity.power): {"Q1": 0.9, "Q2": 1.1, "Q3": 1.3, "Q4": 1.0},
}


HOURLY_CURVE_BY_COUNTRY_COMMODITY = {
    (Countries.GB, Commodity.crude): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.GB, Commodity.natgas): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.GB, Commodity.power): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.FR, Commodity.crude): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.FR, Commodity.natgas): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.FR, Commodity.power): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.DE, Commodity.crude): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.DE, Commodity.natgas): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.DE, Commodity.power): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.NL, Commodity.crude): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.NL, Commodity.natgas): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
    (Countries.NL, Commodity.power): {
        0: 0.9,
        1: 1.1,
        2: 1.1,
        3: 1.1,
        4: 1.1,
        5: 1.1,
        6: 1.2,
        12: 0.9,
        13: 1.1,
        14: 1.1,
        15: 1.1,
        16: 1.1,
        17: 1.1,
        18: 1.2,
        19: 1.1,
        20: 1.1,
        21: 1.1,
        22: 1.2,
        23: 1.1,
        24: 1.1,
    },
}

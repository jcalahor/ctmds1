from typing import List, Dict, Optional
import duckdb
import logging
from ctmds1.constants import Countries, Commodity

logger = logging.getLogger(__name__)


async def init_db():
    conn = duckdb.connect(database=":memory:")
    conn.execute(
        """
        CREATE TABLE hourly_curve AS 
        SELECT * FROM read_csv_auto('./ctmds1/data/hourly_curve_by_country_commodity.csv', HEADER=True)
    """
    )
    conn.execute(
        """
        CREATE TABLE season_curve AS 
        SELECT * FROM read_csv_auto('./ctmds1/data/curve_by_season.csv', HEADER=True)
    """
    )
    conn.execute(
        """
        CREATE TABLE currency_rates AS 
        SELECT * FROM read_csv_auto('./ctmds1/data/currency_rates.csv', HEADER=True)
    """
    )
    conn.execute(
        """
    CREATE TABLE prices (
        country TEXT,
        commodity TEXT,
        price_date TEXT,
        hour INT,
        minute INT,
        price FLOAT
    )
    """
    )
    return conn


def get_hourly_curve_factor(
    db, country: Countries, commodity: Commodity
) -> Optional[Dict[int, float]]:
    try:
        results = db.execute(
            """
            SELECT hour, factor
            FROM hourly_curve
            WHERE country = ? AND commodity = ?
            """,
            (country.value, commodity.value),
        ).fetchall()

        if not results:
            return None
        return {hour: factor for hour, factor in results}
    except duckdb.Error as e:
        logger.error(f"Error querying hourly curve factor: {e}")
        return None


def get_season_curve_factor(
    db, country: Countries, commodity: Commodity
) -> Optional[Dict[str, float]]:
    country_str = country.value
    commodity_str = commodity.value

    try:
        results = db.execute(
            """
            SELECT season, factor
            FROM season_curve
            WHERE country = ? AND commodity = ?
            """,
            (country_str, commodity_str),
        ).fetchall()
        logger.info(results)

        if not results:
            return None
        return {season: factor for season, factor in results}
    except duckdb.Error as e:
        logger.error(f"Error querying season curve factor: {e}")
        return None


def get_currency_factor(db, country: Countries) -> Optional[float]:
    country_str = country.value
    try:
        result = db.execute(
            """
            SELECT conversion_rate
            FROM currency_rates
            WHERE country = ?
            """,
            (country_str,),
        ).fetchone()
        print(result[0])
        if not result:
            return None
        return result[0]
    except duckdb.Error as e:
        logger.error(f"Error querying currency factor: {e}")
        return None


def store_price(
    db,
    country: Countries,
    commodity: Commodity,
    price_date: str,
    hour: int,
    minute: int,
    price: float,
) -> bool:
    try:
        db.execute(
            """
            INSERT INTO prices (country, commodity, price_date, hour, minute, price)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (country.value, commodity.value, price_date, hour, minute, round(price, 2)),
        )
        return True
    except duckdb.Error as e:
        logger.error(f"Error storing price: {e}")
        return False


def get_prices(
    db, country: Countries, commodity: Commodity, price_date: str
) -> Optional[List[Dict[str, float]]]:
    try:
        results = db.execute(
            """
            SELECT hour, minute, price
            FROM prices
            WHERE country = ? AND commodity = ? AND price_date = ?
            ORDER BY hour, minute
            """,
            (country.value, commodity.value, price_date),
        ).fetchall()

        if not results:
            return None

        return [
            {"hour": hour, "minute": minute, "price": round(price, 2)}
            for hour, minute, price in results
        ]
    except duckdb.Error as e:
        logger.error(f"Error querying prices: {e}")
        return None

from typing import Optional, Dict
import duckdb
from .constants import Countries, Commodity


async def init_db():
    conn = duckdb.connect(database=":memory:")
    conn.execute(
        """
        CREATE TABLE hourly_curve AS 
        SELECT * FROM read_csv_auto('./ctmds1/data/hourly_curve_by_country_commodity.csv', HEADER=True)
    """
    )
    print(conn.execute("SELECT * FROM hourly_curve LIMIT 5").fetchall())
    return conn



def get_hourly_curve_factor(
    db, country: Countries, commodity: Commodity
) -> Optional[Dict[int, float]]: 
    country_str = country.value
    commodity_str = commodity.value

    if country_str not in Countries.__members__ or commodity_str not in Commodity.__members__:
        raise ValueError("Invalid country or commodity")
    try:
        results = db.execute(
            """
            SELECT hour, factor
            FROM hourly_curve
            WHERE country = ? AND commodity = ?
            """,
            (country_str, commodity_str),
        ).fetchall()

        if not results:
            return None
        return {hour: factor for hour, factor in results}
    except duckdb.Error as e:
        print(f"Error querying hourly curve factor: {e}")
        return None

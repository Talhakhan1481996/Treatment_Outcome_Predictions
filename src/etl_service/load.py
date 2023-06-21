import json

from base_logger import logger
from redis_connector import redis_client
from transform import data_transformations


def load_data_to_redis(specializations_dfs: dict) -> dict:
    """
    Function: load_data_to_redis

    Description:
    This function loads data from a dictionary of specializations dataframes into Redis.

    Parameters:

    specializations_dfs (dict): A dictionary containing specializations (key) dataframes (value).
    Returns:

    dict: The same input dictionary of specializations dataframes.

    Note:
    The function requires a Redis client to be initialized before calling it.
    The logger object is expected to be available to log the information regarding the successful storage of data in Redis.
    """
    for key, val in specializations_dfs.items():
        redis_client.set(key, json.dumps(val, indent=2))
    logger.info("Data Stored in Redis.")
    return specializations_dfs


if __name__ == "__main__":
    load_data_to_redis(data_transformations())

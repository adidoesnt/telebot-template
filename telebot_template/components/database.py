from peewee import *

from telebot_template.constants import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
from telebot_template.constants import DB_PATH

# db = SqliteDatabase(
#     DB_PATH, {
#         "pragmas": {
#             "journal_mode": "wal",
#             "cache_size": -1024 * 64,
#         }
#     }
# )

# db = MySQLDatabase(
#     DB_NAME,
#     host=DB_HOST,
#     port=DB_PORT,
#     user=DB_USER,
#     password=DB_PASSWORD,
# )

db = PostgresqlDatabase(
    DB_NAME,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
)
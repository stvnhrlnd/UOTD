"""Settings for the UOTD application retrieved from environment variables."""

from os import environ

REPOSITORY_SETTINGS = {
    "STORAGE_NAME": environ.get("STORAGE_NAME"),
    "STORAGE_KEY": environ.get("STORAGE_KEY"),
    "STORAGE_TABLE_UOTD": environ.get("STORAGE_TABLE_UOTD")
}

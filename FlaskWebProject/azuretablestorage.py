"""Azure Table storage support for the UUID of the Day website."""

from azure.common import AzureMissingResourceHttpError
from azure.storage.table import TableService
from datetime import date
from uuid import uuid4


class Repository(object):
    """Azure Table storage repository for UOTD."""

    def __init__(self, settings):
        """Initialise UOTD repository with the given settings dict.

        Required settings:
        STORAGE_NAME -- the Azure Storage account name
        STORAGE_KEY -- an access key for the Storage account
        STORAGE_TABLE_UOTD -- the name of the table
        """
        self.service = TableService(settings["STORAGE_NAME"],
                                    settings["STORAGE_KEY"])
        self.uotd_table = settings["STORAGE_TABLE_UOTD"]
        self.service.create_table(self.uotd_table)
        self.partition_key_format = "%Y%m"
        self.row_key_format = "%d"

    def get_uotd(self):
        """Get the UUID for the current day.

        If the UUID does not yet exist then it will be created.
        """
        partition_key = date.today().strftime(self.partition_key_format)
        row_key = date.today().strftime(self.row_key_format)

        try:
            uotd_entity = self.service.get_entity(self.uotd_table,
                                                  partition_key,
                                                  row_key)
            uuid = uotd_entity.uuid
        except AzureMissingResourceHttpError:
            uuid = str(uuid4())
            uotd_entity = {
                "PartitionKey": partition_key,
                "RowKey": row_key,
                "uuid": uuid
            }
            self.service.insert_entity(self.uotd_table, uotd_entity)

        return uuid

    def get_uuids(self, partition_key):
        """Get all the UUIDs in a given partition."""
        filter = "PartitionKey eq '{0}'".format(partition_key)
        entities = self.service.query_entities(self.uotd_table, filter=filter)
        return entities

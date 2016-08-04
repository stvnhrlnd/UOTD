from azure.common import AzureMissingResourceHttpError
from azure.storage.table import TableService
from datetime import date
from uuid import uuid1


class Repository(object):
    def __init__(self, settings):
        self.service = TableService(settings["STORAGE_NAME"],
                                    settings["STORAGE_KEY"])
        self.uotd_table = settings["STORAGE_TABLE_UOTD"]
        self.service.create_table(self.uotd_table)
        self.uotd_partition = "uotd"

    def get_uotd(self, date_obj=None):
        if date_obj is None:
            row_key = date.today().strftime("%Y%m%d")

            try:
                uotd_entity = self.service.get_entity(self.uotd_table,
                                                      self.uotd_partition,
                                                      row_key)
                uuid = uotd_entity.uuid
            except AzureMissingResourceHttpError:
                uuid = str(uuid1())
                uotd_entity = {
                    "PartitionKey": self.uotd_partition,
                    "RowKey": row_key,
                    "uuid": uuid
                }
                self.service.insert_entity(self.uotd_table, uotd_entity)
        else:
            row_key = date_obj.strftime("%Y%m%d")

            try:
                uotd_entity = self.service.get_entity(self.uotd_table,
                                                      self.uotd_partition,
                                                      row_key)
                uuid = uotd_entity.uuid
            except AzureMissingResourceHttpError:
                uuid = None

        return uuid

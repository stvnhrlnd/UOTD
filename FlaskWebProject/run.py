import os
import sys

sys.path.append(os.path.join(os.getcwd(), "site-packages"))

import azuretablestorage
import settings

if __name__ == "__main__":
    repository = azuretablestorage.Repository(settings.REPOSITORY_SETTINGS)
    repository.get_uotd()

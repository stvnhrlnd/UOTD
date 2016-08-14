"""Azure WebJob for generating the UUID of the Day."""

import os
import sys

# Ensure third-pary packages can be imported:
# http://nicholasjackson.github.io/azure/python/python-packages-and-azure-webjobs/
sys.path.append(os.path.join(os.getcwd(), "site-packages"))

import azuretablestorage
import settings

if __name__ == "__main__":
    repository = azuretablestorage.Repository(settings.REPOSITORY_SETTINGS)
    repository.get_uotd()

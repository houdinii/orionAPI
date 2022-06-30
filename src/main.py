#! python3 -v
import os

from utilities.utilities import Utilities

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    util = Utilities()
    settings = util.get_settings('../config/settings.json')
    print(settings)

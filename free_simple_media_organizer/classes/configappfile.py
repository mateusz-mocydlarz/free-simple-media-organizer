# -*- coding: utf-8 -*-
import json
import platformdirs
from os.path import join, exists


class ConfigAppFile (object):
    """The configuration for the app in json"""

    config_file_path = join(platformdirs.user_config_path("FreeSimpleMediaOrganizer"), "configuration.json")

    def __init__(self) -> None:

        if exists(self.config_file_path):
            self.config_app = json.load(self.config_file_path)
        else:
            self.create_config_file()

    def create_config_file(self):
        config = dict()
        config["app_vesriob"] = "01.000.000.00"

        self.config_app = json.loads(config)

        # json.dump(config, self.config_file_path)
        self.__init__()

        # print(self.config_file_path)
        # config_app = json.load(self.config_file_path)


if __name__ == "__main__":
    test = ConfigAppFile()

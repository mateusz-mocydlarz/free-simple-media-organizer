# -*- coding: utf-8 -*-
import json
import platformdirs
from os.path import join, exists, dirname
from os import makedirs


class ConfigAppFile (object):
    """The configuration for the app in json"""

    app_config_file_path = join(platformdirs.user_config_path("FreeSimpleMediaOrganizer"), "configuration.json")

    def __init__(self):

        self.app_config = dict()
        self.app_config["test"] = "testowa wartość"

        if exists(self.app_config_file_path):
            with open(self.app_config_file_path, "r", encoding="utf8") as config_file:
                self.app_config.update(json.load(config_file))
        else:
            makedirs(dirname(self.app_config_file_path), exist_ok=True)
            with open(self.app_config_file_path, "w", encoding="utf8") as config_file:
                json.dump(self.app_config, config_file, indent=4, ensure_ascii=False)

    def load(self) -> dict:
        """Return configuration as dict

        Returns:
            dict: configuration
        """
        return self.app_config

    def save(self, config_data: dict) -> None:
        """Save configuration to file data

        Args:
            config_data (dict): configuration
        """
        with open(self.app_config_file_path, "w") as config_file:
            json.dump(config_data, config_file, indent=4)


if __name__ == "__main__":
    test = ConfigAppFile()
    print(test.load())

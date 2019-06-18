"""
A parser for .yml and .ymal files.
"""
import os
import yaml

class YamlReader:
    """
    A .yml/.ymal reader
    """

    def valid_path_file(self):
        """
        checking for valid file path and valid extension
        """
        validated = True

        while validated:

            file_path = input('Please type a valid file path for your .yml or .yaml file:\n')
            valid_path = os.path.isfile(file_path)
            valid_extension = YamlReader.valid_yml_file(self, file_path)

            if not valid_path:
                print(file_path + " is not a valid directory.")
            elif not valid_extension:
                print(file_path + " is not a .yml or .yaml file.")
            else:
                validated = False
            data = YamlReader.yaml_loader(self, file_path)
        return data

    def valid_yml_file(self, file_path):
        """
        validating .yml or .ymal extension
        """
        file_extension = os.path.splitext(file_path)
        valid_extension = file_extension[1] == '.yml' or file_extension[1] == '.yaml'
        return valid_extension

    def yaml_loader(self, file_path):
        """
        reading the content of the .yml or .ymal file
        """
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
        
import json


class Utilities:
    def get_settings(self, file_path):
        settings = self.read_json(file_path)
        if settings is None:
            print("No settings file found.")
            return None
        return settings

    def read_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not found: {}".format(file_path))
            return None
        except json.JSONDecodeError:
            print("Invalid JSON: {}".format(file_path))
            return None
        except Exception as e:
            print("{}".format(e))
            return None
#   Create version of parse_json_to_dict.py but for parsing/converting YAML to a dictionary
import yaml
import sys
import os

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        try:
            with open(sys.argv[1], "r") as file:
                yaml.safe_load(file)
            print("YAML file is valid!")
        except yaml.YAMLError as e:
            print("YAML syntax error:")
            print(e)
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + sys.argv[1] + "' not found")

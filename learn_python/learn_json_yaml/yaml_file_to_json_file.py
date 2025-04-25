# 3.	Create a YAML to JSON file conversion script
import os
import sys
import yaml
import json

if len(sys.argv) > 2:
    yaml_filename = sys.argv[1]
    json_filename = sys.argv[2]
    # check yaml file exists
    if os.path.exists(yaml_filename):
        # check json file does not exist
        if not os.path.exists(json_filename):
            # open file for reading
            with open(yaml_filename, "r") as file:
                yaml_content = yaml.safe_load(file)
            with open(json_filename, 'w') as json_file:
                json.dump(yaml_content, json_file, indent=2)
        else:
            # alert user that savefile already exists
            print("ERROR: File '" + json_filename + "' already exists")
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + yaml_filename + "' not found")
else:
    print("ERROR: missing at least one argument (YAML_filename), (JSON_filename)")
    print(f"Usage: {sys.argv[0]} <YAML_filename> <JSON_filename>")
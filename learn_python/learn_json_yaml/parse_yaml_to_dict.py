#   Create version of parse_json_to_dict.py but for parsing/converting YAML to a dictionary
import os
import sys
import yaml

if len(sys.argv) > 1:
    # check file exists
    if os.path.exists(sys.argv[1]):
        # open file for reading
        with open(sys.argv[1], "r") as file:
            yaml_content = yaml.safe_load(file)
            print(type(yaml_content))
            print(yaml_content)
        print("YAML file is valid!")
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + sys.argv[1] + "' not found")
else:
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")
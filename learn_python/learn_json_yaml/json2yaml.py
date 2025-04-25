import json
import os
import sys
import yaml

# 1. Convert the JSON to YAML - use yaml library
def json_to_yaml(json_string):
    yaml_content = yaml.dump(json_string, sort_keys=False)
    return yaml_content

# 2. Save the YAML into a new file with the name for it received as a argument
# 2.2 Check the target file doesn't already exist
# 2.3 If previous conditions not met, then save YAML file
def save_yaml_file(yaml_content, filename):
    if os.path.exists(filename):
        print("File already exists")
    else:
        with open(filename, "w") as file:
            file.write(yaml_content)
            return print("file saved as " + filename)

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()

        # Convert to yaml
        yaml_output = json_to_yaml(source_content)
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
        if len(sys.argv) > 2:
            save_yaml_filename = sys.argv[2]
            save_yaml_file(yaml_output, save_yaml_filename)
        else:
            print(yaml_output)

    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")
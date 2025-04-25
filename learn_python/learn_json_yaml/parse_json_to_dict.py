#Convert JSON file and JSON string from JSON file to Python dict

# 1. Convert JSON file to a Python dictionary

# a.	Use 'with' to open server.json
# b.	Parse contents the JSON file into a Python dictionary named "servers"
# c.	Print out the type of "servers"
# d.	Print out the dictionary record with the key "server1"
# e.	Print out the dictionary record with the key "server2"
# f.    Print all of the keys and values
import json
import sys
import os

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            servers = json.load(file)
            print(type(servers))
            print(servers["server1"])
            print(servers["server2"])
            print(servers)

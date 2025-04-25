import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/w51nx")

# Automatically pretty-print headers (as dict)
print("\nHeaders:")
print(json.dumps(dict(post_codes_req.headers), indent=4))  # <-- converts headers to dict and formats it

# Automatically pretty-print content if it's JSON
print("\nContent:")
try:
    print(json.dumps(post_codes_req.json(), indent=4))  # <-- directly pretty-prints the parsed JSON
except ValueError:
    print("Response content is not valid JSON.")

import requests
from datetime import datetime as dt
import json

# File name prefix
file_name_prefix = "liseberg"
# Time when script is executed
fetch_time = dt.now().strftime("%Y%m%dT%H%M%S")

# Settings for the URLs
base_url = "https://www.liseberg.se/sv/api/queue/"
ids = ["87", "64", "3", "89", "88",
       "79", "71", "44", "16", "39",
       "6", "63", "78", "61", "80",
       "72", "73", "74", "28", "32",
       "75", "36", "45", "18", "55",
       "57", "69", "92", "83", "33",
       "15", "42", "31", "47", "76",
       "77", "56", "96", "24"]
# for testing purposes
test_ids = ["87", "64"]

# placeholder variables
results = []

# Fetch data from Liseberg API
for id in ids:
    this_url = base_url + id
    request = requests.get(this_url)
    request_dict = json.loads(request.text)
    request_dict['time_stamp'] = dt.now().isoformat(timespec='seconds')
    results.append(request_dict)

# Write to file
filename = file_name_prefix+"_"+fetch_time+".txt"
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

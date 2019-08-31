import json
import pandas as pd
from os import listdir
import fnmatch
import re

# Data paths
raw_data_folder = "./data/"
processed_data_path = "./dataframes/data.csv"

# Prepare variables
data = []
index = []

# Translates the Liseberg status string to a numerical value
status_to_value_dict = {'0-10': 10,
                        '10-20': 20,
                        '20-30': 30,
                        '30-40': 40,
                        '40-50': 50,
                        '50-60': 60}

# Traverse all data files
listOfFiles = listdir(raw_data_folder)

# Iterate over all files in data folder matching this pattern
pattern = "liseberg_*.txt"
for file in listOfFiles:
    # New data dict for file
    data_dict = {}
    if fnmatch.fnmatch(file, pattern):
        filename = raw_data_folder + file
        # Read data from file to a format working with pd.DataFrame
        with open(filename, 'r') as f:
            json_data = json.load(f)
            # Fill index for this file
            index.append(json_data[0].get('time_stamp'))
            for entry in json_data:
                # Value = None is the standard value
                value = None
                # Extract queue value from status string
                queue_time = re.search(':\s(.+?)\smin', entry['status'])

                if queue_time:
                    match = queue_time.group(1)
                    # Get the value corresponding to the string
                    # See dict above
                    print(status_to_value_dict.get(match))
                    value = status_to_value_dict.get(match)
                data_dict[str(entry['name'])] = value
            data.append(data_dict)

# Create dataframe using the dates as index
df = pd.DataFrame(data, index=index)
# Replace "None" with "NaN"
df.fillna(value=pd.np.nan, inplace=True)
# Turn index to DateTime
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)
# For debugging
print(df.head())

# Save to csv
df.to_csv(processed_data_path)

## To import csv file
#df2 = pd.read_csv(processed_data_path, index_col=0)
#print(df2.head())

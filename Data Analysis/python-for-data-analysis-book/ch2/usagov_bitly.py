#Find top 10 occuring time zones in USA-GV file

from pandas import DataFrame, Series
import pandas as pd
import json

path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

#Create list of timezones if they exist within file
time_zones = []
for rec in records:
    if 'tz' in rec:
        time_zones.append(rec['tz'])

#Insert counts of time zones into a dict
def get_counts(sequence):
    counts = {}
    for tz in sequence:
        if tz in counts:
            counts[tz] = counts[tz] + 1
        else:
            counts[tz] = 1
    return counts

# Get top 10 occuring time zones and their counts
def top_counts(count_seq, n = 10):
    key_value_pairs = []
    for tz, count in count_seq.items():
        key_value_pairs.append((count,tz))
    key_value_pairs.sort(reverse = True)
    return key_value_pairs[:n]
    
    
counts = get_counts(time_zones)
top10 = top_counts(counts)


## Top 10 with pandas
frame = DataFrame(records)

tz_counts = frame['tz'].value_counts()

#clean data to make matlibplot 
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ""] = 'Unknown'

tz_counts = clean_tz.value_counts()

#plot top-10
tz_counts[:10].plot(kind='barh',rot=0)




    

import pandas as pd
import re

df = pd.read_csv("C:/Users/alper/OneDrive/Masaüstü/datas.csv", sep=";")

def extract_url_and_device_type(series, device_series):
    url_regex = re.compile(r'''(
        [a-zA-Z0-9._-]+
        \.
        [a-zA-Z]{2,4}
        )''', re.VERBOSE)
    url_dict = {}
    for i, text in enumerate(series):
        matches = url_regex.findall(text)
        if matches:
            url_dict[matches[0]] = device_series[i]
    return url_dict

url_link = df["Stats_Access_Link"]
device_types = df["Device_Type"]
url_device_dict = extract_url_and_device_type(url_link, device_types)

print(url_device_dict)
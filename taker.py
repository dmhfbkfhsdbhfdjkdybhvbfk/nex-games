import ipdata
from pprint import pprint
import pandas as pd
import csv
def take_user_ip(user_ip):
    ipdata.api_key = "b59478c956aae925d4443f6c5b6f9e0c8f075d88d5888f1d843d54a7"
    response = ipdata.lookup(user_ip)

    cool = [{"STATUS":"successful",
    "IP":user_ip,
    "COUNTRY":response["country_name"],
    "COUNTRY_CODE":response["country_code"],
    "REGION":response["region"],
    "CITY":response["city"],
    "LATITUDE":response["latitude"],
    "LONGTIUDE":response["longitude"],
    "CURRENT TIME":response["time_zone"]["current_time"],
    "TIME ZONE NAME":response["time_zone"]["name"],
    "DOMAIN":response["asn"]["domain"],
    "NAME/ASN":response["asn"]["name"],
    "TYPE/ASN":response["asn"]["type"] ,
    "CALLING CODE":response["calling_code"],
    "CARRIER MCC":response["carrier"]["mcc"],
    "CARRIER MNC":response["carrier"]["mnc"],
    "CARRIER NAME":response["carrier"]["name"]}]



    # Open the file in write mode
    with open('ip.csv', 'a', newline="\n") as csv_file:
    # Create a CSV writer object
        fieldnames = ["STATUS","IP","COUNTRY","COUNTRY_CODE","REGION","CITY","LATITUDE","LONGTIUDE","CURRENT TIME","TIME ZONE NAME","DOMAIN","NAME/ASN","TYPE/ASN","CALLING CODE","CARRIER MCC","CARRIER MNC","CARRIER NAME"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,extrasaction="ignore")

        # Write the header row

        # Write the rows of the list to the CSV file
        for row in cool:
            writer.writerow(row)
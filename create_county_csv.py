import csv
import os
from glob import glob
import pandas as pd
import numpy as np

# This code pulls all data for the state selected and returns a formatted dataframe.

def create_files(state, path, files):

    county_list = []
    county_list_apr12update = []

    for i in files:

        #only files past 3/21. The data started breaking cases down by county on 3/22.
        if i[:-4] > "03-21-2020":

            with open(path+'/'+i, newline='') as csvfile:

                csvreader = csv.reader(csvfile, delimiter=',')

                for row in csvreader:

                    row_case_insensitive = [i.lower() for i in row]

                    if state in row_case_insensitive:
                        if row in county_list:
                            break
                        else:
                            if i[:-4] < "04-12-2020":
                                county_list.append(row)
                            else:
                                county_list_apr12update.append(row)
    df = pd.DataFrame(county_list_apr12update)
    df1 = pd.DataFrame(county_list)
    df1.columns = ["FIPS", "County", "State", "Country", "Date", "lat", "lon", 
        "Confirmed", "Deaths", "Recovered", "Active", "Combined_Key"]
    df.columns = ["State", "Country", "Date", "lat", "lon", "Confirmed", "Deaths", "Recovered", "Active","County","FIPS", 
        "Combined_Key","Incident_Rate","People_Tested", "People_Hospitalized", "UID", "ISO3"]
    df = df[["FIPS","County","State", "Country","Date", "lat", "lon", "Confirmed", "Deaths", "Recovered", "Active", 
        "Combined_Key","Incident_Rate","People_Tested", "People_Hospitalized", "UID", "ISO3"]]
    df = df.drop(["Incident_Rate","People_Tested", "People_Hospitalized", "UID", "ISO3"], axis=1)
    frames = [df1, df]
    combined_df = pd.concat(frames)

    return(combined_df)
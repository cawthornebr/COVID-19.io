import csv
import os
from glob import glob
import pandas as pd
import numpy as np

# This code pulls all data for the state selected and returns a formatted dataframe.

def create_files(state, path, files):

    county_list = []

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
                            county_list.append(row)
    
    df = pd.DataFrame(county_list)
    df.columns = ["FIPS", "County", "State", "Country", "Date", "lat", "lon", 
        "Confirmed", "Deaths", "Confirmed", "Active", "Combined_Key"]
    return(df)
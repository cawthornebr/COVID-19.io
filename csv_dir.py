import csv
import os
from glob import glob
import pandas as pd
import numpy as np

#This code generates a list of csv files in the directory selected.

def new_path(path_name):
    EXT = ".csv"
    all_csv_files = []
    for file in os.listdir(path_name):
        if file.endswith(EXT):
            all_csv_files.append(file)
    return(all_csv_files)
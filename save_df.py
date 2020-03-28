import csv
import os
from glob import glob
import pandas as pd
import numpy as np

def save_df(df, path, state):

    df = df.sort_values(by='County')
    path_save = f'{path}/{state}_master_file.csv'
    df.to_csv(path_save, index = False)
        

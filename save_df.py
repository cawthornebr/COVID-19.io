import csv
import os
from glob import glob
import pandas as pd
import numpy as np
import datetime as dt

from pandas import ExcelWriter

def save_df(df, path, state):

    df = df.sort_values(by='County')

    # master_df = df
    # ############################ test
    # master_df = master_df[master_df.County != 'Unassigned']
    # master_df['Date'] = master_df['Date'].apply(pd.to_datetime)
    # master_df['Date'] = master_df['Date'].dt.strftime('%m/%d')
    # master_df.sort_values(by=['County','Date'], inplace=True)
    # master_df = master_df.drop(columns=['FIPS', 'State','Country','lat','lon','Active','Combined_Key'])
    # master_df = master_df.drop(columns=['Recovered'])
    # master_df = master_df.dropna()


    # try:
    #     master_df_confirmed = master_df.pivot(index=master_df.columns[0],
    #                 columns=master_df.columns[1],
    #                 values= master_df.columns[2])
    # except:
    #     master_df_confirmed = master_df.pivot_table(index='County', columns='Date', values='Confirmed')
    # dates_confirmed = list(master_df_confirmed.columns)
    # master_df_confirmed = master_df_confirmed.sort_values(by=dates_confirmed[-1], ascending=False)
    # master_df_confirmed = master_df_confirmed.dropna()
    # master_df_confirmed=master_df_confirmed[master_df_confirmed[dates_confirmed[-1]]!=0].dropna()
    # # master_df_confirmed.to_html(f'data/{states}_data/{states}_table.html')
    # #counties
    # counties = master_df_confirmed.reset_index()
    # master_df_confirmed = master_df_confirmed.astype('int64', copy=False)
    # master_df_confirmed.loc['Total'] = master_df_confirmed.sum()

    # master_df_confirmed = pd.DataFrame(master_df_confirmed.loc["Total"])
    # master_df_confirmed = master_df_confirmed.reset_index()
    # master_df_confirmed = master_df_confirmed.transpose()
    # master_df_confirmed.columns = master_df_confirmed.iloc[0]
    # master_df_confirmed = master_df_confirmed.drop(["Date"])
    # ############################ test

    
    path_save = f'{path}/{state}_master_file.csv'
    path_save2 = f'{path}/{state}_master_file.xls'
    # path_save3 = f'{path}/{state}_master_file_total.csv'
    # path_save4 = f'{path}/{state}_master_file_county.csv'
    writer = ExcelWriter(path_save2)
    df.to_csv(path_save, index = False)
    df.to_excel(writer,'Sheet1', index=False)
    # master_df_confirmed.to_csv(path_save3,index=False)
    # counties.to_csv(path_save4,index=False)
    writer.save()
#basics
import numpy as np
import pandas as pd

##### TABLE OF CONTENTS ####
## get_co2_data(): acquires and preps data
## 
## 
## 


def get_co2_data():
    '''
    This function acquires and preps Mauna Loa CO2. Data must first exist in a csv in the working directory.
    Returns a dataframe with a datetime index and a single CO2 column.
    Assumes using file downloaded on 28JUN2022 that contains data through the end of May
    
    Returns: Pandas Dataframe
    '''
    #read csv
    dfm = pd.read_csv("monthly_in_situ_co2_mlo_28JUN2022.csv",header=56,names=['yr','mn','co2'],usecols=[0,1,4])
    #Convert to strings and pad if necessary
    dfm.yr = dfm.yr.astype(str)
    dfm.mn = dfm.mn.astype(str).str.zfill(2)
    #create date column
    dfm['date'] = dfm.yr + '-' + dfm.mn + '-15'
    #convert date column to datetime format
    dfm['date'] = pd.to_datetime(dfm.date,format="%Y-%m-%d")
    #set date column as index and sort
    dfm = dfm.set_index('date').sort_index()
    #drop the null months which are on the edges
    dfm = dfm['1964-05':'2022-05']
    return dfm
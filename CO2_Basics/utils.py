#basics
import numpy as np
import pandas as pd
#viz
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

def mlo_inset_plot(tr_mod,yrdf):
    '''
    Plots the monthly and yearly CO2 data, with an inset zoomed in on a two year period.
    '''
    fig, ax = plt.subplots(figsize=[12,6])
    #BIG PLOT
    ax.plot(tr_mod.index,tr_mod.co2,label='Monthly');
    ax.plot(yrdf.index,yrdf.co2,label='Yearly');
    ax.set_title("Observed Mauna Loa $CO_2$ Readings",size=14);
    ax.set_ylabel("$CO_2$ (ppm)",size=14);
    ax.autoscale(enable=True, axis='x', tight=True); #makes x axis tight
    #INSET PLOT
    dims = [.1, .6, .3,.3] #distance from left axis, distance from y axis, width, height
    axin = ax.inset_axes(dims) #create new axis
    axin.plot(tr_mod.co2['1994':'1995'])
    axin.plot(yrdf.co2['1993':'1995'])
    axin.set(title="Seasonal Cycle")
    #inverse colors for inset
    axin.set(facecolor='white')
    axin.grid(color='lightgrey')
    # INSET XLabel Formatting
    locator = mdates.AutoDateLocator(minticks=3,maxticks=7) #set acceptable tick range
    formatter = mdates.ConciseDateFormatter(locator) #format with concise dates
    axin.xaxis.set_major_locator(locator)
    axin.xaxis.set_major_formatter(formatter)
    # Draw lines to inset
    ax.indicate_inset_zoom(axin,edgecolor='black')
    plt.show()
    return None

def plot_mlo_seasons(m1_season,m2_season,last_full_year):
    '''
    Plots the seasonal variation of CO2 data with the two methods.
    '''
    #Show Seasonality
    plt.figure(figsize=(10,6))
    plt.bar(range(1,13),m1_season.seas_var, color=np.where(m1_season.seas_var>0, '#0173b2', '#d55e00'),label='Average Monthly Variance')
    plt.plot(range(1,13),m2_season.seasonal[last_full_year],label='Statsmodel Decomposition',marker='x',color='k')
    plt.legend()
    plt.xticks(range(1,13),labels=m1_season.mn);
    plt.ylabel("CO$_2$ Variance (ppm)");
    plt.title("Seasonal Trends in CO$_2$ Observations",size=14);
    return None
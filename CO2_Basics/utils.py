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
    plt.legend()
    plt.show()
    return None

def mlo_adj_inset_plot(tr_mod,yrdf):
    '''
    Plots the monthly and sesasonally adjusted CO2 data, with an inset zoomed in on a two year period.
    '''
    #Plot observed and seasonally adjusted
    fig, ax = plt.subplots(figsize=[12,6])
    #BIG PLOT
    ax.plot(tr_mod.co2,label='Observed')
    ax.plot(tr_mod.co2_adj,label='Seasonally Adjusted')
    ax.set_ylabel("CO$_2$ (ppm)")
    ax.set_title("Seasonally Adjusted CO$_2$ Readings",size=14);
    ax.autoscale(enable=True, axis='x', tight=True)
    #INSET PLOT
    axin = ax.inset_axes([.1, .6, .3,.3]) 
    axin.plot(tr_mod.co2['1994':'1995'],label='Observed')
    axin.plot(tr_mod.co2_adj['1994':'1995'],label='Seasonally Adjusted')
    axin.set(title="Seasonal Cycle")
    #inverse colors
    axin.set(facecolor='white')
    axin.grid(color='lightgrey')
    # INSET XLabel Formatting
    locator = mdates.AutoDateLocator(minticks=3,maxticks=7) #set acceptable tick range
    formatter = mdates.ConciseDateFormatter(locator) #format with concise dates
    axin.xaxis.set_major_locator(locator)
    axin.xaxis.set_major_formatter(formatter)
    # Draw lines to inset
    ax.indicate_inset_zoom(axin,edgecolor='black')
    plt.legend(loc=4)
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

def plot_models(te_pred):
    '''
    Plots the 3 models created against the observed values
    '''
    #Do some plotting
    plt.figure(figsize=(12,5))
    # plt.plot(tr_mod_eom.co2,label='Train')
    plt.plot(te_pred.co2,label='Observed Values')
    plt.plot(te_pred.h_linear_w_seas, label='Holt - Linear')
    plt.plot(te_pred.h_exp_w_seas, label='Holt - Exponential')
    plt.plot(te_pred.hw_ExpSmooth, label='Holt-Winters Exponential Smoothing')
    plt.title("Predicted Mauna Loa CO$_2$ Readings", size=14)
    plt.ylabel("CO$_2$ (ppm)")
    plt.legend()
    plt.show()
    return None
    
def get_custom_error(te_pred,predictions):
    '''
    Given the test predictions from a time series model, and forecasted predictions, this extrapolates an error band 
    onto the forecasted data based off of the error found in the test dataset.
    '''
    #Calculate error at given point
    te_pred['err'] = round((te_pred.co2 - te_pred['h_exp_w_seas']),2)
    #Percent error at given point
    te_pred['perc_err'] = round((te_pred.err / te_pred.co2),4)
    #create trendline
    m, b = np.polyfit(range(0,te_pred.shape[0]),te_pred.perc_err,1)
    #create substitute x values for prediction dataframe
    x = range(1,predictions.shape[0]+1)
    #Generate extrapolated error predictions
    #M*x = percent error at given point.  *Pred gets the expected error in ppm
    error = m*x*predictions.pred_w_seas
    return error
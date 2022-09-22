import pandas as pd
import numpy as np
from datetime import datetime



def store_items():
    #pull. data locally
    df = pd.read_csv("all_combined.csv", index_col= 0)
    # we can get ride of GMT time as it is all same
    df.sale_date = df.sale_date.str.replace("00:00:00 GMT","")
    df.sale_date = df.sale_date.str.strip()
    #now change it into datetime format
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
    #set date to index and sort
    df = df.set_index('sale_date').sort_index()
    #create month and day of week column
    df["month"] = df.index.month_name()
    df["day_of_week"] = df.index.day_name()
    #create new column sales total that is product of sale amount and unit price
    df["sales_total"] = df.sale_amount * df.item_price

    return df


  #######################################################################



  def opsd_data():
    #pull data from acquire
    df = acquire.get_opsd_data()
    #convert object date into datetime64
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date").sort_index()
    df["month"] = df.index.month_name()
    df["year"] = df.index.year
    df.Wind = df.Wind.fillna(0)
    df.Solar= df.Solar.fillna(0)
    df["Wind+Solar"] = df["Wind+Solar"].fillna(0)
    
    return df  
import pandas as pd
import requests
import os

#########################################################################
def get_items_data():
   
    items = []
    for page in range(1, 4):
        url = "https://python.zgulde.net/api/v1/items?page="
        url = url + str(page)
        response = requests.get(url)
        data = response.json()
        page_items = data["payload"]["items"]
        items +=page_items

    items = pd.DataFrame(items)
    return items


def items_data():
    filename = "items.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        items = get_items_data()
        items.to_csv("items.csv")
    return items

#########################################################################

def get_stores_data(url):
    response=requests.get(url)
    data = response.json()
    max_page = data["payload"]["max_page"]
    stores = []
    for page in range(1, max_page + 1):
        url = url + '?page = ' + str(page)
        response = requests.get(url)
        data = response.json()
        page_stores = data["payload"]["stores"]
        stores +=page_stores
        
    stores = pd.DataFrame(stores)
    return stores


#save stores data locally
def store_data(url):
    filename = "store.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        stores = get_stores_data(url)
        stores.to_csv("store.csv")
    return stores

#########################################################################


def get_sales_data(base_url):
    response = requests.get(base_url) 
    data = response.json() 
    maxpage = data['payload']['max_page']
    
    items= [] 

    for page in range(1, maxpage+1): 
        url = base_url + '?page=' + str(page)
        response = requests.get(url)
        page_data = response.json()
        page_items = page_data['payload']["sales"]
        items += page_items
    
    # convert list of page items to dataframe and return
    return pd.DataFrame(items)



#save sales data locally
def sales_data(url):
    filename = "sales.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        sales = get_sales_data(url)
        sales.to_csv("sales.csv")
    return sales
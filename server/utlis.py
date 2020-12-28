import json
import pickle
import numpy as np

__model=None
__data_columns=None
__location=None

def load_save_utils():
    global __model
    global __location
    global __data_columns
    with open("./files/banglore_home_price.pickle","rb") as f:
        __model=pickle.load(f)
    print("loading the Model from the directory.......")
    with open("./files/columns.json","r") as f:

        __data_columns=json.load(f)["data_columns"]
        __location=__data_columns[3:]
    print("loading the Data from the directory.....")

def get_location_names():
    return __location
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

if __name__=="__main__":
    load_save_utils()


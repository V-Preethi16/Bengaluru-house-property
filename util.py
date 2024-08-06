import json
import pickle
import numpy as np

__locations=None
__data_columns=None
__model=None
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1
    except Exception as e:
        print(f"Error finding location index: {str(e)}")
        return None
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    try:
        return round(__model.predict([x])[0], 2)
    except Exception as e:
        print(f"Error during model prediction: {str(e)}")
        return None
def get_location_names():
    return __locations

def load_saved_artifact():
    print("load saved artifact--Start")
    global __data_columns
    global __locations

    with open("./artifacts/columns1.json",'r') as f:
        data=json.load(f)
        __data_columns=data['data_columns']
        __locations= __data_columns[3:]
    global __model

    with open("E:/user personal files/Abinash/Documents/BENGALURU WEB APPLICATION/server/artifacts/bengaluru_house_data_model2.pickle",'rb') as f:
        __model=pickle.load(f)
    print("Loading saved artifacts....done")

def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifact()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3,3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2,2))
    print(get_estimated_price('Kalhalli', 1000, 2,2))
    print(get_estimated_price('Ejipura', 1000, 2,2))
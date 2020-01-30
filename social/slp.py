import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import  pickle
import os


def pre_pos(df):
    df = df.drop(["Crop_Yield"], axis="columns")

    df["District_Name"] = df["District_Name"].replace(["Cox's bazar", "Chattagram", "Rangamati", "Khagrachari",
                          "Bandarban", "Khulna", "Jessore", "Bogra", "Moulvibazar",
                                                       "Dinajpur"], [0, 1,2,3,4,5,6,7,8,9])
    df["Soil_Type"] = df["Soil_Type"].replace(["Grey Piedmont and Brown hill soils", "Brown hill soils",
                      "Acid Sulphate Soils", "Peat","Grey Terrace soils", "Grey Piedmont soils",
                                               "Grey Terrace floodplain soils"], [0, 1, 2, 3, 4, 5,6])
    df["Season"] = df["Season"].replace(["Kharif", "Rabi"], [0, 1])
    df["Pro_Name"] = df["Pro_Name"].replace(["Aus", "Aman", "Tea", "Jute", "Blackgram", "Chili",
                    "Boro", "Tobacco", "Wheat", "Chili", "Onion", "Lentil", "Barley",
                                             "Linseed", "Cotton"], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])


    return df

def training():
    df = pd.read_csv('crop.csv')
    df = pre_pos(df)
    print(df)
    y = df["Production"]
    print(y)
    df.drop("Production",  axis="columns", inplace = True)
    x = df
    print(x)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
    model = DecisionTreeRegressor( random_state = 0)
    model.fit(x, y)
    pkl_filename = "pickle_model2.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model,file)
    y_pred = model.predict(X_test)
    rms = np.sqrt(mean_squared_error(y_test, y_pred))
    print(rms)
def pred(ob):
    d1 = ob.to_dict()
    df = pd.DataFrame(d1,index=[0])
    df = pre_pos(df)

    pkl_filename = "./pickle_model2.pkl"
    pkl_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_filename)
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict(df)
    return pred

if __name__ =="__main__":
    training()

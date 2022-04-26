
import pandas as pd
import numpy as np 
import sklearn
import xgboost



from xgboost import XGBClassifier
import joblib


def predictions(input) :
    input = np.array(input)
    input = np.reshape(input,(1, input.size))
    xgb = joblib.load('XGB2.pkl')
    pred = xgb.predict(input)
    return pred 

# if pred == 0 :
#     print('Likely to be a normal individual')
#     print('Please note that this is model is at experimental stage and needs to be validated using prospective data, treat results with caution')
# if pred == 1 :
#     print('Likely to be an alpha thalassemia carrier')
#     print('\n')
#     print('Please note that this is model is at experimental stage and needs to be validated using prospective data, treat results with caution')
    
    
    
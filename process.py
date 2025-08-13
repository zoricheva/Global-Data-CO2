import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_prediction(energy):
   X_test = [energy]

   linear_model = pickle.load(open('model.pkl','rb'))
   minmax_scaler_X = pickle.load(open('scaler.pkl','rb'))
   minmax_scaler_y = pickle.load(open('scaler_y.pkl','rb'))
  
  return co2


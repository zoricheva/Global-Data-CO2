import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_prediction(energy):
   X_test = [energy]

   linear_model = pickle.load(open('model.pkl','rb'))
   minmax_scaler_X = pickle.load(open('scaler.pkl','rb'))
   minmax_scaler_y = pickle.load(open('scaler_y.pkl','rb'))

   X_test = pd.DataFrame(X_test,columns=['Electricity from fossil fuels (TWh)','Electricity from nuclear (TWh)','Electricity from renewables (TWh)'])

   X_test = minmax_scaler_X.transform(X_test)
   co2 = linear_model.predict(X_test)
   co2 = minmax_scaler_y.inverse_transform(co2)
  
return co2


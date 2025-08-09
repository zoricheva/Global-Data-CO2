import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def get_prediction(energy):
   X_test = [energy]

   pipeline = pickle.load(open('pipline.pkl', 'rb'))
   #linear_model = pickle.load(open('model41.pkl','rb'))
   #minmax_scaler_X = pickle.load(open('model41.pkl','rb'))
   
   X_test = pd.DataFrame(X_test,columns=['Electricity from fossil fuels (TWh)','Electricity from nuclear (TWh)','Electricity from renewables (TWh)'])

   #minmax_scaler_X = MinMaxScaler()
   #minmax_scaler_X.fit([X])
   #X_test = minmax_scaler_X.transform(X_test)

   
   co2 = pipeline.predict(X_test)

   
   #co2 = linear_model.predict(X_test)

   #co2 = minmax_scaler_y.inverse_transform(co2)

   return co2


#X_test = minmax_scaler.transform(np.array(X_test))

   































































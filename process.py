import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def get_prediction(energy):
   X = energy
   linear_model = pickle.load(open('model41.pkl','rb'))

   minmax_scaler_X = MinMaxScaler()
   minmax_scaler_X.fit([X])
   X_test = minmax_scaler_X.transform([X])
   
   co2 = linear_model.predict(X_test)

   return co2


#X_test = minmax_scaler.transform(np.array(X_test))

   


























































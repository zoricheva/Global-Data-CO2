import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
#from sklearn.pipeline import Pipeline


def get_prediction(energy):
   X_test = [energy]

   linear_model = pickle.load(open('model.pkl','rb'))
   minmax_scaler_X = pickle.load(open('scaler.pkl','rb'))
   
   X_test = pd.DataFrame(X_test,columns=['Electricity from fossil fuels (TWh)','Electricity from nuclear (TWh)','Electricity from renewables (TWh)'])

   X_test = minmax_scaler_X.transform(X_test)
   co2 = linear_model.predict(X_test)

   #co2 = minmax_scaler_y.inverse_transform(co2)

   return co2


#X_test = minmax_scaler.transform(np.array(X_test))

 #minmax_scaler_X = MinMaxScaler()
   #minmax_scaler_X.fit([X])
   #X_test = minmax_scaler_X.transform(X_test)

   #X_test = pipline.transform(X_test)
   #co2 = pipline.predict(X_test)
   













































































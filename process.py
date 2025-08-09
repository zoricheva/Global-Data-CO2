import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def get_prediction(energy):
   X = energy
   linear_model = pickle.load(open('model41.pkl','rb'))

   minmax_scaler_X = MinMaxScaler()
   X = minmax_scaler_X.fit_transform([X])
   #X_test = minmax_scaler.transform(np.array(X_test))
   X_test = minmax_scaler_X.transform([X])
   
   co2 = linear_model.predict(X_test)

   return co2

   
    # TODO: Добавить загрузку модели из файла
    # Примечание: если использовалась предобработка, то нужно тоже ее выполнить в коде приложения
    # TODO: Добавить получение предсказаний загруженной модели
    #co2 = 400 * energy + 345
    
   # with open('model.pkl', 'rb') as f:
       # loaded_model = pickle.load(f)
 
        
    #co2 = loaded_model.predict([(energy)])























































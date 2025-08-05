import pickle

import numpy as np

from sklearn.linear_model import LinearRegression

def get_prediction(energy):

    energy = X_test
    linear_model = pickle.load(open('model.pkl','rb'))
    co2 = linear_model.predict(X_test)
    
    # TODO: Добавить загрузку модели из файла
    # Примечание: если использовалась предобработка, то нужно тоже ее выполнить в коде приложения
    # TODO: Добавить получение предсказаний загруженной модели
    #co2 = 400 * energy + 345
    
   # with open('model.pkl', 'rb') as f:
       # loaded_model = pickle.load(f)
 
        
    #co2 = loaded_model.predict([(energy)])

     

    
    return co2
















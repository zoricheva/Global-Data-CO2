import pickle
from sklearn.preprocessing import MinMaxScaler


def get_prediction(energy):
   X_test = energy.values
   linear_model = pickle.load(open('model4.pkl','rb'))

   co2 = linear_model.predict([X_test])

   return co2

   
    # TODO: Добавить загрузку модели из файла
    # Примечание: если использовалась предобработка, то нужно тоже ее выполнить в коде приложения
    # TODO: Добавить получение предсказаний загруженной модели
    #co2 = 400 * energy + 345
    
   # with open('model.pkl', 'rb') as f:
       # loaded_model = pickle.load(f)
 
        
    #co2 = loaded_model.predict([(energy)])













































import pickle

def get_prediction(energy):
    
    # TODO: Добавить загрузку модели из файла
    # Примечание: если использовалась предобработка, то нужно тоже ее выполнить в коде приложения
    # TODO: Добавить получение предсказаний загруженной модели
    #co2 = 400 * energy + 345
    
   # with open('model.pkl', 'rb') as f:
       # loaded_model = pickle.load(f)
    
     linear_model = pickle.load(open('model.pkl','rb'))
     co2 = linear_model.predict(X_test)
        
    #co2 = loaded_model.predict([(energy)])

      co2 = co2(energy)

    
    return co2












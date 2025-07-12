

def loaded_model(energy):
  with open('model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

  return y_pred

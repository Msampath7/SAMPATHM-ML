import pickle
import numpy as np
with open('modelj.pkl', 'rb') as m:
    model = pickle.load(m)
array=np.array([1,1,1,1,1,1,1,1,1,1,1])
array=array.reshape(1,-1)
print(model.predict(array))
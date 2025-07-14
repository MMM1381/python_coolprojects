import pandas as pd
import numpy as np

class MyMinMaxScaler():
    def __init__(self,min,max):
        self.min = []
        self.max = []
        for idx,i in enumerate(min): 
            self.min.append(i)
        for idx,i in enumerate(max): 
            self.max.append(i)
        self.min = np.array(self.min)
        self.max = np.array(self.max)
    
    def transform(self,data):
        return (data - self.min) / (self.max - self.min)
    
    def inverse_transform(self,data):
        return data * (self.max - self.min) + self.min
    
    def save(self,name):
        np.save(name+'.npy',np.concatenate((self.min.reshape(1,-1), self.max.reshape(1,-1)), axis=0))
        print(f'scaler saved in {name}.npy')
    
    def load(self,name):
        arr = np.load(name+'.npy')
        self.min = arr[0]
        self.max = arr[1]

'''the usage should be somthink like this:
assume we have a dataframe that we just want to adjust 
the last column min and max our self:


mins = df_train.min().values
mins[-1]=-200
maxs = df_train.max().values
maxs[-1]=200

features_scaler = MyMinMaxScaler(min=mins,max=maxs)
scaler = MyMinMaxScaler(min=[-200],max=[200])

X,y = sequencer(df_train.values,T)
X = features_scaler.transform(X)
y = scaler.transform(y.reshape(-1,1))


val_size =int(len(X)*0.2)
x_train = X[:-val_size]
y_train = y[:-val_size]

x_val = X[-val_size:]
y_val = y[-val_size:]

x_test,y_test = sequencer(df_test.values,T)
x_test = features_scaler.transform(x_test)


'''
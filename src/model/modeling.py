import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

import warnings
warnings.filterwarnings('ignore')

class Polynomial_regression_model:

    def __init__(self, path_dataframe, scaler , degree : int):
        
        dataframe = pd.DataFrame(pd.read_csv(path_dataframe))

        # We specify this so that the train and test data set always have the same rows, respectively
        np.random.seed(0)

        myscaler = scaler
        df_transform = myscaler.fit_transform(dataframe)
        dataframe = pd.DataFrame(df_transform, index=dataframe.index, columns=dataframe.columns)
        
        y = dataframe.pop('price')
        X = dataframe
        X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=41, test_size=0.2)
    
        pipe = make_pipeline(PolynomialFeatures(degree), LinearRegression())

        pipe.fit(X_train,y_train)

        self.model = pipe

    
    def predict( self, data_X):
        return self.model.predict(data_X) 


# model = Polynomial_regression_model('src/model/dataset.csv', MinMaxScaler(), 3)
# prediction = model.predict([[1.0, 4.0, 250.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0]])
# print("my prediction :", prediction)
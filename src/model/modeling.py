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
        
        y = dataframe.pop('price')
        X = dataframe

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, random_state=41, test_size=0.2)
    
        self.model = make_pipeline(scaler, PolynomialFeatures(degree), LinearRegression())

        self.model.fit(self.X_train, self.y_train)

        self.train_r2_score = self.model.score(self.X_train, self.y_train)
        self.test_r2_score = self.model.score(self.X_test, self.y_test)
    
    def get_test_r2_score(self) -> float:
        """
        Calcule the score of the model

        Returns:
            float: [description]
        """
        return self.test_r2_score
    
    def predict(self, data_X) -> list(float):
        """
        Predict the prices of the dataframe.  

        Args:
            data_X (iterable): Data to predict on.

        Returns:
            prices (list(float)): array of price predicted from dataframe
        """
        return self.model.predict(data_X)
    
    def predict_single_point(self, x) -> float:
        """
        Predict the price of the data.  

        Args:
            data (list): Data to predict on.

        Returns:
            price (float): price predicted
        """

        # x[3] => equipped_kitchen_has
        # if equipped_kitchen_has feature is ommitted (np.nan), it is replaced with majority value of the column
        if np.isnan(x[3]):
            x[3] = self.X_train['equipped_kitchen_has'].value_counts().idxmax()

        # the data point to be predicted has to have a shape (1,10)
        X = x.reshape(1,-1)

        return self.predict(X)[0]

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class Preprocess :


    @staticmethod
    def preprocess_csv_dataset(path_csv_file : str) -> None :
        """
        This method create a new csv with clean data used by the model

        Args:
            path_csv_file (str): The path of the csv who most be cleaned
        """

        def dummy(col : str, df) -> None:
            """
            This method create new columns from different values of a column

            Args:
                col (str): The column target
                df (Dataframe): The dataframe who will receive the columns

            Returns:
                df (Dataframe): The old dataframe with news columns added 
            """

            col_enc = pd.get_dummies(df[col])
            
            df = pd.concat([df, col_enc], axis=1)
            
            #When the new columns are create we can delete the old coulumn
            df.drop([col], axis=1, inplace=True)
            
            return df
        
        df = pd.DataFrame(pd.read_csv(path_csv_file))
        df[['house_is', 'equipped_kitchen_has','furnished','open_fire','terrace','garden','swimming_pool_has']]=df[['house_is', 'equipped_kitchen_has','furnished','open_fire','terrace','garden','swimming_pool_has']].astype('int')
        
        df = dummy('region', df)
        df = dummy('building_state_agg', df)

        df.drop_duplicates()

        delete_col = ['postcode','source','property_subtype','facades_number','furnished','open_fire','swimming_pool_has', 'land_surface','terrace','terrace_area','garden','garden_area']
        df = df.drop(delete_col, axis=1)
        
        df.to_csv("src/model/dataset.csv", index=False)


    
    

Preprocess.preprocess_csv_dataset("src/model/FINAL_clean_sales_dataset.csv")

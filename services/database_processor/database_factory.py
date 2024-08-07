import pandas as pd
from services.database_processor.database_builder import DataBaseBuilder
from services.database_processor.database_QA import DatabaseQA
from services.database_processor.database_survey import DatabaseSurvey

class DatabaseFactory(DataBaseBuilder):
    def __init__(self,) -> None:
        self.data_type = None

    def get_database(self,data_type :str) -> pd.DataFrame:
        '''
        Return a a database depending of data type selected

        paramater:
        -data_type (str)

        return: 
        - pd.Dataframe

        types or specialties:
        - data_type:'qa'
        - data:'survey'

        Example:

        DatabaseFactory().get_database(data_type = 'qa')

        Previous code returns entire QA's database. This can help us to get the raw data of the 
        database would like to extract from local path. 
        '''
        try:
            if data_type == 'qa':
                self.raw_data = DatabaseQA().get_database()
                return self.raw_data
            elif data_type == 'survey':
                pass                
        except Exception as e:
            print('Please type a valid input')


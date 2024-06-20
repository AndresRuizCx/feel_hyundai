import pandas as pd
import os
import sys
from services.database_processor.database_builder import DataBaseBuilder
from services.file_processor.file_processor_factory import FileProcessorFactory
from services.database_path.data_path import DataPath

class DatabaseSurvey(DataBaseBuilder):

    def __init__(self) -> None:
        pass

    def get_database(self, lob: str) -> pd.DataFrame:
        '''
        Creates Survey database from local path

        paramater:
        -lob (str)

        return: 
        - pd.Dataframe

        types or specialties:
        - lob:'blcc'
        - lob:'gccc'
        - lob:'hccc'

        Example:

          DatabaseSurvey().get_database(lob = 'blcc')

        Previous code returns BLCC's database. This can help us to identify which
        database would like to extract from local path      
        '''
        if lob == 'blcc': 
            folder_path = DataPath()._get_survey_blcc()
        elif lob == 'gccc':
            folder_path = DataPath()._get_survey_gccc()
        elif lob == 'hccc':
            folder_path = DataPath()._get_survey_hccc()

        df_list = []

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path,file)

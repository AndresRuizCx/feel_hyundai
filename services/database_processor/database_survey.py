import pandas as pd
import os
from services.database_processor.database_builder import DataBaseBuilder
from services.file_processor.file_processor_factory import FileProcessorFactory
from services.database_path.data_path import DataPath

class DatabaseSurvey(DataBaseBuilder):

    def __init__(self, data_path: DataPath, file_processor_factory: FileProcessorFactory) -> None:
        self.data_path = data_path
        self.file_processor_factory = file_processor_factory

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
        folder_path = self._get_folder_path(lob)

        df_list = []

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            file_processor = self.file_processor_factory.create_file_processor(file_path=file_path)
            df_aux = file_processor.process_files()
            df_list.append(df_aux)
        
        self.raw_data = pd.concat(df_list, axis=0, ignore_index=True)
        folder_name = folder_path.split('\\')[-1]
        print(f'Working on folder: {folder_name}')
        
        return self.raw_data

    def _get_folder_path(self, lob: str) -> str:
        if lob == 'blcc': 
            return self.data_path._get_survey_blcc()
        elif lob == 'gccc':
            return self.data_path._get_survey_gccc()
        elif lob == 'hccc':
            return self.data_path._get_survey_hccc()
        else:
            raise ValueError(f"Unknown LOB: {lob}")

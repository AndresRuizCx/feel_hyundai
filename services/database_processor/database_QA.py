import pandas as pd
import os
import sys
from services.database_processor.database_builder import DataBaseBuilder
from services.file_processor.file_processor_factory import FileProcessorFactory
from services.database_path.data_path import DataPath

class DatabaseQA(DataBaseBuilder):
    def __init__(self) ->None:
        pass

    def get_database(self) -> pd.DataFrame:
        '''
        Creates QA database from local path.
        
        Return: pd.DataFrame
        
        '''
        df_list = []
        qa_folder = DataPath().get_QA()

        # Moving on folders
        for folder in os.listdir(qa_folder):

            # Creating folder path
            sub_folder_path = os.path.join(qa_folder, folder)
            print(f'Working on file: {folder}...')

            # Moving on files
            for file in os.listdir(sub_folder_path):
                # Creating file path
                file_path = os.path.join(sub_folder_path, file)
                file_processor = FileProcessorFactory().create_file_processor(file_path)
                aux_df = file_processor.process_files()

                for col in aux_df.columns:
                    new_name = ''.join(char for char in col if not char.isdigit())
                    aux_df = aux_df.rename(columns={col:new_name})
                
                df_list.append(aux_df)

        # Creating database raw data
        self.raw_data = pd.concat(df_list, axis=0, ignore_index=True)
        print(f'Data loaded sucessfully')

        return self.raw_data
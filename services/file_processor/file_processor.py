import pandas as pd
import os
from abc import ABC, abstractmethod

class FileProcessor(ABC):

    def __init__(self,file_path: str):
        self.file_path = file_path
        self.data_frame = None

    @abstractmethod
    def process_files(self) -> pd.DataFrame:
        ''' Abstract Method. To re-write'''
        pass

class CSVProcessor(FileProcessor):
    def process_files(self) -> pd.DataFrame:
        '''
        Read a Csv file to return it as Pandas Dataframe
        
        '''
        self.data_frame = pd.read_csv(self.file_path)
        return self.data_frame
    
class ExcelProcessor(FileProcessor):  
    def process_files(self) -> pd.DataFrame:
        '''
        Read a Excel file to return it as Pandas Dataframe
        
        '''
        self.data_frame = pd.read_excel(self.file_path, engine='openpyxl')
        return self.data_frame
    
class ParquetProcessor(FileProcessor):
    def process_files(self) -> pd.DataFrame:
        '''
        Read a Parquet file to return it as Pandas Dataframe
        
        '''
        self.data_frame = pd.read_parquet(self.file_path)
        return self.data_frame
import os

class DataPath:
    def __init__(self) -> None:
        self.raw_data_path = None
    
    def get_QA(self) -> str:
        '''
        Get QA raw data (private)

        '''
        self.raw_data_path = 'C:\\Users\\andres.ruiz\\Documents\\GitHub\\feel_hyundai\\raw_data\\data_qa'
        return self.raw_data_path
    
    def get_survey(self) -> str:
        '''
        Get Survey raw data (private)
        
        '''
        self.raw_data_path = 'C:\\Users\\andres.ruiz\\Documents\\GitHub\\feel_hyundai\\raw_data\\data_survey'
        return self.raw_data_path
    
    def _get_survey_blcc(self) -> str:

        '''
        Get Survey BLCC data (private)
        '''
        return 'C:\\Users\\andres.ruiz\\Documents\\GitHub\\feel_hyundai\\raw_data\\data_survey\\blcc_sat'
    
    def _get_survey_gccc(self) -> str:

        '''
        Get Survey GCCC data (private)
        '''
        return 'C:\\Users\\andres.ruiz\\Documents\\GitHub\\feel_hyundai\\raw_data\\data_survey\\gccc_sat'

    
    def _get_survey_hccc(self) -> str:

        '''
        Get Survey HCCC data (private)
        '''
        return 'C:\\Users\\andres.ruiz\\Documents\\GitHub\\feel_hyundai\\raw_data\\data_survey\\hccc_sat'

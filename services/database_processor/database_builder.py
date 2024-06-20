import pandas as pd
from abc import ABC, abstractmethod

class DataBaseBuilder:

    def __init__(self) -> None:
        self.raw_data = None

    @abstractmethod  
    def get_database(self) -> pd.DataFrame:
        pass


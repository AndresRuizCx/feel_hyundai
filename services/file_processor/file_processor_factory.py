from services.file_processor.file_processor import *

class FileProcessorFactory:

    def __init__(self) -> None:
        pass

    def create_file_processor(self, file_path: str) -> FileProcessor:

        '''
        Create an Object FileProcessor that allow to
        return a Dataframe depending on the ".filetype"

        Example:

        file_path = 'example.csv'

        return: FileProcessor(csv)

        to get a pd.Dataframe (method):
        process_files() -> pd.Dataframe
        '''
        
        if file_path.endswith(".csv"):
            return CSVProcessor(file_path=file_path)
        elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            return ExcelProcessor(file_path=file_path)
        elif file_path.endswith('.parquet'):
            return ParquetProcessor(file_path=file_path)
        else:
            raise ValueError(f'Unsupported file type: {file_path}') 
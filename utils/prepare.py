# prep functions for data processing
import os 
import pandas as pd
def import_data(data_dir, file_name=None):
    """
    Import data from the data directory
    """
    # check if data directory exists
    # get the directory of the current project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print(f"Project root: {project_root}")
    full_path = os.path.join(project_root, data_dir)
    if not os.path.exists(full_path):
        raise ValueError(f"Data directory {full_path} does not exist")

    
    # check if data directory is empty
    if len(os.listdir(data_dir)) == 0:
        raise ValueError(f"Data directory {data_dir} is empty")
    elif file_name is None:
        # get file names that exist in the data directory
        files = os.listdir(data_dir)
        # take the first .csv file 
        for file in files:
            if file.endswith('.csv'):
                data_dir = os.path.join(data_dir, file)
                break
        # import data
        df = pd.read_csv(os.path.join(data_dir))
    else: 
        # import data
        df = pd.read_csv(os.path.join(data_dir, file_name, '.csv'))
    
    return df





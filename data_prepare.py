import os
import numpy as np
import sktime
from sktime.datasets import load_from_tsfile

DATA_PATH = './Monash_UEA_UCR_Regression_Archive/'

def convert_to_npy(data_):
    data_ = np.array(data_)
    data_shape2 = len(data_[0,0])
    data = np.zeros((data_.shape[0], data_.shape[1], data_shape2), dtype=np.float64)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data[i, j, :] = np.array(data_[i, j])
    return data

for data in ['BIDMC32HR', 'BIDMC32RR', 'BIDMC32SpO2']:
    '''
    If you have a UnicodeDecodeError: 'utf-8' :
    You can edit load_from_tsfile_to_dataframe function in sktime/datasets/_readers_writers/ts.py 
    Replace with open(full_file_path_and_name, encoding="utf-8") encoding with "cp1252".
    '''
    train_x, train_y = load_from_tsfile(os.path.join(DATA_PATH, f"{data}/{data}_TRAIN.ts"))
    test_x,  test_y  = load_from_tsfile(os.path.join(DATA_PATH, f"{data}/{data}_TEST.ts"))
    np.save(f'dataset/{data}_train_x',convert_to_npy(train_x))
    np.save(f'dataset/{data}_train_y',train_y)
    np.save(f'dataset/{data}_test_x', convert_to_npy(test_x))
    np.save(f'dataset/{data}_test_y', test_y)

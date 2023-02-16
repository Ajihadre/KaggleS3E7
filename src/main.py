# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:59:47 2023

@author: tcaron
"""

import sys
import pandas as pd
sys.path.insert(0, './src')
import warnings

if __name__ == '__main__':
    warnings.simplefilter("ignore", UserWarning)
    """
    CHEMIN A MODIFIER :
    """
    path = "/Users/tcaron/Documents/Python Scripts/KaggleS3E7/data/"
    train = pd.read_csv(path+"train.csv")
    test = pd.read_csv(path+"test.csv")
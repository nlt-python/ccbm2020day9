import pandas as pd  
import numpy as np 

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, log_loss
from sklearn.model_selection import train_test_split


def load_data(filename='data/Student Dataset.xlsx'):
    '''
    Input: 
    - Excel file path and name. NB: Only loads a spreadsheet, not a workbook of multiple spreadsheets

    Output: 
    - pandas dataframe where column titles = first row of spreadsheet and
                                dataframe index = first column of spreadsheet
    '''

    return pd.read_excel(filename, header=0, index_col=0)


def convert_ints(dframe, lst_old, lst_new):
    '''
    Input: 
    NB: Uses load_data() to generate dataframe
    - takes a list of values to be replaced
    - takes a second list of values for replacing with

    Output: 
    - pandas dataframe where all values of M/F, Yes/No and Y/No are replaced with 1/0
    '''

    dframe.replace(lst_old, lst_new, inplace=True)
    return dframe


def ohe(dframe, a_series):
    '''
    Input: 
    - pandas Dataframe
    - pandas Series containing categorical data (a column from the dataframe)

    Output:
    - pandas Dataframe with the categorical column one-hot encoded. Original column is retained
    '''
    









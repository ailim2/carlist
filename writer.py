import os
from openpyxl import load_workbook
import pandas as pd

class Writer:

    def write_data(self, df):
        if os.path.exists('data.csv') == False:
            df.to_csv('data.csv', index=False)

        if os.path.exists('data.csv') == True:
            df.to_csv('data.csv', mode='a', header=False, index=False)

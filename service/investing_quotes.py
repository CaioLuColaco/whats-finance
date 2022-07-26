import sys
import os

from pandas_datareader import data as web
from datetime import date, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def get_values(ativo):
    date_yesterday = date.today()
    date_yesterday = date_yesterday.strftime('%m-%d-%Y')
    df = web.DataReader(f'{ativo}', data_source='yahoo', start=date_yesterday, end=date_yesterday)
    return df
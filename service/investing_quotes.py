import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from pandas_datareader import data as web
from datetime import date, timedelta

def get_values(ativo):
    date_yesterday = date.today() - timedelta(1)
    date_yesterday = date_yesterday.strftime('%m-%d-%Y')
    df = web.DataReader(f'{ativo}', data_source='yahoo', start=date_yesterday, end=date_yesterday)
    return df
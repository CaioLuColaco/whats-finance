import sys
import os
import traceback

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from pandas_datareader import data as web
from utils import errorLogger, errorTrigger, infoLogger
from datetime import date, timedelta

def get_values(ativo):
    try:
        infoLogger(os.path.basename(__file__), 'Getting quote values')
        date_yesterday = date.today() - timedelta(1)
        date_yesterday = date_yesterday.strftime('%m-%d-%Y')

        df = web.DataReader(f'{ativo}', data_source='yahoo', start=date_yesterday, end=date_yesterday)
        infoLogger(os.path.basename(__file__), 'quotes obtained successfully')
        return df
    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        errorLogger(traceback.format_tb(exc_traceback)[1], error)
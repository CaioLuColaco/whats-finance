import os
import sys
import traceback

from config.settings import *
from utils import errorLogger, errorTrigger, infoLogger
import pywhatkit 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def send_whatsapp(ativo, df):
    try:
        infoLogger(os.path.basename(__file__), 'Starting message sending')
        
        pywhatkit.sendwhatmsg_instantly("+85981888144", f"Valor de fechamento do ativo {ativo} ontem e valor atual:\n{df['Adj Close']}", 15, True, 4)
        
        infoLogger(os.path.basename(__file__), 'The messages have been sent')
    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        errorLogger(traceback.format_tb(exc_traceback)[1], error)

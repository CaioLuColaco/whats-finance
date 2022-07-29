import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from service.investing_quotes import get_values
from service.send_whats import send_whatsapp
from utils import errorLogger, errorTrigger, infoLogger

def whats_finance_robot():
    infoLogger(os.path.basename(__file__), 'Starting Robot')
    ativo = "BTC-USD"
    df = get_values(ativo)

    send_whatsapp(ativo, df)
    infoLogger(os.path.basename(__file__), 'finished Robot')
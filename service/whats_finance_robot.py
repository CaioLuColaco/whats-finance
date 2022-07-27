import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from service.investing_quotes import get_values
from service.send_whats import send_whatsapp

def whats_finance_robot():
    print("iniciando o robô")
    ativo = "BTC-USD"
    df = get_values(ativo)

    send_whatsapp(ativo, df)
    print("Encerrou")

whats_finance_robot()





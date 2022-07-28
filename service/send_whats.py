import os
import sys

from config.settings import *

import pywhatkit 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def send_whatsapp(ativo, df):
    print("Iniciando o envio da mensagem")

    pywhatkit.sendwhatmsg_instantly("+85981888144", f"Valor de fechamento do ativo {ativo} ontem e valor atual:\n{df['Adj Close']}", 15, True, 4)
    print("Successfully Sent!") 

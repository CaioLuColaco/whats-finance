import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from service.investing_quotes import get_values

def whats_finance_robot():
    df = get_values("BTC-USD")

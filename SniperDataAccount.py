from binance.client import Client
from binance.enums import *

class Account:
    def __init__(self):
        self.api_key = ''           # clé public contenant le token de connexion au compte client
        self.api_secret = ''        # clé PRIVÉ contenant le token de connexion au compte client
        self.Client = Client(self.api_key, self.api_secret)
        self.BoolAccount = True

    def GetBool(self):
        return self.BoolAccount

    def Login(self):
        account_info = self.Client.get_account()
        return account_info
    
    def Snipe(self, symbol, Qty):
        try:
            self.Client.create_order(
                symbol = symbol,
                side = SIDE_BUY,
                type = ORDER_TYPE_MARKET,
                quantity = Qty,
            )
            print("notif    : - - {} sniped to {} - -".format(Qty, symbol))
            self.BoolAccount = False
        except:
            print("err code : - - echec - -")
            
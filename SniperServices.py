import SniperDataAccount
import threading

class Service:
    def __init__(self):
        self.AccountInstance = SniperDataAccount.Account()
        self.AccountInfo = self.AccountInstance.Login()
        self.BalanceInfo = self.AccountInfo['balances']
        self.BoolService = True

    def LogIn(self):
        self.AccountInfo = self.AccountInstance.Login()
        self.BalanceInfo = self.AccountInfo['balances']

    def GetSniperDeviceValue(self, SniperDevice):
        self.LogIn()
        for e in self.BalanceInfo:
            if e['asset'] == SniperDevice:
                return float(e['free'])
            
    def GetNewListingTitleValue(self, NewListingTitle):
        self.LogIn()
        for e in self.BalanceInfo:
            if e['asset'] == NewListingTitle:
                return float(e['free'])

    def Snipe(self, SniperAmount, SniperDevice, NewListingTitle):
        symbol = NewListingTitle + SniperDevice
        while self.BoolService:
            SendRequestForSnipe = threading.Thread(target=self.AccountInstance.Snipe, args=(symbol, SniperAmount,))
            SendRequestForSnipe.start()
            self.BoolService = self.AccountInstance.GetBool()

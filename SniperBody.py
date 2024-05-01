import SniperServices
import hashlib
import time

RUNNING = True
InputPassWord = hashlib.sha256((input('\nPassword required :\n → ')).encode('utf-8')).hexdigest()
PassWord = ''

while RUNNING :
    if InputPassWord == PassWord :

        ISLABELFALSE = True
        Service = SniperServices.Service()       

        while ISLABELFALSE :
            NewListingTitle = input('Confirm\n\nNew-Listing title required :\n → ')
            if isinstance(NewListingTitle, str):
                ISLABELFALSE = False
        print('Title entered : {}\n'.format(NewListingTitle))

        ISLABELFALSE = True
        while ISLABELFALSE :
            SniperDevice = input('StableToken title required ( USDT | USDC | FDUSD | EURT) :\n → ')
            if SniperDevice == 'USDT' or SniperDevice == 'USDC' or SniperDevice == 'FDUSD' or SniperDevice == 'EURT':
                ISLABELFALSE = False
        print('Device entered : {}\n'.format(SniperDevice))

        SniperDeviceAvailable = Service.GetSniperDeviceValue(SniperDevice)

        ISLABELFALSE = True
        while ISLABELFALSE :
            SniperAmount = input('Sniper-Amount required ({} {} available) :\n → '.format(SniperDeviceAvailable, SniperDevice))
            if SniperAmount.isdigit() and int(SniperAmount) <= SniperDeviceAvailable and int(SniperAmount) > int(SniperDeviceAvailable)/2:
                ISLABELFALSE = False
            else:
                print('] {} ; Sniper-Amount ; {} ]'.format(round(SniperDeviceAvailable/2, 2), round(SniperDeviceAvailable, 2)))
        print('Amount entered : {}\n'.format(SniperAmount))

        ISLABELFALSE = True
        while ISLABELFALSE :
            DoISnipe = hashlib.sha256((input('{} {} will be snipe to {}. enter Password again to confirm :\n → '.format(SniperAmount, SniperDevice, NewListingTitle))).encode('utf-8')).hexdigest()
            if DoISnipe == PassWord :
                Service.Snipe(int(SniperAmount), SniperDevice, NewListingTitle)
                ISLABELFALSE = False
        RUNNING = False
    else :
        InputPassWord = hashlib.sha256((input('Password required :\n → ')).encode('utf-8')).hexdigest()

time.sleep(2)

print('_________________________\n\nCurrent wallet : {} {}, {} {}\nsystem end\n_________________________\n'.format(Service.GetSniperDeviceValue(SniperDevice), SniperDevice, Service.GetNewListingTitleValue(NewListingTitle), NewListingTitle))
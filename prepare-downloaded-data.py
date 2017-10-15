'''
Takes a ANZ CSV download and produces two output CSV.

One file is of payments out of the account, the other
is of receipts into the account. 

The column ordering of each is specific to our needs
with the existing spreadsheet
'''
import os
import csv
import pprint
from configparser import ConfigParser

DATADIR = "D:\data\NZPUG\NZPUG-16-17-Balance-Sheet-Inputs"
INPUTFILENAME = "06-0158-0360348-00_Transactions_2016-09-01_2017-08-31.csv"
OUTPUTPAYMENTSFILENAME = "PAYMENTSOUT-2016-09-01_2017-08-31.csv"
INPUTRECEIPTSFILENAME = "RECEIPTSIN-2016-09-01_2017-08-31.csv"


def getConfig():
    '''
    Read the standard and 'local only' configs
    and build a corresponding dictionary of values
    '''
    parser = ConfigParser()
    parser.read('anzaccountinfomessage.ini')
    dicout = {}
    dicout['OUTPUTPAYMENTSFILENAME'] = parser.get('DEFAULT', 'OUTPUTPAYMENTSFILENAME')
    dicout['INPUTRECEIPTSFILENAME'] = parser.get('DEFAULT', 'INPUTRECEIPTSFILENAME')
    #Switch to local only config
    parserlocal = ConfigParser()
    parserlocal.read('anzaccountinfomessage-localonly.ini')
    dicout['DATADIR'] = parserlocal.get('DEFAULT', 'DATADIR')
    dicout['INPUTFILENAME'] = parserlocal.get('DEFAULT', 'INPUTFILENAME')

    return dicout
    

def makeFileNames(dicConfig):
    dicOut = {
            'IN' : os.path.join(dicConfig['DATADIR'], dicConfig['INPUTFILENAME']),
            'OUTPAYMENTS' : os.path.join(dicConfig['DATADIR'], dicConfig['OUTPUTPAYMENTSFILENAME']),
            'INRECEIPTS' : os.path.join(dicConfig['DATADIR'], dicConfig['INPUTRECEIPTSFILENAME'])
            }
    return dicOut

def manageProcessing(dicFileNames):
    with open(dicFileNames['IN'], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
             
            pprint.pprint(row)
            print("")


def main():
    print("Version 1")
    config = getConfig()
    dicFileNames = makeFileNames(config)
    manageProcessing(dicFileNames)

if __name__ == "__main__":
    main()

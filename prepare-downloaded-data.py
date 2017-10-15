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
from decimal import Decimal
from datetime import datetime

CREDITKEYS = ['DateISO', 'Amount', 'DateISO', 'Type', 'Details', 'Code', 'Particulars', 'Reference',  'Amount', 'DateISO']
DEBITKEYS = ['DateISO', 'Amount', 'Type', 'Details', 'Code', 'Particulars', 'Reference', 'Amount', 'DateISO', 'ForeignCurrencyAmount']


def getConfig():
    '''
    Read the standard and 'local only' configs
    and build a corresponding dictionary of values
    '''
    parser = ConfigParser()
    parser.read('anzaccountinfomessage.ini')
    dic_out = {}
    dic_out['OUTPUTPAYMENTSFILENAME'] = parser.get('DEFAULT', 'OUTPUTPAYMENTSFILENAME')
    dic_out['INPUTRECEIPTSFILENAME'] = parser.get('DEFAULT', 'INPUTRECEIPTSFILENAME')
    # Switch to local only config
    parserlocal = ConfigParser()
    parserlocal.read('anzaccountinfomessage-localonly.ini')
    dic_out['DATADIR'] = parserlocal.get('DEFAULT', 'DATADIR')
    dic_out['INPUTFILENAME'] = parserlocal.get('DEFAULT', 'INPUTFILENAME')

    return dic_out


def makeFileNames(dic_config):
    '''
    Manipulate config values into full paths
    '''
    dic_out = {
            'IN': os.path.join(dic_config['DATADIR'], dic_config['INPUTFILENAME']),
            'OUTPAYMENTS': os.path.join(dic_config['DATADIR'], dic_config['OUTPUTPAYMENTSFILENAME']),
            'INRECEIPTS': os.path.join(dic_config['DATADIR'], dic_config['INPUTRECEIPTSFILENAME'])
            }
    return dic_out


def provideISOVersionOfDate(strdmy):
    '''
    Take a string containging a dmy date
    and output it as YYYY-MM-DD

    Assumes 'y' in input is a four figure
    year
    '''

    lst_dt_elems = strdmy.split("/")
    strdtout = "{}-{}-{}".format(lst_dt_elems[2], lst_dt_elems[1], lst_dt_elems[0])
    return strdtout


def getDateTimeAsISO():
    '''
    Return current datetime in ISO
    '''
    d = datetime.now()
    return d.strftime('%Y%m%dT%H%M%S')


def makeentrysequence(dic_entry, key_seq):
    '''
    Prepare a list of dictionary keys
    with which to select elements from
    the entry dictionaries

    Also do something weird in order to provide
    an empty column to categories the entries
    by when they're used in the target workbook.
    '''

    colcnt = 0
    lst_out = []

    for k in key_seq:
        lst_out.append(dic_entry[k])

    # This is the idiosyncratic bit of processing
    # where we insert an empty column immediately
    # after the first column
    lst_out_final = lst_out[0:1]
    lst_out_final.extend([''])
    lst_out_final.extend(lst_out[1:])

    return lst_out_final


def renameFileIfNess(path):
    '''
    If the `path` file already exists rename it
    with an the current datetime in ISO formate
    appended onto the end of the file name
    '''

    if os.path.isfile(path):
        new_path = path + "." + getDateTimeAsISO()
        print("About to rename : " + path + " to " + new_path)
        os.rename(path, new_path)


def manageProcessing(dic_file_paths):
    '''
    Read inputs and output outputs !
    '''
    lst_entries = []
    cnt_in = 0
    cnt_crd_out = 0
    cnt_dbt_out = 0

    # Preprocess the input data
    with open(dic_file_paths['IN'], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cnt_in += 1
            tmprow = row
            tmprow['DateISO'] = provideISOVersionOfDate(tmprow['Date'])
            lst_entries.append(tmprow)

    import pprint
    pprint.pprint(lst_entries)

    # Rename any existing output credits file if necesary
    renameFileIfNess(dic_file_paths['OUTPAYMENTS'])

    # Output the credits
    lst_credits = []
    with open(dic_file_paths['OUTPAYMENTS'], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for dic_entry in lst_entries:
            if Decimal(dic_entry['Amount']) > 0:
                cnt_crd_out += 1
                writer.writerow(makeentrysequence(dic_entry, CREDITKEYS))

    # Rename any existing output debits file if necesary
    renameFileIfNess(dic_file_paths['INRECEIPTS'])

    # Output the debits
    lst_debits = []
    with open(dic_file_paths['INRECEIPTS'], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for dic_entry in lst_entries:
            if Decimal(dic_entry['Amount']) < 0:
                cnt_dbt_out += 1
                writer.writerow(makeentrysequence(dic_entry, DEBITKEYS))

    # Report row counts
    print("")
    print("Count of rows in : " + str(cnt_in))
    print("Count of credit rows out : " + str(cnt_crd_out))
    print("Count of debit rows out : " + str(cnt_dbt_out))


def main():

    print("Version 2")
    print("")

    config = getConfig()
    dic_file_paths = makeFileNames(config)
    manageProcessing(dic_file_paths)

if __name__ == "__main__":
    main()

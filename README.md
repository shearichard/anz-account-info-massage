# ANZ Account CSV Download Massage  
These simple scripts are a utility for processing ANZ CSV download files.

Their very limited funcitonality is of use to me but, I think , unlikely to be of use to anyone else. However feel free to look.


## Invoking prepare-downloaded-data.py ##
The `prepare-downloaded-data.py` script takes no arguments so invoke is like this.
```
python prepare-downloaded-data.py
```
##  Tested Environments ##
### Windows / Python 2.x ###
This code has only been run in Python 2.x on Windows 7. It may work elsewhere but it may need tweaking to do so.

### Windows and Virtenvs ###
The `requirements.txt` defines the necessary Python libraries and in the dev env I used a virtenv .

There's something a bit weird (to me) about using virtenvs on windows so as a memory jogger here's how to invoke the virtenv (which is called 'anzmassage' in the dev env).

```
.\anzmassage\Scripts\activate.bat
```
## configuration Files ##
### Primary config files ###
There is a primary config file which is used to contain data I don't mind committing to git.
It's called `anzaccountinfomessage.ini` and the format is like this :

```
[DEFAULT]
OUTPUTPAYMENTSFILENAME = PAYMENTSOUT-2016-09-01_2017-08-31.csv
INPUTRECEIPTSFILENAME = RECEIPTSIN-2016-09-01_2017-08-31.csv
```
`OUTPUTPAYMENTSFILENAME` is the name which will be used for the output payments CSV file.
`INPUTRECEIPTSFILENAME` is the name which will be used for the output receipts CSV file.

## 'Local only' config files ##
There is a 'local only' config which is used to contain data I don't want to commit to git.
It's called `anzaccountinfomessage-localonly.ini`, it doesn't appear in the repository but the format of it is like this :

```
[DEFAULT]
DATADIR=adir
INPUTFILENAME = afile.csv 
```

Reasonably self-explanatory : `DATADIR` is the directory in which the input data is expected to be found and the output data will be written; `INPUTFILENAME` is the name of the file which was downloaded from ANZ exactly as it was received.

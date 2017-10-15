# ANZ Account CSV Download Massage  
These simple scripts are a utility for processing ANZ CSV download files.

Their very limited funcitonality is of use to me but, I think , unlikely to be of use to anyone else. However feel free to look.


## Invoking prepare-downloaded-data.py ##
The `prepare-downloaded-data.py` script takes no arguments so invoke is like this.
```
python prepare-downloaded-data.py
```
## Windows and Virtenvs ##
Just because I forget how this stuff works in Windows this is how you invoke the virtenv (which is called 'anzmassage' in the dev env).

```
.\anzmassage\Scripts\activate.bat
```
## 'Local only' configs ##
There is a 'local only' config which is used to contain data I don't want to commit to git.
It's called `anzaccountinfomessage-localonly.ini` and the format of it is like this :

```
[DEFAULT]
DATADIR=adir
INPUTFILENAME = afile.csv 
```

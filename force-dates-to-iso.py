import tempfile
import os

LSTDATEIN = [
'31/05/2016',
'30/05/2016',
'30/05/2016',
'30/05/2016',
'30/05/2016',
'30/05/2016',
'30/05/2016',
'30/05/2016',
'25/05/2016',
'25/05/2016',
'25/05/2016',
'04/05/2016',
'03/05/2016',
'02/05/2016',
'29/04/2016',
'14/04/2016',
'14/04/2016',
'30/03/2016',
'01/03/2016',
'29/02/2016',
'01/02/2016',
'11/01/2016',
'11/01/2016',
'11/01/2016',
'30/12/2015',
'08/12/2015',
'04/12/2015',
'30/11/2015',
'20/11/2015',
'05/11/2015',
'30/10/2015',
'27/10/2015',
'27/10/2015',
'23/10/2015',
'14/10/2015',
'14/10/2015',
'14/10/2015',
'05/10/2015',
'05/10/2015',
'05/10/2015',
'05/10/2015',
'05/10/2015',
'05/10/2015',
'05/10/2015',
'30/09/2015',
'29/09/2015',
'10/09/2015',
'10/09/2015',
'10/09/2015',
'08/09/2015',
'07/09/2015',
'03/09/2015',
'03/09/2015',
'03/09/2015',
'03/09/2015',
'03/09/2015',
'02/09/2015',
'01/09/2015',
'01/09/2015',
'01/09/2015',
'01/09/2015',
'31/08/2015',
'31/08/2015',
'31/08/2015',
'31/08/2015',
'31/08/2015',
]

def makeTempDir():
    path2dir = tempfile.mkdtemp()
    return path2dir
def getTempPath(fName, dPath=None):
    if dPath==None:
        path2dir = makeTempDir()
    else:
        path2dir = dPath
    fullpath = os.path.join(path2dir,fName)
    return fullpath


def main(lstDateIn):

    pthToTmpOutFile = getTempPath("force-dates-to-iso.txt")
    print(pthToTmpOutFile)

    with open(pthToTmpOutFile, 'wt') as f:
        for d in lstDateIn:
            lstDtElems = d.split("/")
            strDtOut = "{}-{}-{}".format(lstDtElems[2],
                                    lstDtElems[1],
                                    lstDtElems[0])
            f.write(strDtOut)
            f.write('\n')





if __name__ == '__main__':
    main(LSTDATEIN)



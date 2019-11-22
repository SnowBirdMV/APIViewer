from ftplib import FTP
import ftplib
import os
import string
import random
import shutil
import time

dirPath = os.path.dirname(os.path.realpath(__file__))
testFilePath = os.path.join(dirPath, 'testFiles')
downloadsFilePath = os.path.join(dirPath, 'Downloads')
tempFilePath = os.path.join(dirPath, 'tmp')

def ftpLogin():
    ftp = FTP('seappserver1.rit.edu')
    ftp.login('', '')
    return ftp

def uploadFile(ftp, filePath):
    tmpFilePath = generateTmpFile(filePath)
    fp = open(tmpFilePath, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(tmpFilePath), fp, 1024)
    return os.path.splitext(os.path.basename(tmpFilePath))[0]

def retrieveFile(ftp, destinationPath):
    fileName = os.path.basename(destinationPath)
    print(fileName)
    oldDir = ftp.pwd()
    ftp.cwd(ftp.pwd() + '/Completed/')
    if os.path.exists(destinationPath):
        os.remove(destinationPath)
    handle = open(destinationPath, 'wb')
    while True:
        try:
            ftp.retrbinary('RETR %s' % fileName, handle.write)
            break
        except ftplib.error_perm:
            print(ftp.nlst())
            print('file not ready yet, retrying in 5 seconds')
            time.sleep(5)
    handle.close()
    ftp.cwd(oldDir)

def generateTmpFile(filePath):
    fileName = os.path.basename(filePath)
    baseFileName, extension = os.path.splitext(fileName)
    newFileName = randomString(20) + extension
    destPath = os.path.join(tempFilePath, newFileName)
    shutil.copy(filePath, destPath)
    return destPath

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    ftp = ftpLogin()
    tmpFileName = uploadFile(ftp, os.path.join(testFilePath, 'Application_L_Page_002.png'))
    print( os.path.join(downloadsFilePath, tmpFileName + '.txt'))
    retrieveFile(ftp, os.path.join(downloadsFilePath, tmpFileName + '.txt'))

if __name__ == '__main__':
    main()
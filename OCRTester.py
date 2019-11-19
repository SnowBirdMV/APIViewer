import requests
import xml.etree.ElementTree as ET
import json
import sys
import os
import time

dirPath = os.path.dirname(os.path.realpath(__file__))
testFilePath = os.path.join(dirPath, 'testFiles')

def processFile(filePath):
    file = {'data' : open(filePath, 'rb')}
    r = requests.post('http://seappserver1.rit.edu/OCRService/api/ProcessFile', files=file)
    return json.loads(r.text)

def processFileAsync(filePath):
    file = {'data': open(filePath, 'rb')}
    r = requests.post('http://seappserver1.rit.edu/OCRService/api/ProcessFileAsync', files=file)
    return json.loads(r.text)

def GetProcessedFile(fileName):
    while True:
        r = requests.get('http://seappserver1.rit.edu/OCRService/api/GetProcessedFile?fileName=' + fileName)
        rJSON = json.loads(r.text)
        if rJSON['_fileReady']:
            break
        print(rJSON)
        time.sleep(5)

def main():
    fileName = 'Application_L_Page_002.png'
    filePath = os.path.join(testFilePath, fileName)
    processFileAsync(filePath)
    #processFile(filePath)
    GetProcessedFile(fileName)

if __name__ == '__main__':
    main()
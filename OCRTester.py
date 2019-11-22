import requests
import xml.etree.ElementTree as ET
import json
import sys
import os
import time

dirPath = os.path.dirname(os.path.realpath(__file__))
testFilePath = os.path.join(dirPath, 'testFiles')
downloadsFilePath = os.path.join(dirPath, 'Downloads')

def processFile(filePath):
    fileName = os.path.basename(filePath)
    print('location: ' + os.path.join(downloadsFilePath, fileName))
    file = {'data' : open(filePath, 'rb')}
    r = requests.post('http://seappserver1.rit.edu/OCRService/api/ProcessFile', files=file)
    rJSON = json.loads(r.text)
    newFilePath = os.path.join(downloadsFilePath, os.path.splitext(filePath)[0] + '.txt')
    overwriteExistingFile(newFilePath, rJSON['_text'])
    print(r.text)
    return json.loads(r.text)

def processFileAsync(filePath):
    fileName = os.path.basename(filePath)
    print('location: ' + os.path.join(downloadsFilePath, fileName))
    file = {'data': open(filePath, 'rb')}
    r = requests.post('http://seappserver1.rit.edu/OCRService/api/ProcessFileAsync', files=file)
    rJSON = json.loads(r.text)
    overwriteExistingFile(os.path.join(downloadsFilePath, fileName), rJSON['_text'])
    print(r.text)
    return json.loads(r.text)

def GetProcessedFile(fileName):
    while True:
        r = requests.get('http://seappserver1.rit.edu/OCRService/api/GetProcessedFile?fileName=' + fileName)
        rJSON = json.loads(r.text)
        if rJSON['_fileReady']:
            break
        print(rJSON)
        time.sleep(5)
    return r

def overwriteExistingFile(filePath, content):
    if os.path.exists(filePath):
        os.remove(filePath)
    with open(filePath, 'w') as file:
        file.write(content)

def main():
    fileName = 'Application_L_Page_002.png'
    filePath = os.path.join(testFilePath, fileName)
    #processFileAsync(filePath)
    result = processFile(filePath)
    print(result['_text'])

if __name__ == '__main__':
    main()
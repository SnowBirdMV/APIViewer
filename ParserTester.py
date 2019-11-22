import requests
import xml.etree.ElementTree as ET
import json
import sys
import os
from pprint import pprint

dirPath = os.path.dirname(os.path.realpath(__file__))
testFilePath = os.path.join(dirPath, 'testFiles')
downloadsFilePath = os.path.join(dirPath, 'Downloads')


def processFile(filePath):
    fileName = os.path.basename(filePath)
    print('location: ' + os.path.join(downloadsFilePath, fileName))
    file = {'data' : open(filePath, 'rb')}
    r = requests.post('http://seappserver1.rit.edu/parserservice/api/ReadForm', files=file)
    rJSON = json.loads(r.text)
    return rJSON


def main():
    pprint(processFile(os.path.join(testFilePath, 'Application_L_Page_002.txt')))


if __name__ == '__main__':
    main()
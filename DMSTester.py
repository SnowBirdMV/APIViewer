import requests
import xml.etree.ElementTree as ET
import json
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
downloadsPath = os.path.join(dirPath, 'Downloads')

def getFileList():
    r = requests.get('http://seappserver1.rit.edu/DMService/api/ListFiles')
    fileInfo = json.loads(r.text)
    return fileInfo

def downloadFile(fileName):
    r = requests.get('http://seappserver1.rit.edu/DMService/api/DownloadFile?fileName=' + fileName)
    filePath = os.path.join(downloadsPath, fileName)
    if os.path.exists(filePath):
        os.remove(filePath)
    with open(filePath, 'wb') as file:
        file.write(r.content)
    return filePath


def main():
    fileInfo = getFileList()
    print(fileInfo[0]['fileName'])
    downloadFile(fileInfo[0]['fileName'])

if __name__ == '__main__':
    main()
import requests
import xml.etree.ElementTree as ET
import json
import sys
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
testFilePath = os.path.join(dirPath, 'testFiles')

def main():
    with open(os.path.join(testFilePath, 'testTextFile.txt'), "r") as file:
        content = file.read()


if __name__ == '__main__':
    main()
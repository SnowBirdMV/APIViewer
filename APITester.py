import DMSTester as DMSService
import OCRTester as OCRService

def main():
    fileList = DMSService.getFileList()
    fileName = fileList[0]['fileName']
    filePath = DMSService.downloadFile(fileName)

main()

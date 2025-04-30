from  PyPDF2 import PdfReader
import os 
os.system("cls")
def read_custom_page_info(inFilePath,inPageNumber):
  page_text =None
  try:
      with open(inFilePath, 'rb') as pdfFile:
            readerObject = PdfReader(pdfFile)
            if readerObject.is_encrypted:
              readerObject.decrypt("")
            numberOfPages = len(readerObject.pages)
            if(inPageNumber<1 or inPageNumber > numberOfPages):
              raise ValueError("\nfata error page number is out of range..")
            pageObj= readerObject.pages[inPageNumber-1]
            page_text = pageObj.extract_text()
  except Exception as e:
       print(f"\n Hey encounterd an error :{e}")
  return page_text
pdfFilepath = "C://Users//LENOVO/Downloads//Python Cheat Sheet.pdf"
page_number= int(input("please enter the page number to read: "))  
read_custom_page_info = read_custom_page_info(pdfFilepath,page_number)  
if read_custom_page_info:
    print(f"\nNow printing the data from the pade numver {page_number}:\n\n{read_custom_page_info}")
else:
    print("\nNo data found for the given page number.")
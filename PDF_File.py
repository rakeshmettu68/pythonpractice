import os 
from PyPDF2 import PdfReader,PdfMerger,PdfWriter
os.system("cls")
#Reading the all pages in the pdf
def readAllPages(inFilePath):
    pdfPagesText = []
    try:
        with open(inFilePath, 'rb') as pdfFile:
          readerObject = PdfReader(pdfFile)
          if readerObject.is_encrypted:
            readerObject.decrypt("")
          numberOfPages = len(readerObject.pages)
          for pageNum in range(numberOfPages):
              pageObj = readerObject.pages[pageNum]
              pageData = pageObj.extract_text()
              pdfPagesText.append(pageData)
    except Exception as e:
       print(f"Hey encounter an error :{e}\n")
    return pdfPagesText
#Reading only specific page as per the end user request
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
#merging the two pdf files
def merge_files(pdfFile2merge,outmerge):
  merge_obj = PdfMerger()
   
  for pdf in pdfFile2merge:
    merge_obj.append(pdf)
  merge_obj.write(outmerge)
  merge_obj.close()
  return
   
#spiliting the pdf file
def spilting_pdf_file(inPdfFile,outputDirectory):
  try:
    
    with open(inPdfFile,"rb") as myPDFfile:
       readerObj = PdfReader(myPDFfile)
       numberOfPages = len(readerObj.pages)
       for pageNum in range(numberOfPages):
          writeObject = PdfWriter()
          writeObject.add_page(readerObj.pages[pageNum])
          splitPdfPath = os.path.join(outputDirectory,f"page_{pageNum+1}.pdf")
          with open(splitPdfPath,"wb")as splitPdfFile:
             writeObject.write(splitPdfFile)
          print(f"Created a split File :{splitPdfPath}")
  except FileNotFoundError as FileNotFoundObj:
      print(f"Error:The given file {inPdfFile} is not found")
      print(f"File not found : {FileNotFoundObj}")
  except PermissionError as permissionObj:
      print(f"Error: Permission denied to read the filr {inPdfFile} or write the output to {outputDirectory}")
      print(f"Permission denied : {permissionObj}")
  except Exception as e:
      print(f"Error:unexpcted error encountered",end="\n")
      print(f"An error occurred: {e}")
  return 
      
   
if __name__=="__main__":
    pdfFilePath = "C://Users//LENOVO//Downloads//Rakesh_MBA_resume.pdf"
    print("\nReading PDF file ...\n1.Read All pages \n2.Read Specific page \n3.Merge PDFs\n4.Spiliting Pdf\n5.addwater Mark3",end="\n")
    
    inReadChoice = int(input("\nPlease Enter Your Reading choise from the menu: "))
    if inReadChoice == 1:
      allPageInfo = readAllPages(pdfFilePath)
      for pageIndex ,outpage in enumerate(allPageInfo,start=1):
          print(f"Now printing the page Number {pageIndex}:\n\n{outpage}")
    elif inReadChoice == 2:
      page_number= int(input("please enter the page number to read: "))  
      read_custom_page_info = read_custom_page_info(pdfFilePath,page_number)  
      if read_custom_page_info:
        print(f"\nNow printing the data from the pade numver {page_number}:\n\n{read_custom_page_info}")
      else:
         print("\nNo data found for the given page number.")
    elif inReadChoice == 3:
       inFile1="C://Users//LENOVO//Downloads//Rakesh_MBA_resume.pdf"
       inFile2="C://Users//LENOVO//Downloads//GBS.pdf"
       pdfFile2merge =[inFile1,inFile2]
       outmerge = "C://Users//LENOVO//Desktop//file handling//merge.pdf"
       merge_files(pdfFile2merge,outmerge)
       print("\nMerging the file is done Go and check given file path....")
       print(f"\nThe merged file has been saved as {outmerge}\n")
    elif inReadChoice==4:
       pdfFilePath = "C://Users//LENOVO//Downloads//GBS.pdf"
       outputDirectory = "C://Users//LENOVO//Desktop//file handling//"
       spilting_pdf_file(pdfFilePath,outputDirectory)
       print("\nSplitting the file is done Go and check given directory path....")
       print(f"\nThe splitted files are saved in {outputDirectory}\n")
    else:
        print("\nInvalid choice. Please try again.")
        sys.exit()
                
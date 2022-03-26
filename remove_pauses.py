from PyPDF2 import PdfFileWriter, PdfFileReader
import os

dirr = "./pdfs"
out_dir = "./out"

def main():
    
    for file in os.listdir(dirr):
        remove_pauses(f'{dirr}/{file}')
    
def remove_pauses(filename):
    if filename.split(".")[-1] != "pdf":
        print("Not a pdf: ", filename)
        return
    infile = PdfFileReader(filename, 'rb')
    output = PdfFileWriter()
        
    cnt = 0
    for i in range(1, infile.getNumPages()):
        if not infile.getPage(i - 1).extractText() in infile.getPage(i).extractText():
            cnt += 1
            output.addPage(infile.getPage(i - 1))
    output.addPage(infile.getPage(-1))
            
    print(cnt)

    file = filename[len(dirr) + 1:]
    # print(file)
    with open(f'{out_dir}/{file[:file.find(".pdf")]}_pauses_removed.pdf', 'wb') as f:
        output.write(f)
        
main()
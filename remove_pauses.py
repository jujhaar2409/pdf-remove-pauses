from PyPDF2 import PdfWriter, PdfReader
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
    infile = PdfReader(filename, 'rb')
    output = PdfWriter()
        
    cnt = 0
    for i in range(1, len(infile.pages)):
        if not infile.pages[i-1].extract_text() in infile.pages[i].extract_text():
            cnt += 1
            output.add_page(infile.pages[i-1])
    output.add_page(infile.pages[i-1])
            
    print(cnt)

    file = filename[len(dirr) + 1:]
    # print(file)
    with open(f'{out_dir}/{file[:file.find(".pdf")]}_pauses_removed.pdf', 'wb') as f:
        output.write(f)
        
main()


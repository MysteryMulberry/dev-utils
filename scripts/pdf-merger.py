import sys
from PyPDF2 import PdfMerger

def merge_pdfs(files, output):
    merger = PdfMerger()
    for f in files:
        merger.append(f)
        print(f'  Added: {f}')
    merger.write(output)
    merger.close()
    print(f'Merged to: {output}')

if __name__=='__main__':
    merge_pdfs(sys.argv[1:-1], sys.argv[-1])

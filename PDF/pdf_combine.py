import PyPDF2
import sys

input = sys.argv[1:]

def combine(input):
    merge = PyPDF2.PdfFileMerger()
    for pdf in input:
        merge.append(pdf)
    merge.write('files/super.pdf')

combine(input)
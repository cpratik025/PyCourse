import PyPDF2
#rb represents read in binary mode
with open('files/dummy.pdf','rb') as file:
    reader= PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page_read = reader.getPage(0)
    rotate=page_read.rotateClockwise(180)
    writer= PyPDF2.PdfFileWriter()
    writer.addPage(rotate)
    with open('files/rotate.pdf','wb') as write:
        writer.write(write)
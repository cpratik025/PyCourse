import PyPDF2

water_mark = PyPDF2.PdfFileReader(open('files/super.pdf','rb'))
super_pdf = PyPDF2.PdfFileReader(open('files/wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for pages in range(super_pdf.getNumPages()):
    page =  super_pdf.getPage(pages)
    page.mergePage(water_mark.getPage(0))
    output.addPage(page)
    with open('files/watermarked.pdf','wb') as file:
        output.write(file)

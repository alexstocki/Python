from PyPDF2 import merger, PdfFileMerger, PdfFileReader, PdfFileWriter

def get_watermarked(virgin_file, watermark_file):
    v_pdf = PdfFileReader(open(virgin_file, 'rb'))
    w_pdf = PdfFileReader(open(watermark_file, 'rb'))

    output_file = PdfFileWriter()
    watermark = w_pdf.getPage(0)

    for i in range(v_pdf.getNumPages()):
        page = v_pdf.getPage(i)
        page.mergePage(watermark)
        output_file.addPage(page)    
    return output_file
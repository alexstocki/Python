import PyPDF2
import sys
from pathlib import Path
from functions import get_watermarked

options = 0

while True:
    try:
        if options:
            path_base = input('Directorio: ')
        else:
            path_base = sys.argv[1]

        pathlist = Path(str(path_base)).glob('**/*.pdf')
        new_file = PyPDF2.PdfFileMerger()

        for path in pathlist:
            if str(path) != 'w_mark.pdf':
                new_file.append(str(path))

        new_file.write('super.pdf')

        salida = get_watermarked('super.pdf', 'w_mark.pdf')

        merged_file = open('superduper.pdf','wb')

        salida.write(merged_file)
        print('Proceso finalizado con exito\n')
        break
    except IndexError:
        print('\nNo se recibio directorio como argumento\n')
        options = 1
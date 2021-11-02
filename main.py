import camelot as cam
from requests import get
import tabula


def extract_table_from_pdf():
    while True:
        try:
            f = open("table.pdf", 'wb')
            f.write(
                get("https://www.southalabama.edu/mathstat/personal_pages/mulekar/st550/Krishnakumar.pdf", ).content)
            f.close()

            table = cam.read_pdf("table.pdf", pages='3', flavor='stream')
            # table[0].df[[5, 6]].to_excel("camelot_demo.xls")
            print(table[0])

            break
        except Exception as e:
            print(e)
            raise


extract_table_from_pdf()

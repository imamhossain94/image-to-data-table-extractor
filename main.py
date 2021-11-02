from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"table.png"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)
# " ".join(text.split())
# print(text[:-1])

list_x = text.split('\n')
list_y = []
for x in list_x:
    if x.strip() not in "      ":
        # print(x.strip())
        list_y.append(x.strip())

# print(list_y)

header = list_y[0].split(' ')
data = list_y[1:]

values = []
for d in data:
    values.append(d.split(' '))

finalData = {
    "header": header,
    "values": values
}


print(finalData)

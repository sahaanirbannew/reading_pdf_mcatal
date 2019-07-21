import PyPDF2
import re

file_pdf = 'D:/pdf/Modulkatalog_SoSe2019.pdf'
file_write = 'D:/pdf/output.txt'
pdfFileObj = open(file_pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
text = ''
count = 13


while count < 695:
    pageObj = pdfReader.getPage(count)
    text = text + pageObj.extractText()
    count = count + 1

text = text.replace("\n", "")                   # Removes the new lines.
text = text.replace("   ", " ")
text = text.replace("  ", " ")

text = re.sub(r'(Seite).[0-9][0-9].(Inhaltsverzeichnis)', '', text)
text = re.sub(r'(Seite).[0-9][0-9][0-9].(Inhaltsverzeichnis)', '', text)
text = text.replace('Modulbezeichnung:', 'uModulbezeichnung:')
text = re.sub(r'(engl.).(uModulbezeichnung:)', 'engluodulbezeichnung:', text)

f = open('D:/pdf/raw_text.txt', 'w', encoding='utf-8')
f.write(text)
f.close()


print("check that out.")
course_list = text.split('uModulbezeichnung:')

text = ''
line = 0
print(len(course_list))

# create the file:
f = open(file_write, 'w', encoding='utf-8')
f.close()

while line < len(course_list):
    new_string = course_list[line].replace('uModulbezeichnung:', 'engl. Modulbezeichnung:')
    print(new_string)
    text = 'Modulbezeichnung: ' + new_string + '\n'
    f = open(file_write, 'a', encoding='utf-8')
    f.write(text)
    f.close()
    line = line + 1




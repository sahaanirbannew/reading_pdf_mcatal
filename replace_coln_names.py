import text_to_table
from gTrans import translate

field_names_de_en = []
field_names = []

for field in text_to_table.fields:
    field_en = translate(field)
    confirm = input('Is '+field_en+' a correct translation?')
    if confirm != 'yes':
        field_en = input('Enter correct translation:')

    field_names_de_en.append(field)
    field_names_de_en.append(field_en)
    field_names.append(field_names_de_en)

print(field_names)

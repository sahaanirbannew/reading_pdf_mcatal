import text_to_table


def create_file(line, number):

    # Constructing the file name of individual courses.
    file_path = 'D:/pdf/Modulkatalog_SoSe2019/'
    file_name = line.split('Kürzel:')[1].split('ggf. Untertitel:')[0].strip().replace('/', '-')
    if file_name == '':
        file_name = 'CODE'+str(number)+file_name

    # Creating the document which maps the course name with the file name:
    course_name = line.split('Modulbezeichnung:')[1].split('engluodulbezeichnung:')[0].strip()
    course_log = open(file_path+'course_index.csv', 'a', encoding='utf-8')
    course_log.write(course_name+','+file_name+'\n')
    course_log.close()

    # If English, create a separate list of courses
    course_lang = line.split('Sprache:')[1].split('Zuordnung zum Curriculum:')[0].strip()
    if course_lang != 'deutsch':
        course_log2 = open(file_path + 'course_index_english.csv', 'a', encoding='utf-8')
        course_log2.write(course_name + ',' + file_name + '\n')
        course_log2.close()

    # Adding the extension to the file names.
    file_name = file_name + '.txt'

    if file_name != '.txt':
        #print(file_name)
        field_num = 0
        trans_field_name = ''

        f = open(file_path+file_name, 'w', encoding='utf-8')

        while field_num < 21:
            # start = text_to_table.fields[field_num]  # == old
            start = text_to_table.fields_tn[field_num][0]
            #print(start)
            final_text = ''
            trans_field_name = text_to_table.fields_tn[field_num][1]

            if field_num != 20:
                end = text_to_table.fields_tn[field_num + 1][0]
                text = line.split(start)[1].split(end)[0].strip()
                if text == '':
                    final_text = trans_field_name + 'no values' + '\n'
                else:
                    final_text = trans_field_name + text + '\n'
            else:
                end = text_to_table.fields[field_num]
                text = line.split(end)[1].strip()
                if text == '':
                    final_text = trans_field_name + 'no values' + '\n'
                else:
                    final_text = trans_field_name + text + '\n'

            # Write to the file.
            f.write(final_text)
            field_num = field_num + 1
        f.close()


file_path = 'D:/pdf/output.txt'
file = open(file_path, 'r', encoding='utf-8')
line = file.readline().strip()
file_number = 0

while line != '':
    create_file(line, file_number)
    line = file.readline()
    file_number = file_number + 1

file.close()

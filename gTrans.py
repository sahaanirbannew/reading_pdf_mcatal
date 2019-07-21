from googletrans import Translator
import datetime


def translate(text):
    print("Original: " + text)
    translator = Translator()
    text = translator.translate(text, dest='EN')
    #print("Translated: " + text.text)
    text = text.text
    return text


# weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# translator = Translator()
# date = datetime.datetime.now()
# day_no = date.weekday()
# day = weekDays[day_no]
# print(day)
# text = day
# text = translate(text)
# print(text)

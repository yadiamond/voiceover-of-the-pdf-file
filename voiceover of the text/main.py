import pyttsx3
import fitz

#инициализация озвучкера
engine = pyttsx3.init()


path = input('enter path to pdf file')
#открытие пдф файла, ввод страницы и вывод текста
pdf_file = path
pdf_document = fitz.open(pdf_file)

page_number = int(input())

page = pdf_document[(page_number - 1)]

text = page.get_text()

engine.say(text)
engine.runAndWait()

pdf_document.close()


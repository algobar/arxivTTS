from gtts import gTTS
import PyPDF2

file = open("test.pdf",'rb')
pdf_file = PyPDF2.PdfFileReader(file)

page = pdf_file.getPage(0)


txt = page.extractText()

language = 'en'

ob = gTTS(text=txt,lang=language,slow=False)

ob.save("test.mp3")

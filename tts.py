from gtts import gTTS
import PyPDF2
import logging
import argparse

def file_to_pdf(filename):
    logger = logging.getLogger("TTS")
    try:
        assert isinstance(filename,str)
        file = open(filename,'rb')
        pdf_file = PyPDF2.PdfFileReader(file)

        return pdf_file
    except AssertionError:
        logger.error("filename is not a string!")
        exit(1)
    except FileExistsError:
        logger.error("file does not exist")
        exit(1)
    except FileNotFoundError:
        logger.error("file not found")
        exit(1)

def run(filename):
    logger = logging.getLogger("TTS")
    pdf = file_to_pdf(filename)

    if pdf is None:
        logger.error("file_to_pdf returned an error, exiting")
        exit(1)

    print(pdf.pages)


'''
txt = page.extractText()

language = 'en'

ob = gTTS(text=txt,lang=language,slow=False)

ob.save("test.mp3")

'''
if __name__ == "__main__":

    logger = logging.getLogger("TTS")
    logger.setLevel("INFO")
    logger.info("welcome to arxiv text to speech conversion!")

    run("test")
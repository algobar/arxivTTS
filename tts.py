from gtts import gTTS
import PyPDF2
import logging
import argparse


class ArxivTTS:
    '''
        Initial class to handle the conversion from pdf to text
    '''

    __name__ = "arxivTTS"

    def __init__(self):

        self.logger = self.__setup_logging__()
        self.logger.info("welcome to arxiv text to speech conversion!")

    def __file_to_pdf__(self,filename):
        '''
        private
        :param filename: string of a pdf file
        :return: pdf class of the file
        '''

        try:
            assert isinstance(filename, str), "not a string"
            file = open(filename, 'rb')
            pdf_file = PyPDF2.PdfFileReader(file)

            return pdf_file
        except AssertionError as e:
            self.logger.error(e.args[0])
            exit(1)
        except FileExistsError:
            self.logger.error("file does not exist")
            exit(1)
        except FileNotFoundError:
            self.logger.error("file not found")
            exit(1)

    def __setup_logging__(self):
        '''
        initializes the logger for printing
        :return: nothing
        '''

        logger = logging.getLogger("arxivTTS")
        stdout = logging.StreamHandler()
        formatter = logging.Formatter('%(name)s::%(message)s')
        stdout.setFormatter(formatter)
        logger.addHandler(stdout)
        logger.setLevel("DEBUG")

        return logger

    def run(self,filename):
        '''
        public, runs the conversion to mp3
        :param filename: string of path leading to filename
        :return: nothing
        '''

        pdf = self.__file_to_pdf__(filename)
        file_title = filename.split("/")[-1].split(".")[0]
        txt = ""

        for num,pages in enumerate(pdf.pages):
            self.logger.info("pre-processing page {}".format(num))
            txt += pages.extractText()

        language = 'en'
        ob = gTTS(text=txt, lang=language, slow=False)
        ob.save(file_title+".mp3")

        if pdf is None:
            self.logger.error("file_to_pdf returned an error, exiting")
            exit(1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('filename',default=None)
    args = parser.parse_args()

    arxiv_tts = ArxivTTS()
    arxiv_tts.run(args.filename)

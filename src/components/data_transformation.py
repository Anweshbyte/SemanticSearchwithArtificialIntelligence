import os
import sys
from dotenv import load_dotenv
load_dotenv()
folder_path = os.environ['FOLDER_PATH']
sys.path.append(folder_path)
from src.exception import CustomException
from src.logger import logging

import pandas as pd
import PyPDF2
import docx

folder = os.path.join(folder_path,"source_docs")
files = os.listdir(folder)

def update_all_files():
    df= pd.read_csv(os.path.join(folder,"file_status.csv"))
    files_rn = df['File_name'].unique()
    for file in files:
        if file not in files_rn:
            df.loc[len(files_rn)]=[file,0]
    df.to_csv(os.path.join(folder,"file_status.csv"), index=False)


def gen_para_file(file_name):
    file_extension = os.path.splitext(file_name)[1]
    if (file_extension=='.pdf'):
        return gen_para_pdf(file_name)
    elif (file_extension == '.doc' or file_extension=='.docx'):
        return gen_para_doc(file_name)
    elif (file_extension=='.txt'):
        return gen_para_txt(file_name)
    logging.info("Paragraph of {} is generated.".format(file_name))

def gen_para_pdf(file_name):
    file_path = os.path.join(folder, file_name)
    
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            paragraphs=[]
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text = page.extract_text()
                paragraph = text.split('.\n')
                for para in paragraph:
                    paragraphs.append(para)
            return paragraphs
    else:
        logging.info("File {0} not found.".format(file_name))
        paragraph=[]
        return paragraph

def gen_para_doc(file_name):
    file_path = os.path.join(folder, file_name)
    if os.path.isfile(file_path):
        doc = docx.Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            if (paragraph) :
                p_text = paragraph.text
                if len(p_text):
                    text.append(p_text)
        return text
    else:
        logging.info("File {0} not found.".format(file_name))
        paragraph=[]
        return paragraph
    

def gen_para_txt(file_name):
    file_path = os.path.join(folder, file_name)
    paragraphs=[]
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            paragraph = str(text).split('.\n')
            for para in paragraph:
                if (para):
                    paragraphs.append(para)
        return paragraphs
    else:
        logging.info("File {0} not found.".format(file_name))
        paragraph=[]
        return paragraph
    
if __name__=="__main__":
    update_all_files()
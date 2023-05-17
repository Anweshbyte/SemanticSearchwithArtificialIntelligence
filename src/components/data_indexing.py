import os
import sys
from dotenv import load_dotenv
load_dotenv()
folder_path = os.environ['FOLDER_PATH']
sys.path.append(folder_path)
from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import gen_para_file, update_all_files
from src.utils import Pinecone
from src.utils import Embeddings

import pandas as pd
path_to_csv = os.path.join(folder_path,"source_docs","file_status.csv")
import torch 
import numpy as np

class DataIndexing:
    def __init__(self) :
        self.db = Pinecone()
        self.db.connect_index()
        logging.info("Pinecone is connected.")
        self.tf = Embeddings()
        logging.info("Albert Model is initialised.")
        self.data = pd.DataFrame(columns=["id","vector","meta"])
        self.i= 1+ self.db.curr_size()

    def vectorize_file(self,filename):
        paragraphs = gen_para_file(filename)
        logging.info("will be appending in pinecone from location {}.".format(i))
        for para in paragraphs:
            vector = self.tf.embeddings(para)
            self.data.loc[len(self.data.index)] = [str(self.i),vector,{"text":para.split(" ")}]
            self.i+=1
        logging.info("{} is vectorized".format(filename))
        logging.info("Size of the input dataframe is {}.".format(len(self.data.index)))
    
    def upsert_files(self):
        self.db.upsert_data(self.data)
        logging.info("files got upserted.")
        self.data = pd.DataFrame(columns=["id","vector","meta"])

if __name__=="__main__":
    DI = DataIndexing()
    print("Here are the list of files in your source_docs folder and their upload status : ")
    update_all_files()
    file_list = pd.read_csv(path_to_csv)
    print(file_list)
    print("Write the indices of the files you want to upload seaparated by a space. (Eg: 0 1 to upload the first 2 files in the list.)")
    file_idx = map(int,input().split())
    
    for i in file_idx:
        row = file_list.iloc[i]
        file_name=row['File_name']
        print(file_name)
        DI.vectorize_file(file_name)
        file_list.at[i,"Upload_status"]=1

    DI.upsert_files()
    
    print(file_list)
    file_list.to_csv(path_to_csv,index=False)
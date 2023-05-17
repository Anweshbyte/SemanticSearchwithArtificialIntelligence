# any functionalities used in entire project
import os
import sys
import numpy as np
import pandas as pd
import torch
from dotenv import load_dotenv
load_dotenv()
import pinecone

folder_path = os.environ['FOLDER_PATH']
sys.path.append(folder_path)
from src.logger import logging
from src.exception import CustomException



class Pinecone:
    def __init__(self):
        pinecone_api_key = os.environ['PINECONE_API_KEY']
        pinecone_environment = os.environ['PINECONE_ENVIRONMENT']
        self.index_name = os.environ['INDEX_NAME']
        logging.info("Initialising Pinecone.")
        pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)

    
    def is_index_present(self) :
        if self.index_name in pinecone.list_indexes():
            return True
        else:
            return False
    
    def create_index(self):
        try:
            logging.info("Creating Pinecone index.")
            pinecone.create_index(self.index_name, dimension=768, metric="cosine")
        except Exception as e :
            raise CustomException(e,sys)

    def connect_index(self):
        try:
            if (self.is_index_present()== False):
                self.create_index()
            logging.info("Connecting to pinecone index {}".format(self.index_name))
            self.index = pinecone.Index(index_name=self.index_name)
        except Exception as e :
            raise CustomException(e,sys)
        
    def curr_size(self):
        dictionary=self.index.describe_index_stats()
        n= dictionary['total_vector_count']
        return n
    
    def upsert_data(self,data):
        logging.info("Entered the data upsertion method.")
        try:
            self.index.upsert(vectors = zip(data.id,data.vector,data.meta))
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def search(self,vector,top_k):
        df = self.index.query(vector=vector,top_k=top_k,
                              include_values=False,include_metadata=True)
        return df
    
class Embeddings:
    def __init__(self):
        logging.info("Initialising transformers.")
        try :
            from transformers import AlbertTokenizer,AlbertModel
            self.model = AlbertModel.from_pretrained("albert-base-v2")
            self.tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
        except Exception as e:
            raise CustomException(e,sys)
        
    def tokenize_sentences(self,text):
        try :
            token=self.tokenizer.tokenize(text)
            token = self.tokenizer.convert_tokens_to_ids(token)
            return token
        except Exception as e:
            raise CustomException(e,sys)

    def embeddings(self,text):
        try :
            token = self.tokenize_sentences(text)
            with torch.no_grad():
                output = self.model(torch.tensor(token).unsqueeze(0))
                return output[1][0].tolist()
        except Exception as e:
            raise CustomException(e,sys)
        


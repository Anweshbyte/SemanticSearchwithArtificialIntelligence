import sys
import os
from dotenv import load_dotenv
load_dotenv()
folder_path = os.environ['FOLDER_PATH']
sys.path.append(folder_path)
from src.exception import CustomException
from src.logger import logging
from src.utils import Pinecone
from src.utils import Embeddings

class Search:
    def __init__(self,inp_query: str, top_k):
        self.db = Pinecone()
        self.db.connect_index()
        self.tf = Embeddings()
        self.inp_query = inp_query
        self.top_k = int(top_k)
    
    def predict(self):
        try:
            vector = self.tf.embeddings(self.inp_query)
            logging.info("Embedding generated for query.")
            top_k=self.top_k
            df = self.db.search(vector=vector,top_k=top_k)
            logging.info("Query done.")
            answers= []
            for mat in df['matches']:
                m = " ".join(mat['metadata']['text'])
                answers.append(m)
            logging.info("Answers generated.")
            return answers
        except Exception as e:
            raise CustomException(e,sys)
        
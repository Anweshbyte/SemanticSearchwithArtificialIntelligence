# Semantic Search with Artificial Intelligence

**Project Overview:**
This project aims to implement a semantic search using artificial intelligence. This project uses Pinecone as the vector database to store the user's text files. The project supports three types of files: word (.doc or .docx), text (.txt), and pdf (.pdf) files. Using the Huggingface's ALBERT model, the text in these files is converted into vectors and then upserted to a Pinecone index. The project has a frontend page where the user can search his query for similarity within the text stored in the Pinecone index. The user's query is also embedded into a vector using Huggingface's ALBERT model and then a similiarity search is carried out using Pinecone's inbuilt functions. The search results represent the text stored in the Pinecone index resembling the user's query, ranked based on relevance.

## Installation
### Requirements
1. Python 3.6 or higher
2. pip

### Setup Project
1. Fork the repository.
2. Clone the repository. In your terminal, type:
  <pre><code>git clone https://github.com/your-username/SemanticSearchwithArtificialIntelligence.git</code></pre>
3. Set up a python virtual environment.
    1. Install virtualenv using the following command: <code> pip install virtualenv</code>
    2. Navigate to your project directory.
    3. Create a new virtual environment. <code> virtualenv env </code>.
    4. Activate the virtual environment. On Windows , <code>env\Scripts\activate.bat</code>. On Linux/macOS , <code>source env/bin/activate</code>.
4. Install the required packages: <code> pip install -r requirements.txt</code>
5. Add your text files to the folder **source-docs**.
6. Rename the .env.sample file to .env  and fill in the following details : your Pinecone API key, Pinecone Environment name, Pinecone Index Name and the location of this project folder in your system.
7. Run the data_indexing.py file and give the file index as input to embed the text in the file into vectors and upsert them into the Pinecone index.
8. Run the app.py file and search http://127.0.0.1:8000 on the browser.

### Project Structure
1. **source_docs** : All the files (pdf, word or text) that are to be upserted to the vector database are to be stored here. It also contains a **file_status.csv** file to keep track of which files are uploaded. On running **data_indexing.py** file, the file_status.csv gets updated.
2. **src** : It contains the **exception.py** file for handling Custom Exceptions and the **logger.py** file which creates log files that helps us track our progress while the project is running and also stores the exceptions occured. The **utils.py** file contains two classes : the first to handle some operations related to the Pinecone index (create, connect, upsert, enquire the number of vectors present) and the second to generate tokens and embedding vectors of text using Huggingface ALBERT model. The **search_query.py** file takes in the user's query from the webpage, converts it to vectors and runs a similiarity search with the vectors stored in the Pinecone index.
          The src folder has a subfolder names components, which stores two files : data_transformation.py which can separate out the paragraphs from pdf, text or word files  and the data_indexing.py file which receives the paragraphs, convert them to vectors and upserts them into the pineclone index.
3. The static folder contains the css file for our frontend page.
4. The templates folder contains the HTML code for our frontend page.
5. The app.py is a Flask app that passes the user's query to the search_query.py file and displays the top_k queries (as asked by the user) on the webpage.
6. The .env file contains informations like the Pinecone API key, Pinecone Environment name, Pinecone Index name and the destination of the project folder in the system.
7. The requirements.txt file contains all the Python modules required in the project.

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

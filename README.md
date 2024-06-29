# FAISSVectorSearch
Flask-based RESTful API that enables efficient and accurate similarity searches for educational course content.
Leveraging FAISS for fast nearest neighbor search and Sentence Transformers for generating text embeddings, this API helps in finding and recommending courses based on similarity.
Installation:
  Clone the repository.
  Install the required packages: pip install -r requirements.txt
  Ensure that the vector store is properly set up by running the "vectorstore.py" file
  Start the Flask API by running the "main.py" file.
Using the API
  To search for similar course content, add "/search/text" to the path of the web page created by the Flask API, replacing text with your query. 
  (eg. http://127.0.0.1:5000/search/Python)

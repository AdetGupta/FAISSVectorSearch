# CourseVectorSearch

CourseVectorSearch is a Flask-based RESTful API that enables efficient and accurate similarity searches for educational course content. Leveraging FAISS for fast nearest neighbor search and Sentence Transformers for generating text embeddings, this API helps in finding and recommending courses based on similarity.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CourseVectorSearch.git
    cd CourseVectorSearch
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that the vector store is properly set up by running the `vectorstore.py` file:
    ```bash
    python vectorstore.py
    ```

4. Start the Flask API by running the `main.py` file:
    ```bash
    python main.py
    ```

## Using the API

To search for similar course content, add `/search/text` to the path of the web page created by the Flask API, replacing `text` with your query.

Example:
```bash
    http://127.0.0.1:5000/search/Python
```

from flask import Flask, jsonify
from vector_store import find_similar_embeddings
app = Flask(__name__)

@app.route('/')
def hello_world():
    temp =  'To search for a particular word in the vector store add "/search/-WORD" to the path.'
    return temp

@app.route('/search/<text>')
def similarity_search(text):
    result = find_similar_embeddings(text)
    return jsonify(result)

app.run(debug=True)
    


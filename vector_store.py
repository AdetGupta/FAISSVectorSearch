from langchain_community.document_loaders import UnstructuredURLLoader
import faiss
from sentence_transformers import SentenceTransformer
import json

urls = ["https://brainlox.com/courses/category/technical"]
loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

# Extract from web-page
def extract_courses(raw_text):
    lines = raw_text.split('\n')
    courses = []
    i = 0
    while i < len(lines):
        course = {}
        if 'per session' in lines[i]:
            course["title"] = lines[i + 2]
            course["description"] = lines[i + 4]
            course["price"] = lines[i - 2]
            course["lessons"] = lines[i + 6]
            courses.append(course)
        i += 1
    return courses

# Creating ebeddings
def create_embeddings(text):
    return model.encode(text)

# Search similar results
def find_similar_embeddings(text, k=67):
    # Perform a nearest neighbor search
    query_embedding = create_embeddings(text)
    distances, indices = faiss_index.search(query_embedding.reshape(1, -1), k)
    results = []
    i = 0
    for dist, idx in zip(distances[0], indices[0]):
        if(dist < 1):
            result = {
                'id': [i],
                'text': texts[idx]
            }
            i += 1
            results.append(result)
    return results


raw_text = data[0].page_content
course_data = extract_courses(raw_text)

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [course['title'] + ", " + course['description'] for course in course_data]
text_embeddings = create_embeddings(texts)

dim = len(text_embeddings[0])  # Dimensionality of the embeddings
faiss_index = faiss.IndexFlatL2(dim)

faiss_index.add(text_embeddings)

# print(find_similar_embeddings("python"))
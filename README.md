# text_similarity_challenge

Implementing text similarity:
- Using cosine similarity to get the similarity between two text documents
- Ignoring punctuations in the input string
- Have removed common english stop words
- No specific ordering has been done to the input strings
- Have implemented the similarity by using cosine similarity between two term-frequency vectors,
  Computing the dot product of the 2 vectors and dividing by the product of the absolute values
  of the vectors
- The data structures used are Python dictionary and python lists

# How to run the code
- The project utilized the Flask API so it can run as a web service
- The project includes a requirements.txt file to install all necessary libraries
- The project can be run on command line by running the app.py file -> "python app.py"

# Resources
- Understanding Cosine Similarity:  https://www.sciencedirect.com/topics/computer-science/cosine-similarity
- Using and implementing the Flask API: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

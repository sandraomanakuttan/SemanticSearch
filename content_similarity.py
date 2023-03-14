# Import the SentenceTransformer class and util module from the sentence_transformers library
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained transformer model named "all-MiniLM-L6-v2"
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Define a function named sentence_similarity that takes two input sentences as strings and returns their similarity score as a percentage


def sentence_similarity(input1, input2):
    # Encode the two input sentences into their vector representations using the pre-trained model
    embedding1 = model.encode(input1.lower(), convert_to_tensor=True)
    embedding2 = model.encode(input2.lower(), convert_to_tensor=True)

    # Calculate the cosine similarity between the two encoded vectors using the util.cos_sim method
    cosine_scores = util.cos_sim(embedding1, embedding2).tolist()[0]

    # Round the similarity score to two decimal places and convert it to a percentage value
    result = round(cosine_scores[0], 2)
    return round(result*100, 2)

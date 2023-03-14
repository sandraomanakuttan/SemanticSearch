from gensim.models import KeyedVectors
from gensim.similarities import WmdSimilarity
import time

start = time.time()

# Load Google News pre-trained word embeddings
model_path = "GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

def word_movers_distance(s1, s2):
    # Example sentences
    try:
        # Preprocess sentences (tokenize and remove stop words)
        s1_tokens = [word for word in s1.lower().split() if word.isalnum()]
        s2_tokens = [word for word in s2.lower().split() if word.isalnum()]

        # Calculate WMD distance
        instance = WmdSimilarity([s1_tokens], model, num_best=1)
        distance = instance[s2_tokens][0][1]

        # Calculate percentage similarity
        max_distance = instance[s1_tokens][0][1]
        similarity = round((distance / max_distance) * 100, 2)
        print(f"Similarity percentage: {similarity:.2f}%")
        return similarity
    except:
        pass

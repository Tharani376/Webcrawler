import json
import re

# load inverted index
with open("inverted_index.json", "r") as f:
    inverted_index = json.load(f)

# load idf values
with open("idf_values.json", "r") as f:
    idf_values = json.load(f)


def tokenize_query(query):
    query = query.lower()
    query = re.sub(r'[^\w\s]', '', query)
    return query.split()


def search(query, top_n=10):

    tokens = tokenize_query(query)

    scores = {}

    for word in tokens:

        if word in inverted_index:

            postings = inverted_index[word]

            for doc_id, tf in postings:

                score = tf * idf_values.get(word, 0)

                if doc_id not in scores:
                    scores[doc_id] = 0

                scores[doc_id] += score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    results = []

    for doc, score in ranked[:top_n]:
        results.append({
            "document": doc,
            "score": round(score, 4)
        })

    return results
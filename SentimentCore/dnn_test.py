import numpy as np
from senti_classifier import senti_classifier

from dnnsent import sentiment

sentence = "Accuracy vs performance as usual"
pos_score, neg_score = senti_classifier.polarity_scores([sentence])
print(pos_score, neg_score)
score_vec = np.array([pos_score, neg_score], dtype=np.float)
vector_norm = score_vec / float(2 * np.linalg.norm(score_vec))
print(vector_norm)
final_score = 0.5 + vector_norm[0] - vector_norm[1]
print(final_score)


final_score = sentiment.sentiment_score(sentence)
print(final_score)
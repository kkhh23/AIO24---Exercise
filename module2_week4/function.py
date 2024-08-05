from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib . pyplot as plt
import pandas as pd
import gdown
import numpy as np


def compute_mean(x: np.ndarray):
    result = np.sum(x)/len(x)
    return result


def compute_median(x: np.ndarray):
    sorted_x = np.sort(x)
    n = len(sorted_x)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_x[mid - 1] + sorted_x[mid]) / 2
    else:
        median = sorted_x[mid]

    return median


x = [1, 5, 4, 4, 9, 13]
print(compute_median(x))


def compute_std(x):
    mean = compute_mean(x)
    N = len(x)
    variance = np.sum((x - mean) ** 2) / N
    return np.sqrt(variance)


def compute_correlation_coefficient(X, Y):
    N = len(X)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sqrt(np.sum((X - mean_X) ** 2)
                          * np.sum((Y - mean_Y) ** 2))
    if denominator == 0:
        return 0

    return numerator / denominator


# url = 'https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'
# output = 'advertising .csv'
# gdown.download(url, output, quiet=False)
data = pd.read_csv('module2_week4/advertising .csv')
# x = data['TV'].to_list()
# y = data['Radio'].to_list()
# corr_xy = compute_correlation_coefficient(X=x, Y=y)
# print(f" Correlation between TV and Sales : {round(corr_xy, 2)}")

# features = ['TV','Radio','Newspaper']

# for feature_1 in features :
#     for feature_2 in features :
#         correlation_value = compute_correlation_coefficient( data [ feature_1 ] , data [ feature_2 ])
#         print ( f" Correlation between { feature_1 } and { feature_2 }: { round (correlation_value , 2)}")

# data = pd.read_csv("advertising.csv")
# x = data ['Radio']
# y = data ['Newspaper']
# np.coefficient(x,y)
# data.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(data.corr(), annot=True, fmt=".2f", linewidth=.5)
# plt . show()

# import gdown
# gdown.download('https://drive.google.com/uc?id=1jhp2DlaWsDo_vEVICrTrNh3mUuXd-cw6', 'module2_week4/vi_text_retrieval.csv', quiet=False)


vi_data_df = pd.read_csv('module2_week4/vi_text_retrieval.csv')
context = vi_data_df['text'].to_list()
context = [doc.lower() for doc in context]
# context


tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
round(context_embedded.toarray()[7][0], 2)


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(
        context_embedded, query_embedded).reshape((-1,))
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc)
    return results


question = vi_data_df.iloc[0]['question']
print("Question: ", question)
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
results[0]['cosine_score']


def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_scores = np.corrcoef(
        query_embedded.toarray()[0],
        context_embedded.toarray()
    )
    corr_scores = corr_scores[0][1:]
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results


question = vi_data_df . iloc[0][’question ’]
results = corr_search(question, tfidf_vectorizer, top_d=5)
results[1]['corr_score']

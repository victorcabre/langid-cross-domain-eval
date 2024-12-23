from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

from my_utils import read_data, save_model, identity


data = "all.train"

train_path = f"../data/{data}"
txts_train, golds_train = read_data(train_path)

count_vectorizer = CountVectorizer(ngram_range=(1,4), preprocessor=identity, analyzer="char", max_features=10000)
x_train = count_vectorizer.fit_transform(txts_train)

mnb = MultinomialNB()
mnb.fit(x_train, golds_train)

print(mnb.get_params())
save_model(mnb, f"models/{data}")
save_model(count_vectorizer, f"vectorizers/{data}")


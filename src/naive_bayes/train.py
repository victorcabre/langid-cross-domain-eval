from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

from my_utils import read_data, save_model, identity


source_domains = ["wiki", "news", "religious", "combined"]
seed_number = 0

for source_domain in source_domains:
    train_path = f"langid4/data/domain.{seed_number}.{source_domain}.train"
    txts_train, golds_train = read_data(train_path)

    count_vectorizer = CountVectorizer(ngram_range=(1,4), preprocessor=identity, analyzer="char")
    x_train = count_vectorizer.fit_transform(txts_train)

    mnb = MultinomialNB()
    mnb.fit(x_train, golds_train)

    print(mnb.get_params())
    save_model(mnb, f"models/naive_bayes/{source_domain}")
    save_model(count_vectorizer, f"models/naive_bayes/vectorizers/{source_domain}")
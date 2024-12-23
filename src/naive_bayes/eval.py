from sklearn.metrics import accuracy_score

from my_utils import read_data, load_model, identity

source_domains = ["wiki", "news", "religious", "combined"]
test_domains = ["wiki", "news", "religious", "rights", "social"]
seed_number = 0
scores = []

for source_domain in source_domains:
    model = load_model(f"models/naive_bayes/{source_domain}")
    vectorizer = load_model(f"models/naive_bayes/vectorizers/{source_domain}")
    for test_domain in test_domains:
        dev_path = f"langid4/data/domain.{seed_number}.{test_domain}.dev"
        txts_dev, golds_dev = read_data(dev_path)
        x_dev = vectorizer.transform(txts_dev)

        y_pred = model.predict(x_dev)
        accuracy = accuracy_score(golds_dev, y_pred)
        scores.append(accuracy)
        print((f"{source_domain} / {test_domain}: {accuracy}"))

print(scores)
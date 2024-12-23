from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from my_utils import read_data, save_model, identity
import numpy as np
from scipy.sparse import vstack


def batch_vectorize(texts, vectorizer, batch_size=1000):
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        yield vectorizer.transform(batch)


def train_in_batches(train_path, batch_size=1000):
    count_vectorizer = CountVectorizer(
        ngram_range=(1,4),
        preprocessor=identity,
        analyzer="char",
        max_features=100000
    )
    mnb = MultinomialNB()

    # Fit vectorizer
    txts_first_batch, _ = read_data(train_path, limit=batch_size)
    count_vectorizer.fit(txts_first_batch)
    del txts_first_batch
    gc.collect()

    # Incremental training
    first_batch = True
    
    def process_batch(start_idx, batch_size):
        txts_batch, golds_batch = read_data(
            train_path, 
            skip=start_idx, 
            limit=batch_size
        )
        if not txts_batch:
            return None, None
        x_batch = count_vectorizer.transform(txts_batch)
        return x_batch, golds_batch

    # First batch
    x_batch, golds_batch = process_batch(0, batch_size)
    if x_batch is not None:
        mnb.partial_fit(x_batch, golds_batch, classes=np.unique(golds_batch))
    
    # Remaining batches
    start_idx = batch_size
    while True:
        x_batch, golds_batch = process_batch(start_idx, batch_size)
        if x_batch is None:
            break
            
        mnb.partial_fit(x_batch, golds_batch)
        
        print(f"Processed batch starting at index {start_idx}")
        start_idx += batch_size

    return mnb, count_vectorizer


# Train models
data = "cut2.train"
train_path = f"../data/{data}"
mnb, count_vectorizer = train_in_batches(train_path)

# Save models
print("Saving models...")
save_model(mnb, f"models/{data}")
save_model(count_vectorizer, f"vectorizers/{data}")
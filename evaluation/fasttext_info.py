import fasttext

model = fasttext.load_model('fastText.out.bin')

vocab_size = len(model.get_words())
embedding_dim = model.get_dimension()
num_parameters = vocab_size * embedding_dim

print(num_parameters)




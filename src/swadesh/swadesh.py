from pathlib import Path
import Levenshtein

class Swadesh:
    def __init__(self, path) -> None:
        self.path = Path(path)


    def read_swadesh(self, lang):
        # Read the Swadesh list for a given language
        english = []
        translation = []

        for line in open(self.path / f"{lang}.txt"):
            line = line.split(':')
            eng = line[0]
            trans = line[1].split('\t')[0].split('|')[0].strip()

            english.append(eng)
            translation.append(trans)

        return english, translation


    def get_common_words(self, eng1, trans1, eng2, trans2):
        # Compute the set of common words in both languages
        common_eng = set(eng1) & set(eng2)

        dict1 = {k: v for k, v in zip(eng1, trans1) if k in common_eng}
        dict2 = {k: v for k, v in zip(eng2, trans2) if k in common_eng}

        common_words_1 = [dict1[k] for k in common_eng]
        common_words_2 = [dict2[k] for k in common_eng]
        
        return common_words_1, common_words_2
    

    def get_similarity(self, lang1: str, lang2: str):
        # Returns the mean similarity between the two languages
        eng1, trans1 = self.read_swadesh(lang1)
        eng2, trans2 = self.read_swadesh(lang2)

        lang1_words, lang2_words = self.get_common_words(eng1, trans1, eng2, trans2)

        similarities = [Levenshtein.ratio(w1, w2) for w1, w2 in zip(lang1_words, lang2_words)]
        mean_similarity = sum(similarities) / len(similarities)
        return mean_similarity

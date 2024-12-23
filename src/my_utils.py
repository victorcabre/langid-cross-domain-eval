import joblib
import subprocess
import sys
import os

def identity(x):
    return x


def read_data(path: str):
    """
    Takes as input a path to a conll-like file, with the label in the first 
    column, and the text in the second. It returns a list of all input texts
    and a separate list with all gold labels.
    """
    txts = []
    golds = []
    for line in open(path):
        tok = line.strip().split('\t')
        txts.append(tok[1])
        golds.append(tok[0])
    return txts, golds


def save_model(model, filename: str):
    """
    Saves a sklearn model to disk.
    """
    joblib.dump(model, filename)


def load_model(filename: str):
    return joblib.load(filename)


def clean_language_name(name: str):
    return name.replace("__label__", "")


def get_lang_dists(lang1: str, lang2: str):
    original_wd = os.getcwd()
    project_dir = "/home/victor/Documents/ITU/Thesis/langid4/lang_dist/"
    sys.path.append(project_dir)
    os.chdir(project_dir)
    from scripts.get_dist import getDists
    dists = getDists(lang1, lang2)
    os.chdir(original_wd)
    return dists


print(get_lang_dists("gle", "eng"))
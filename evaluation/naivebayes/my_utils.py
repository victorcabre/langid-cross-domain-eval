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




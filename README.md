# In-depth evaluation of cross-domain language identification methods

This is the repository for the programs and scripts used in the "In-depth evaluation of cross-domain language identification methods" research project.

The research paper can be found [here](https://raw.githubusercontent.com/victorcabre/langid-cross-domain-eval/main/paper.pdf). The GEP document (project planning and execution document) can be found [here](https://raw.githubusercontent.com/victorcabre/langid-cross-domain-eval/main/gep.pdf).

## Folder structure and file information

The repository is structured as follows:

- `notebooks`: Contains Jupyter notebooks for several experiments.
    - `errors.ipynb`: In-depth analysis of errors produced by the Naïve Bayes method, with cells for manual inspection (requires Data Wrangler extension in Visual Studio Code in order, otherwise the code can be changed to display more rows). This notebook also contains some figures from the paper.
    - `figures.ipynb`: Code to generate some of the figures used in the paper, as well as a figure shown in the GEP document.
    - `naiveBayesAgnostic.ipynb`: Two different approaches to create a domain agnostic model from the models trained on each domain. The two approaches are cross-domain feature selection and feature weight aggregation.
    - `naiveBayesImplementation.ipynb`: The original implementation of our custom Naïve Bayes model. Similar code can be found in `src/naive_bayes`.
    - `swadesh.ipynb`: The original implementation (and some testing) of the Swadesh distance computation script. Similar code can be found in `src/swadesh`.
- `src`: Contains executable scripts for the training and evaluation of our Naïve Bayes-based method and our own implementation of the Swadesh distance.
- `evaluation`: Contains scripts for the evaluation of the three LangID methods used in the paper. The scripts are prepared to be run using the SLURM scheduler in ITU's High Performance Computer. In order to run some of the scripts, you need to clone the dependencies into the same folder (namely, FastText and `langid.py`). The folder containing the data should be present in this directory.
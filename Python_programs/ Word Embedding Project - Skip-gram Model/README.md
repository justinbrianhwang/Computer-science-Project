# Word Embedding Project - Skip-gram Model

This project is a part of the natural language processing (NLP) assignment focused on training word embeddings using a Skip-gram model. The project allows finding similar words based on cosine similarity and was developed in Python using PyTorch. The corpus consists of multiple text files, which are processed to build a vocabulary, generate training data, and create vector embeddings for words.

## Project Overview

- **Language**: Python
- **Framework**: PyTorch
- **Model**: Skip-gram with negative sampling
- **Corpus**: Multiple text files located in the `./dataset/` directory
- **Training Data**: Word pairs with positive and negative examples

## Key Features

- **Vocabulary Creation**: A custom vocabulary is built from the corpus, filtering out words based on frequency thresholds.
- **Training with Negative Sampling**: The Skip-gram model uses context words around a target word and negative sampling to efficiently train word embeddings.
- **Similarity Search**: After training, the model finds the top `k` most similar words to a given word using cosine similarity or Euclidean distance.
- **Model Saving and Loading**: The model can be saved and resumed for further training across file batches.

## Requirements

- Python 3.6+
- PyTorch
- pandas
- numpy





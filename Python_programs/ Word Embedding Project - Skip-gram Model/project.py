## 자연어처리 프로젝트 과제 1번
# 구글 코랩이 적용이 잘 안되어, pycharm 환경에서 코드를 새롭게 짰습니다.

# 필요한 라이브러리 import
import os
import time
import numpy as np
import random
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from collections import defaultdict
import pandas as pd

# 이 기기가 GPU를 사용할 수 있는지 확인 하는 코드이다.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("device = ", device)

cur_dir_path = './dataset'
dir_list = os.listdir(cur_dir_path)
# p(dir_list) # 정상적으로 잘 불러옴을 확인했습니다.

# 단어 정제 함수
def cleaning_word(oword):
    cleaned_oword = oword.replace(",", "").replace("$", "").replace(".", "")
    if cleaned_oword.isnumeric():
        return '<NO>'
    word = cleaned_oword
    word_leng = len(word)
    if word_leng == 0:
        return '<NO>'
    i = 0
    if word_leng > 1 and not word[0].isalpha():
        i = 1
        if word_leng > 2 and not word[1].isalpha():
            i = 2
    j = word_leng - 1
    if j >= i and not word[j].isalpha():
        j -= 1
        if j >= i and j > 0 and not word[j].isalpha():
            j -= 1
    if j < i:
        return '<NO>'
    word = word[i:j+1]
    if len(word) == 0:
        return '<NO>'
    if word.isalpha():
        return word
    else:
        return '<NO>'

# (1)문장의 단어를 읽어, 사전을 만들자

# csv 처리
vocab_file_path = './vocab.csv'
# 임계값 설정
frequency_threshold = 30 # 이는 유동적으로 설정하시면 좋을 듯 합니다.

# 1. 파일에서 문장 읽기 및 단어 빈도수 계산
def build_vocab_from_files(file_list, cleaning_func, threshold=1):
    word_freq = defaultdict(int)  # 단어 빈도 저장

    for file_name in file_list:
        print(f"Processing file: {file_name}")  # 파일 이름 출력
        try:
            with open(file_name, 'r', encoding='utf-8') as fp:
                for line in fp:
                    print(f"Raw line: {line.strip()}")  # 원래 줄을 출력
                    words = line.split()  # 공백을 기준으로 단어 분리
                    for word in words:
                        cleaned_word = cleaning_func(word)
                        print(f"Original word: {word}, Cleaned word: {cleaned_word}")  # 정제된 단어 확인
                        if cleaned_word != '<NO>':
                            word_freq[cleaned_word] += 1  # 단어 빈도수 추가
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")

    # 2. 빈도수 기준으로 단어 정렬
    sorted_vocab = sorted(word_freq.items(), key=lambda kv: kv[1])
    print(f"Sorted vocab size: {len(sorted_vocab)}")

    # 3. 임계값을 넘는 단어만 사전에 추가
    vocab = {}
    total_n_words = len(sorted_vocab)
    for i in range(total_n_words):
        word = sorted_vocab[i][0]
        freq = sorted_vocab[i][1]
        print(f"Word: {word}, Frequency: {freq}")

        if freq >= threshold:  # threshold가 0이라면 모든 단어가 추가될 것임
            vocab[word] = [i, freq]  # 정순으로 인덱스를 추가
            print(f"Added word '{word}' with index {i} and frequency {freq}")

    return vocab

# 2. 사전 파일로 저장 (pandas 사용)
def save_vocab(vocab, file_path):
    vocab_data = [{'Word': word, 'Index': idx, 'Frequency': freq} for word, (idx, freq) in vocab.items()]
    df = pd.DataFrame(vocab_data)  # pandas DataFrame으로 변환
    df.to_csv(file_path, index=False, encoding='utf-8')  # CSV 파일로 저장
    print(f"Vocabulary saved to {file_path}")

# 3. 사전 파일에서 불러오기 (pandas 사용)
def load_vocab(file_path):
    vocab = {}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            word = row['Word']
            idx = row['Index']
            freq = row['Frequency']
            vocab[word] = [int(idx), int(freq)]
    return vocab

# 4. 사전 생성 또는 불러오기
def get_or_create_vocab(file_list, vocab_file, cleaning_func, threshold):
    # vocab.csv 파일이 존재하면 로드
    if os.path.exists(vocab_file):
        print(f"Loading vocab from {vocab_file}")
        vocab = load_vocab(vocab_file)
    else:
        print(f"Building vocab from files")
        word_freq = defaultdict(int)  # 단어 빈도 저장

        # 파일들을 읽어서 사전 생성
        for file_name in file_list:
            print(f"Processing file: {file_name}")
            try:
                with open(file_name, 'r', encoding='utf-8') as fp:
                    for line in fp:
                        print(f"Line from file: {line.strip()}")  # 파일에서 읽은 내용을 출력
                        words = line.split()  # 공백을 기준으로 단어 분리
                        for word in words:
                            cleaned_word = cleaning_func(word)
                            if cleaned_word != '<NO>':
                                word_freq[cleaned_word] += 1  # 단어 빈도수 추가
                            else:
                                print(f"Excluding word: {word} (cleaned: {cleaned_word})")  # <NO> 단어 제외
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")

        # 빈도수 확인
        if len(word_freq) == 0:
            print("No words were added to the vocabulary.")

        # 2. 빈도수 기준으로 단어 정렬
        sorted_vocab = sorted(word_freq.items(), key=lambda kv: kv[1])
        print(f"Sorted vocab size: {len(sorted_vocab)}")

        # 3. 임계값을 넘는 단어만 사전에 추가
        vocab = {}
        total_n_words = len(sorted_vocab)
        for i in range(total_n_words - 1, -1, -1):
            word = sorted_vocab[i][0]
            freq = sorted_vocab[i][1]
            if freq >= threshold:
                vocab[word] = [total_n_words - 1 - i, freq]
            else:
                break

        # 생성된 사전을 파일로 저장
        save_vocab(vocab, vocab_file)

    return vocab

# 실행 예시
cur_dir_path = './dataset'
dir_list = [os.path.join(cur_dir_path, file_name) for file_name in os.listdir(cur_dir_path)]

# 사전 생성 또는 불러오기
vocab = get_or_create_vocab(dir_list, vocab_file_path, cleaning_word, frequency_threshold)

# 결과 확인
print(f"Vocabulary size: {len(vocab)}")
print(f"Sample words from vocab: {list(vocab.items())[:10]}")
vocab_size = len(vocab)

def read_sentences_from_files(file_list, cleaning_func):
    sentences = []

    for file_name in file_list:
        print(f"Reading file: {file_name}")
        try:
            with open(file_name, 'r', encoding='utf-8') as fp:
                for line in fp:
                    words = line.split()  # 문장을 단어로 분리
                    cleaned_words = [cleaning_func(word) for word in words if cleaning_func(word) != '<NO>']
                    if cleaned_words:  # 유효한 단어가 있으면 추가
                        sentences.append(cleaned_words)
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")

    return sentences


# 예시: 파일에서 문장을 읽어와서 sentences 변수에 저장
sentences = read_sentences_from_files(dir_list, cleaning_word)



# (2) 훈련 데이터 만드는 과정
def prepare_training_data(sentences, vocab, vocab_size, window_size=2, negative_sample_rate=0.1):
    """
    sentences: 단어 list 목록
    vocab: 단어를 키로, ID를 값으로 사용하는 사전
    vocab_size: 어휘의 총 단어 수(알 수 없는 단어 및 더미 단어에 사용됨)
    window_size: 컨텍스트 창의 크기
    negative_sample_rate: negative 예시를 샘플링할 확률
    """
    training_data = []

    for sentence in sentences:
        # 각 문장을 단어 ID 리스트로 변환
        word_ids = [vocab.get(word, vocab_size) for word in sentence]

        # 문장 양 끝에 dummy word인 vocab_size ID 추가
        word_ids = [vocab_size] * window_size + word_ids + [vocab_size] * window_size

        # center word를 기준으로 window에서 context word와 target label을 생성
        for i in range(window_size, len(word_ids) - window_size):
            center_word_id = word_ids[i]  # center word는 단일 값이어야 함

            # center word가 dummy word라면 무시
            if center_word_id == vocab_size:
                continue

            # context word 선택 (각 context를 개별적으로 처리)
            context_ids = word_ids[i - window_size:i] + word_ids[i + 1:i + 1 + window_size]

            # context가 dummy word라면 무시
            for context_word_id in context_ids:
                if context_word_id == vocab_size:
                    continue

                # Positive example (target label 1)
                training_data.append([center_word_id, context_word_id, 1])

                # Negative sampling (target label 0)
                if random.random() < negative_sample_rate:
                    negative_word_id = random.randint(0, vocab_size - 1)
                    training_data.append([center_word_id, negative_word_id, 0])

    return training_data



# (3) 훈련데이터 텐서화
def tensorize_data(training_data):
    """
    training_data: list of training examples in the format [center_word_id, context_word_id, target_label]

    Returns:
    train_X: Tensor with shape (num_examples, 2)
    train_Y: Tensor with shape (num_examples, 1)
    """
    # 이중 리스트가 있을 경우 첫 번째 값만 선택하여 평탄화 (flatten)
    train_X = torch.tensor(
        [[example[0][0] if isinstance(example[0], list) else example[0],
          example[1][0] if isinstance(example[1], list) else example[1]]
         for example in training_data], dtype=torch.long)

    train_Y = torch.tensor([[example[2]] for example in training_data], dtype=torch.float)

    return train_X, train_Y


# 만든 함수로 먼저, 데이터 텐서화까지 시키기
# 1. 훈련 데이터를 생성 (Python 리스트 형태로)
training_data = prepare_training_data(sentences, vocab, vocab_size, window_size=2, negative_sample_rate=0.1)

# 생성된 데이터 확인 -> 오류 검출을 위해..
print(f"Training data sample: {training_data[:5]}")


# 2. 훈련 데이터를 텐서화 (train_X와 train_Y로 변환)
train_X, train_Y = tensorize_data(training_data)

BATCH_SIZE = 32
data = TensorDataset(train_X, train_Y)
dataloader = DataLoader(data, sampler=RandomSampler(data), batch_size=BATCH_SIZE, drop_last=True)

# 배치 수 확인
num_batches = len(dataloader)
print(f"Number of batches: {num_batches}")

## model 정의 : 이것은 여러 가지 방식으로 할 수 있다. 다음은 한 가지 예로서 class를 이용하여 정의한 것이다.
class dotModel(nn.Module):
    def __init__(self, vocab_size, d_emb):
        super(dotModel, self).__init__()
        self.embedding1 = nn.Embedding(vocab_size, d_emb)
        self.embedding2 = nn.Embedding(vocab_size, d_emb)
        self.logistic = nn.Sigmoid()

    def forward(self, X):
        wc = X[:,0]
        wo = X[:,1]
        center_word_vector = self.embedding1(wc)
        context_word_vector = self.embedding2(wo)

        s = torch.einsum('ij,ij->i', center_word_vector, context_word_vector)
        y = self.logistic(s)
        return y

"""
[검색한 내용입니다.]
작은 값 (e.g., 50): 계산이 빠르고 메모리 효율적이지만, 단어 간의 복잡한 관계를 충분히 포착하지 못할 수 있습니다.
큰 값 (e.g., 300): 더 복잡한 패턴을 학습할 수 있지만, 계산 비용이 증가하고, 오버피팅의 위험이 있을 수 있습니다.
"""

d_emb = 50
# 모델 객체 변수 model 선언
model = dotModel(vocab_size, d_emb)
model = model.to(device)

# (7) optimizer 및 loss 함수 준비
optimizer = optim.AdamW(model.parameters(), lr=0.9e-5)
criterion = nn.BCELoss()

#------------------------------------------------------------------------------------------------------------------

# 훈련 수행 부
'''
각 input batch를 모델에 적용하고, 그 결과와 target 정보를 이용하여 loss를 구하기 
그리고 backward pass를 수행하고, parameters update를 수행한다. 

num_epochs: 훈련 루프에서 모델이 전체 데이터셋을 몇 번 반복 학습할지를 결정하는 변수
'''

num_epochs = 3
for i in range(num_epochs):
    total_loss = 0.0
    model.train()
    for j, batch in enumerate(dataloader):
        batch = tuple(t.to(device) for t in batch)
        b_train_X, b_train_Y = batch
        optimizer.zero_grad()
        model.zero_grad()
        pred = model(b_train_X)
        pred = torch.reshape(pred, (BATCH_SIZE, 1))
        b_train_Y = b_train_Y.float()

        # 배치 내의 모든 예제에 대하여 loss를 계산하여 배치 내의 예제당 loss 평균을 구해 돌려줌
        loss = criterion(pred, b_train_Y)

        total_loss += loss.item()

        loss.backward()
        optimizer.step()

        if j % 2000 == 0:
            print("number of batches done = ", j)

    avg_loss_per_batch = total_loss / num_batches
    print("epoch = ", i, " has finished.", " average loss per example = ", avg_loss_per_batch)

#-----------------------------------------------------------------------------------------------
# (8) 훈련 작업 진행
# 모델을 저장하는 함수
def save_model(model, optimizer, epoch, path):
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }, path)
    print(f"Model saved at epoch {epoch}")


# 모델을 로드하는 함수
def load_model(model, optimizer, path):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    print(f"Model loaded from epoch {epoch}")
    return epoch


# 파일들을 50개씩 묶기 위한 함수
def batch_files(file_list, batch_size):
    for i in range(0, len(file_list), batch_size):
        yield file_list[i:i + batch_size]


# 예시 실행
file_batches = list(batch_files(dir_list, 50))
model_path = './model_checkpoint.pt'

# 기존 모델이 있는 경우 로드, 없으면 처음부터 시작
start_epoch = 0
if os.path.exists(model_path):
    start_epoch = load_model(model, optimizer, model_path)

# 각 파일 배치에 대해 모델 훈련
for batch_idx, file_batch in enumerate(file_batches):
    print(f"Processing file batch {batch_idx + 1}/{len(file_batches)}")

    # 문장 읽기 및 훈련 데이터 준비
    sentences = read_sentences_from_files(file_batch, cleaning_word)
    training_data = prepare_training_data(sentences, vocab, vocab_size, window_size=2, negative_sample_rate=0.1)
    train_X, train_Y = tensorize_data(training_data)

    # DataLoader 설정
    data = TensorDataset(train_X, train_Y)
    dataloader = DataLoader(data, sampler=RandomSampler(data), batch_size=BATCH_SIZE, drop_last=True)
    num_batches = len(dataloader)

    # 모델 훈련 루프
    num_epochs = 3
    for i in range(start_epoch, num_epochs):
        total_loss = 0.0
        model.train()

        for j, batch in enumerate(dataloader):
            batch = tuple(t.to(device) for t in batch)
            b_train_X, b_train_Y = batch
            optimizer.zero_grad()
            model.zero_grad()
            pred = model(b_train_X)
            pred = torch.reshape(pred, (BATCH_SIZE, 1))
            b_train_Y = b_train_Y.float()

            # loss 계산
            loss = criterion(pred, b_train_Y)
            total_loss += loss.item()

            loss.backward()
            optimizer.step()

            if j % 2000 == 0:
                print("number of batches done = ", j)

        avg_loss_per_batch = total_loss / num_batches
        print(f"epoch = {i} has finished. average loss per batch = {avg_loss_per_batch}")

        # 모델 저장
        save_model(model, optimizer, i, model_path)

# (9) 훈련 충분..
# 코사인 유사도 계산 함수
def cosine_similarity(vec1, vec2):
    return F.cosine_similarity(vec1, vec2, dim=0)

# 유클리드 거리 계산 함수
def euclidean_distance(vec1, vec2):
    return torch.dist(vec1, vec2)

# 모든 단어와 유사도 계산
def find_similar_words(word, model, vocab, top_k=5, similarity_metric="cosine"):
    word_id = vocab[word][0]  # 단어의 ID 가져오기
    word_vec = model.embedding1(torch.tensor([word_id], device=device)).squeeze(0)  # 해당 단어의 임베딩 벡터

    similarities = []

    for other_word, (other_word_id, _) in vocab.items():
        if other_word == word:
            continue

        other_word_vec = model.embedding1(torch.tensor([other_word_id], device=device)).squeeze(0)

        if similarity_metric == "cosine":
            similarity = cosine_similarity(word_vec, other_word_vec).item()
        elif similarity_metric == "euclidean":
            similarity = -euclidean_distance(word_vec, other_word_vec).item()  # 거리가 짧을수록 유사하므로 음수로 변환

        similarities.append((other_word, similarity))

    # 유사도 기준으로 정렬 (가장 가까운 top_k 개 단어 선택)
    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities[:top_k]

# # 테스트할 단어와 유사한 단어 찾기 (예: "apple")
# similar_words = find_similar_words("apple", model, vocab, top_k=5, similarity_metric="cosine")
#
# print("Top 5 similar words to 'apple':")
# for word, similarity in similar_words:
#     print(f"{word}: {similarity:.4f}")

# 이제 원하는 문자를 입력 받아, 출력하도록
w = input("Enter word: ")
similar_words = find_similar_words(w, model, vocab, top_k=5, similarity_metric="cosine")

print(f"Top 5 similar words to {w}:")
for word, similarity in similar_words:
    print(f"{word}: {similarity:.4f}")





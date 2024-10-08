## 과제 2: Korean Entity Recognition 모델 개발 실험

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from eojeol_etri_tokenizer.eojeol_tokenization import eojeol_BertTokenizer
import numpy as np

# 토크나이저 설정
eojeol_tokenizer = eojeol_BertTokenizer("./ner_eojeol_label_per_line.txt", do_lower_case=False)

# 어휘 사전 및 레이블 생성 함수
def build_vocab_and_labels(tokenizer, file_path):
    vocab = set()
    labels = set()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0:
                split_line = line.split()
                if len(split_line) > 1:
                    eoj_tk = tokenizer.tokenize(split_line[0])  # 토큰화
                    label = split_line[1]  # 레이블
                    vocab.update(eoj_tk)
                    labels.add(label)

    vocab = {word: idx for idx, word in enumerate(vocab, start=1)}
    labels = {label: idx for idx, label in enumerate(labels)}
    vocab["[PAD]"] = 0
    return vocab, labels

# 어휘 사전과 레이블 생성
vocab, labels = build_vocab_and_labels(eojeol_tokenizer, "./ner_eojeol_label_per_line.txt")
vocab_size = len(vocab)
num_labels = len(labels)

# 데이터 로딩 및 전처리
def load_data(file_path, tokenizer, vocab, labels):
    sentences = []
    label_sequences = []

    with open(file_path, "r", encoding="utf-8") as f:
        sentence_tokens = []
        sentence_labels = []

        for line in f:
            if len(line.strip()) > 0:
                split_line = line.split()
                if len(split_line) > 1:
                    eoj_tk = tokenizer.tokenize(split_line[0])
                    eoj_tkid = [vocab.get(token, 0) for token in eoj_tk]
                    sentence_tokens.extend(eoj_tkid)

                    label = split_line[1]
                    label_id = labels.get(label, 0)
                    sentence_labels.append(label_id)

            if len(line.strip()) == 0 and sentence_tokens:
                sentences.append(sentence_tokens)
                label_sequences.append(sentence_labels)
                sentence_tokens = []
                sentence_labels = []
    return sentences, label_sequences

# 데이터 로드
sentences, label_sequences = load_data("./ner_eojeol_label_per_line.txt", eojeol_tokenizer, vocab, labels)

# 패딩 함수
def pad_sequences(sequences, max_len):
    padded_sequences = []
    for seq in sequences:
        if len(seq) < max_len:
            padded_sequences.append(seq + [0] * (max_len - len(seq)))
        else:
            padded_sequences.append(seq[:max_len])
    return padded_sequences

# 시퀀스 길이 설정 및 패딩 처리
max_len = 128
padded_sentences = pad_sequences(sentences, max_len)
padded_labels = pad_sequences(label_sequences, max_len)

# 텐서로 변환 및 데이터 분리
X_train, X_test, Y_train, Y_test = train_test_split(padded_sentences, padded_labels, test_size=0.2, random_state=42)
X_train = torch.tensor(X_train, dtype=torch.long)
Y_train = torch.tensor(Y_train, dtype=torch.long)
X_test = torch.tensor(X_test, dtype=torch.long)
Y_test = torch.tensor(Y_test, dtype=torch.long)

train_dataset = TensorDataset(X_train, Y_train)
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)  # 배치 크기를 32에서 16으로 줄였습니다.

test_dataset = TensorDataset(X_test, Y_test)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

# RNN 모델 정의
class RNNModel(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_labels):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size, padding_idx=0)
        self.rnn = nn.RNN(hidden_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(p=0.3)  # 드롭아웃 추가
        self.fc = nn.Linear(hidden_size, num_labels)

    def forward(self, x):
        x = self.embedding(x)
        rnn_out, _ = self.rnn(x)
        rnn_out = self.dropout(rnn_out)  # 드롭아웃 적용
        out = self.fc(rnn_out)
        return out

# LSTM 모델 정의
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_labels):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size, padding_idx=0)
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(p=0.3)  # 드롭아웃 추가
        self.fc = nn.Linear(hidden_size, num_labels)

    def forward(self, x):
        x = self.embedding(x)
        lstm_out, _ = self.lstm(x)
        lstm_out = self.dropout(lstm_out)  # 드롭아웃 적용
        out = self.fc(lstm_out)
        return out

# 성능 평가 및 토큰별 예측 레이블 출력 함수
def evaluate_model(model, data_loader, y_test, vocab, labels):
    model.eval()
    predictions = []
    y_true = []  # 실제 레이블 저장

    with torch.no_grad():
        for batch in data_loader:
            inputs, label_batch = batch
            outputs = model(inputs)
            _, predicted_labels = torch.max(outputs, dim=-1)

            predictions.extend(predicted_labels.tolist())
            y_true.extend(label_batch.tolist())  # 실제 레이블 저장

    # 레이블 인덱스를 레이블로 변환하는 딕셔너리
    idx_to_label = {idx: label for label, idx in labels.items()}
    idx_to_vocab = {idx: token for token, idx in vocab.items()}

    # 입력 문장과 예측 레이블 출력
    for i, sentence in enumerate(inputs):
        print("입력 토큰: ", [idx_to_vocab[token.item()] for token in sentence if token.item() in idx_to_vocab])
        print("예측 레이블: ", [idx_to_label[label] for label in predictions[i] if label in idx_to_label])
        print("실제 레이블: ", [idx_to_label[label] for label in y_true[i] if label in idx_to_label])
        print('-' * 50)

    # classification_report 호출
    y_true_flat = [label for seq in y_true for label in seq]
    predictions_flat = [label for seq in predictions for label in seq]
    print(classification_report(y_true_flat, predictions_flat))

# RNN 및 LSTM 모델 학습 및 평가
def train_and_evaluate_model(model, train_loader, test_loader, num_labels, vocab, labels, num_epochs=5):
    optimizer = optim.AdamW(model.parameters(), lr=5e-5)  # 학습률을 1e-4에서 5e-5로 낮췄습니다.
    criterion = nn.CrossEntropyLoss(ignore_index=0)

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for batch in train_loader:
            inputs, label_batch = batch
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs.view(-1, num_labels), label_batch.view(-1))
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {running_loss/len(train_loader)}")

    evaluate_model(model, test_loader, Y_test, vocab, labels)

# RNN 모델 학습 및 평가
rnn_model = RNNModel(vocab_size, hidden_size=512, num_labels=num_labels)
print("RNN 모델 학습 및 평가")
train_and_evaluate_model(rnn_model, train_loader, test_loader, num_labels, vocab, labels)

# LSTM 모델 학습 및 평가
lstm_model = LSTMModel(vocab_size, hidden_size=512, num_labels=num_labels)
print("LSTM 모델 학습 및 평가")
train_and_evaluate_model(lstm_model, train_loader, test_loader, num_labels, vocab, labels)

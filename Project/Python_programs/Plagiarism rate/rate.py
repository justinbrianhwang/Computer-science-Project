import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(file1, file2):
    # 파일에서 텍스트 읽기
    text1 = read_file(file1)
    text2 = read_file(file2)

    # TF-IDF 벡터라이저 생성
    vectorizer = TfidfVectorizer()

    # 텍스트를 TF-IDF 벡터로 변환
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # 코사인 유사도 계산
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return cosine_sim[0][0] * 100  # 유사도를 퍼센트로 반환

# 파일 경로 설정
file1 = 'example1.py'   # C, Java, Python 파일 가능
file2 = 'example2.py'   # C, Java, Python 파일 가능

# 유사도 계산
similarity_percentage = calculate_similarity(file1, file2)
print(f"유사도: {similarity_percentage:.2f}%")

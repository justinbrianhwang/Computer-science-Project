import os
import requests
from bs4 import BeautifulSoup

# 1. 파일 입출력 기능
def load_keywords_with_counts(file_path):
    keywords = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                keyword, count = line.strip().split(',')
                keywords[keyword] = int(count)
    return keywords

def save_keywords_with_counts(file_path, keywords):
    with open(file_path, 'w') as file:
        for keyword, count in keywords.items():
            file.write(f"{keyword},{count}\n")

def increment_keyword_count(keywords, keyword):
    if keyword in keywords:
        keywords[keyword] += 1
    else:
        keywords[keyword] = 1

# 2. 웹 크롤링 기능 (구글 검색 결과에서 추천 검색어와 입력 단어가 포함된 문장 추출)
def crawl_related_keywords_and_sentences(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    related_keywords = set()
    related_sentences = set()

    for page in range(2):  # 첫 두 페이지를 크롤링
        url = f"https://www.google.com/search?q={keyword}&start={page * 10}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 추천 검색어 추출
        for item in soup.select('div.BVG0Nb a, div.Ww4FFb a'):
            related_keyword = item.get_text()
            if related_keyword and "검색결과" not in related_keyword and "광고" not in related_keyword and "namu" not in related_keyword and related_keyword not in related_keywords:
                related_keywords.add(related_keyword)

        # 입력 단어가 포함된 문장 추출
        for text in soup.stripped_strings:
            if keyword in text and "광고" not in text and "wiki" not in text and "Google" not in text and "위키" not in text and "나무" not in text and "namu" not in text and text not in related_sentences:
                related_sentences.add(text)

    return list(related_keywords), list(related_sentences)

# 3. 특정 키워드가 포함된 단어 필터링 기능
def filter_words_with_keyword(words, keyword):
    filtered_words = set()
    for word in words:
        if keyword in word:
            filtered_words.add(word)
    return filtered_words

# 4. 메인 프로그램
def main():
    file_path = 'keywords.txt'

    # 1. 이전에 입력된 단어들을 불러오기
    keywords_with_counts = load_keywords_with_counts(file_path)

    while True:
        user_input = input("Enter a keyword (type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            break

        # 2. 사용자 입력 단어 카운트 증가
        increment_keyword_count(keywords_with_counts, user_input)

        # 3. 웹 크롤링으로 추천 검색어 및 입력 단어가 포함된 문장 수집
        related_keywords, related_sentences = crawl_related_keywords_and_sentences(user_input)

        # 4. 결과 출력
        if keywords_with_counts[user_input] >= 5:
            print(f"\nThe keyword '{user_input}' has been entered {keywords_with_counts[user_input]} times and is prioritized.")
        
        print("\nRelated keywords from the web:")
        for kw in related_keywords:
            print(kw)

        print("\nSentences containing the keyword from the web:")
        for sentence in related_sentences:
            print(sentence)

        # 5. 문장에서 단어 추출 및 필터링
        all_words = set()
        for sentence in related_sentences:
            words = sentence.split()
            for word in words:
                clean_word = word.strip(".,!?\"'()[]{}<>")
                if clean_word:
                    all_words.add(clean_word)

        filtered_words = filter_words_with_keyword(all_words, user_input)

        print(f"\nFiltered words containing '{user_input}':")
        if keywords_with_counts[user_input] >= 5:
            print(user_input) #가장 먼저 출력

        for word in sorted(filtered_words):
            if word != user_input:
                print(word)

        # 6. 변경된 키워드와 카운트를 파일에 저장
        save_keywords_with_counts(file_path, keywords_with_counts)

if __name__ == "__main__":
    main()

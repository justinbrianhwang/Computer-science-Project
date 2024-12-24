import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/boxoffice/weekly'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # 영화 정보를 포함한 모든 순위 요소를 추출합니다.
    divs = soup.find_all('div', class_='thumb_cont')

    # 1위부터 5위까지의 영화 정보를 출력합니다.
    print('[주간 박스 오피스 랭킹 1위부터 5위]\n')
    for i, div in enumerate(divs[:5], start=1):
        rank = i
        title = div.find('strong', class_='tit_item').text.strip()

        info_txt = div.find('span', class_='txt_info')
        release_date = info_txt.find('span', class_='txt_num').text.strip()
        
        audience_span = div.find('span', string='관객수')
        audience = audience_span.find_next_sibling(string=True).strip().replace('명', '')
        
        print(f'{rank}위: {title}\t(개봉일:{release_date})\n     (누적관객수: {audience}명)\n')
else:
    print('요청에 실패했습니다.')
    



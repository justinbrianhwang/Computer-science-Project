# Python Script to Fetch Weekly Box Office Rankings

This Python script fetches and parses the weekly box office ranking from a specified URL using the `requests` and `BeautifulSoup` libraries. Here’s a detailed explanation of its functionality:

## Import Libraries

- `requests` is used to make HTTP requests to retrieve the webpage content.
- `BeautifulSoup` from the `bs4` library is used for parsing the HTML content of the webpage.

## Fetch Webpage Content

- The script sends a GET request to the URL 'https://movie.daum.net/ranking/boxoffice/weekly'.
- It checks if the request was successful by verifying if the HTTP status code is 200.

## Parse HTML Content

- If the request is successful, it uses `BeautifulSoup` to parse the HTML content of the webpage.

## Extract Movie Information

- It finds all `div` elements with the class `thumb_cont`, which contain the movie information.
- It iterates through the first five of these `div` elements (since we only want the top 5 movies) and extracts the relevant details:
  - **Rank**: Determined by the position in the iteration.
  - **Title**: Extracted from the `strong` element with the class `tit_item`.
  - **Release Date**: Extracted from the `span` element with the class `txt_info`, specifically from its child `span` with the class `txt_num`.
  - **Audience Count**: Extracted from the `span` element that contains the string "관객수", and then from its next sibling element.

## Print Movie Information

- It prints the rank, title, release date, and cumulative audience count for the top 5 movies in a formatted output.

## Error Handling

- If the request to fetch the webpage fails, it prints an error message indicating the failure.

## Code Snippet

Here is a code snippet for the described functionality:

```python
import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/boxoffice/weekly'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all ranking elements containing movie information
    divs = soup.find_all('div', class_='thumb_cont')

    # Print top 5 movies
    print('[Weekly Box Office Rankings from 1st to 5th]\n')
    for i, div in enumerate(divs[:5], start=1):
        rank = i
        title = div.find('strong', class_='tit_item').text.strip()

        info_txt = div.find('span', class_='txt_info')
        release_date = info_txt.find('span', class_='txt_num').text.strip()
        
        audience_span = div.find('span', string='관객수')
        audience = audience_span.find_next_sibling(string=True).strip().replace('명', '')
        
        print(f'{rank}위: {title}\t(Release Date: {release_date})\n     (Cumulative Audience: {audience})\n')
else:
    print('Request failed.')

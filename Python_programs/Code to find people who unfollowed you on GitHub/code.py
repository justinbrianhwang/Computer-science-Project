import requests

username = 'justinbrianhwang'
headers = {'Accept': 'application/vnd.github.v3+json'}

def fetch_all_pages(url, headers):
    results = []
    page = 1
    while True:
        response = requests.get(f"{url}?per_page=100&page={page}", headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        results.extend(data)
        page += 1
    return results

followers_url = f'https://api.github.com/users/{username}/followers'
following_url = f'https://api.github.com/users/{username}/following'

try:
    followers_data = fetch_all_pages(followers_url, headers)
    following_data = fetch_all_pages(following_url, headers)

    followers = {user['login'] for user in followers_data}
    following = {user['login'] for user in following_data}

    unfollowers = following - followers

    print(f"Followers: {len(followers)}")
    print(f"Following: {len(following)}")
    print(f"Unfollowers ({len(unfollowers)}): {unfollowers}")

except requests.exceptions.RequestException as e:
    print(f"API 요청 실패: {e}")
except KeyError as e:
    print(f"응답 파싱 오류: {e}")

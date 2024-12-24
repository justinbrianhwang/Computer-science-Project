import requests

username = 'justinbrianhwang'
headers = {'Accept': 'application/vnd.github.v3+json'}

followers_url = f'https://api.github.com/users/{username}/followers'
following_url = f'https://api.github.com/users/{username}/following'

followers_response = requests.get(followers_url, headers=headers)
following_response = requests.get(following_url, headers=headers)

followers = {user['login'] for user in followers_response.json()}
following = {user['login'] for user in following_response.json()}

unfollowers = following - followers

print("Unfollowers:", unfollowers)

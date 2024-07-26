### GitHub Unfollowers Checker

This Python script checks which users a specified GitHub user is following but who are not following back. It uses the GitHub API to retrieve the lists of followers and followings, then calculates the difference to determine the "unfollowers".

#### Code Breakdown

1. **Import Requests Library**:
    - `import requests` is used to import the `requests` library, which allows the script to send HTTP requests.

2. **Set Variables**:
    - `username = 'justinbrianhwang'`: Specifies the GitHub username to check.
    - `headers = {'Accept': 'application/vnd.github.v3+json'}`: Sets the header to accept GitHub's API version 3 responses.

3. **Define URLs**:
    - `followers_url = f'https://api.github.com/users/{username}/followers'`: URL to fetch the followers of the specified user.
    - `following_url = f'https://api.github.com/users/{username}/following'`: URL to fetch the users that the specified user is following.

4. **Send Requests**:
    - `followers_response = requests.get(followers_url, headers=headers)`: Sends a GET request to the followers URL.
    - `following_response = requests.get(following_url, headers=headers)`: Sends a GET request to the following URL.

5. **Process Responses**:
    - `followers = {user['login'] for user in followers_response.json()}`: Creates a set of followers' usernames from the JSON response.
    - `following = {user['login'] for user in following_response.json()}`: Creates a set of usernames that the specified user is following from the JSON response.

6. **Identify Unfollowers**:
    - `unfollowers = following - followers`: Calculates the difference between the sets of following and followers to identify users who are not following back.

7. **Output Unfollowers**:
    - `print("Unfollowers:", unfollowers)`: Prints the list of unfollowers.

### Example Output

Running this script would produce an output similar to:

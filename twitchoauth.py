import requests

CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost'

auth_url = f'https://id.twitch.tv/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=your_requested_scopes'
print(f'Open this URL in your browser to authorize your application:\n{auth_url}')

authorization_code = input('Enter the authorization code from the URL: ')

token_url = 'https://id.twitch.tv/oauth2/token'
token_params = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'redirect_uri': REDIRECT_URI,
    'code': authorization_code,
    'grant_type': 'authorization_code'
}
response = requests.post(token_url, data=token_params)

if response.status_code == 200:
    token_data = response.json()
    oauth_token = token_data['access_token']
    print(f'OAuth Token: {oauth_token}')
else:
    print('Failed to obtain OAuth token.')



import requests

# Your access token (use the one you obtained earlier)
access_token = 'BQBvdpHzHz___(___)___95Eu__dTi-XQExKOjIs2rsVgei-smz7Kso4Xm'

# Playlist ID of the playlist you want to add tracks to
playlist_id = '4Lqgb___(___)___61SN'

# Headers for the request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Read the URIs from the file you saved
with open('saved_tracks_uris.txt', 'r') as file:
    track_uris = [line.strip() for line in file.readlines()]

# Spotify allows adding up to 100 tracks per request
def add_tracks_to_playlist(playlist_id, uris):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    data = {
        'uris': uris
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print('Tracks added successfully!')
    else:
        print(f'Error: {response.status_code}, {response.json()}')

# Add tracks in batches of 100 (or less)
batch_size = 100
for i in range(0, len(track_uris), batch_size):
    add_tracks_to_playlist(playlist_id, track_uris[i:i+batch_size])

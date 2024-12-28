import requests

# Access token you got from the previous step
access_token = 'BQBvdpHzHzZT9ay___(___)___uo9Xm95Eu__dTi-XQExKOjIs2rsVgei-smz7Kso4Xm'  # Replace with the token you obtained
headers = {
    'Authorization': f'Bearer {access_token}',
}

def get_saved_tracks():
    limit = 50
    offset = 0
    all_tracks = []
    
    while True:
        response = requests.get(f'https://api.spotify.com/v1/me/tracks?limit={limit}&offset={offset}', headers=headers)
        data = response.json()
        
        if 'items' not in data:
            break
        
        for item in data['items']:
            track_uri = item['track']['uri']
            all_tracks.append(track_uri)
        
        # If fewer items are returned, it means we've reached the end
        if len(data['items']) < limit:
            break

        offset += limit

    return all_tracks

# Fetch saved tracks and print URIs
saved_tracks_uris = get_saved_tracks()
print(f'Total saved tracks: {len(saved_tracks_uris)}')

# Optionally, save the URIs to a file
with open('saved_tracks_uris.txt', 'w') as file:
    for uri in saved_tracks_uris:
        file.write(f'{uri}\n')

# spotify_playlist_creator.py
import configparser
import os
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def load_config():
    """Load configuration from config.ini file"""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['spotify']

def get_spotify_client():
    """Create authenticated Spotify client"""
    config = load_config()
    
    auth_manager = SpotifyOAuth(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        redirect_uri=config['redirect_uri'],
        scope='user-library-read playlist-modify-public'
    )
    
    return spotipy.Spotify(auth_manager=auth_manager)

def get_all_liked_songs(sp):
    """Retrieve all liked songs IDs in batches of 50"""
    offset = 0
    batch_size = 50
    all_tracks = []
    
    while True:
        results = sp.current_user_saved_tracks(limit=batch_size, offset=offset)
        if not results['items']:
            break
            
        track_ids = [item['track']['id'] for item in results['items']]
        all_tracks.extend(track_ids)
        offset += batch_size
        
    return all_tracks

def create_playlist(sp, playlist_name=None):
    """Create a new playlist with the given name or default name"""
    if not playlist_name:
        current_date = datetime.now()
        playlist_name = f"Liked {current_date.strftime('%Y-%m')}"
    
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(
        user_id, 
        playlist_name,
        description=f"Your Liked Songs as of {datetime.now().strftime('%Y-%m-%d')}"
    )
    return playlist

def add_tracks_to_playlist(sp, playlist_id, track_ids):
    """Add tracks to playlist in batches of 100"""
    batch_size = 100
    for i in range(0, len(track_ids), batch_size):
        batch = track_ids[i:i + batch_size]
        sp.playlist_add_items(playlist_id, batch)

def main():
    try:
        # Initialize Spotify client
        sp = get_spotify_client()
        
        # Get all liked songs
        print("Fetching your Liked Songs...")
        liked_songs = get_all_liked_songs(sp)
        
        # Get playlist name from user or use default
        playlist_name = input("Enter playlist name (press Enter for default): ").strip()
        
        # Create new playlist
        print("Creating playlist...")
        playlist = create_playlist(sp, playlist_name if playlist_name else None)
        
        # Add tracks to playlist
        print("Adding tracks to playlist...")
        add_tracks_to_playlist(sp, playlist['id'], liked_songs)
        
        print(f"Successfully created playlist '{playlist['name']}' with {len(liked_songs)} tracks!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
if __name__ == "__main__":
    main()


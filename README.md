# spotify-liked-list-workaround

I refuse to update my Spotify app on Android since they just love breaking things that I use, for no reason at all, such as the Liked Songs list that I liked to shuffle. This script will take all your Liked songs and add them to a new 'normal' playlist, which does still work normally, to regain that option.

After creating a new application on Spotify's API dashboard, run this script to generate the playlist with either a custom name or 'Liked YYYY-MM' as the default.

## Usage
- (only first time)
    - Create virtual python environment and install package `spotipy` from pip
    - Create application on Spotify's site (note the values for the next step)
        - Go to https://developer.spotify.com/dashboard
        - 'Create app', make up some name and description, set `http://localhost:8888/callback` as Redirect URI, select Web API, save
        - Next, go to that entry's settings, take the Client ID and secret and replace them in `config.ini`, then save that file

- Activate the environment: open terminal, cd to cloned repo, then do `source ./.venv/bin/activate` (Linux)
- Use `python3 spotify_playlist_creator.py` to run script. It will open your browser for authentication and then do its thing. It works in batches, so depending on the number of tracks, it may take some time.

Issues? Delete the `.cache` file and retry

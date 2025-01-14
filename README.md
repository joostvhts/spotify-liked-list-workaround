# spotify-liked-list-workaround

!! important !! the scripts don't work in this form due to removing imports from non-first scripts

I refuse to update my Spotify app on Android since they just love breaking things that I use, for no reason at all. This set of scripts circumvents the fact that they just flat-out broke the Liked Songs list that I liked to shuffle.

The set of scripts currently authenticates, then gets a list of the songs I've liked, then adds those songs to a specified existing playlist.

## Usage
- (only first time)
    - Create virtual python environment and install package `spotipy` from pip
    - Create application on Spotify's site (note the values for the next step)
    - Replace values for:
        - `client_id`
        - `client_secret`
        - `redirect_uri`
- Activate the environment: `source ./.venv/bin/activate` (Linux)
- Run script

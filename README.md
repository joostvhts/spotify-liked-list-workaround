# spotify-liked-list-workaround

!! important !! the scripts don't work in this form due to removing imports from non-first scripts

I refuse to update my Spotify app on Android since they just love breaking things that I use, for no reason at all. This set of scripts circumvents the fact that they just flat-out broke the Liked Songs list that I liked to shuffle.

The set of scripts currently authenticates, then gets a list of the songs I've liked, then adds those songs to a specified existing playlist.

## Usage
- Create application on Spotify's site (note the values for the next step)
- Replace values for:
    - `client_id`
    - `client_secret`
    - `redirect_uri` (https://domain.tld/callback)
- Run script
- Script will generate a link. After clicking the link and authenticating note the code at the end of the callback URL. Copy everything after `&code=`, paste this in the terminal prompt and hit enter.


## To do
- improve authentication stuff
- have it create a new playlist instead of having to do that manually first
- merge things into one script
- ideally make this available for the world
- somehow make Spotify go bankrupt to fix their monopoly

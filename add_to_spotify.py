import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Informações da sua conta, tudo isso você consegue no site https://developer.spotify.com/
CLIENT_ID = 'CLIENT_ID' # Será algo como as9da9g5sd5a8wf4f4as8f
CLIENT_SECRET = 'CLIENT_SECRET' # Vai estar logo abaixo do Client ID
REDIRECT_URI = 'http://localhost:8000' # Esse link você coloca no URI do seu app no developer.spotify.com
SCOPE = 'playlist-modify-public'

# Autenticação do usuário
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))

# Nome da playlist
playlist_name = 'Nome da playlist'

# Nome do arquivo que contém as músicas
filename = 'arquivo.name' # De preferencia que o arquivo esteja na mesma pasta do codigo, mas se não apenas use o link direto ex: C:/Users/carlinhos/Documents/arquivo.txt

with open(filename, 'r') as f:
    tracks = [line.strip() for line in f.readlines()]

results = []
for track in tracks:
    result = sp.search(q=track, limit=1, type='track')
    if result['tracks']['items']:
        results.append(result['tracks']['items'][0]['uri'])
    else:
        print(f"Não foi possível encontrar a música '{track}' no Spotify")

user = sp.current_user()['id']
playlist = sp.user_playlist_create(user, playlist_name)

sp.playlist_add_items(playlist['id'], results)
print(f"{len(results)} músicas adicionadas à playlist '{playlist_name}'")

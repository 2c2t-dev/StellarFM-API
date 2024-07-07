import base64
import requests

# Remplacez par vos propres valeurs
client_id = '57fca9670f4e45ae9a275623777e8656'
client_secret = '47c5165b3b4547c587d5b4c982a408d7'

def get_access_token(client_id, client_secret):
    # Concaténer le client_id et le client_secret avec ":"
    credentials = f"{client_id}:{client_secret}"
    
    # Encoder en Base64
    credentials_bytes = credentials.encode('ascii')
    credentials_base64 = base64.b64encode(credentials_bytes)
    credentials_base64_str = credentials_base64.decode('ascii')
    print(credentials_base64_str)

    # URL pour obtenir le jeton d'accès
    token_url = "https://accounts.spotify.com/api/token"
    
    # En-têtes et corps de la requête pour obtenir le jeton d'accès
    headers = {
        "Authorization": f"Basic {credentials_base64_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    
    # Faire la requête POST pour obtenir le jeton d'accès
    response = requests.post(token_url, headers=headers, data=data)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Erreur lors de l'obtention du jeton d'accès: {response.status_code}")
        print(response.json())
        return None

def get_artist_data(access_token, artist_id):
    # Utiliser le jeton d'accès pour faire une requête à l'API Spotify
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    artist_response = requests.get(artist_url, headers=headers)
    
    if artist_response.status_code == 200:
        return artist_response.json()
    else:
        #print(f"Erreur lors de la récupération des informations de l'artiste: {artist_response.status_code}")
        #print(artist_response.json())
        return None

# Obtenir le jeton d'accès
access_token = get_access_token(client_id, client_secret)
if access_token:
    #print(f"Access Token: {access_token}")
    
    # Exemple d'utilisation du jeton d'accès pour obtenir des informations sur un artiste
    artist_id = '3TVXtAsR1Inumwj472S9r4'  # Exemple d'ID d'artiste (Drake)
    artist_data = get_artist_data(access_token, artist_id)
    
    if artist_data:
        pass
        #print(artist_data)
else:
    pass
    #print("Impossible d'obtenir le jeton d'accès")

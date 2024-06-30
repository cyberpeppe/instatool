import time
import getpass
from instagrapi import Client

def print_colored(text):
    color = "\033[92m" 
    print(f"{color}{text}\033[0m")

config_path = r'\secret.txt'

username = input('Inserisci l\'username: ')
password = getpass.getpass("Inserisci la password: ")

def write_credentials(file_path, username, password):
    with open(file_path, 'w') as file:
        file.write(f"{username}\n")
        file.write(f"{password}\n")

def read_credentials(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise ValueError("Il file di configurazione deve contenere almeno due righe: username e password.")
        username = lines[0].strip()
        password = lines[1].strip()
        print_colored('Credenziali lette')
        return username, password

write_credentials(config_path, username, password)
username, password = read_credentials(config_path)

try:
    client = Client()
    print_colored('Client configurato')
except Exception as e:
    if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
        print('captcha richiesto, riprova tra alcuni minuti')
        exit()
try:
    client.login(username, password)
    print_colored('Login effettuato')
except Exception as e:
    if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
        print('captcha richiesto, riprova tra alcuni minuti')
        exit()
try:
    followings = client.user_following(client.user_id)
    print_colored('Following completato')
except Exception as e:
    print_colored(f"Errore durante la ricerca dei seguiti: {e}")
    client.logout()
    print_colored('Login...')
    client = Client()
    try:
        client.login(username, password)
        print_colored('Login effettuato')
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('captcha richiesto, riprova tra alcuni minuti')
            exit()
    time.sleep(2)
    followings = client.user_following(client.user_id)
    print_colored('Following completato')

try:
    followers = client.user_followers(client.user_id)
    print_colored('Followers completato')
except Exception as e:
    print_colored(f"Errore durante la ricerca dei followers: {e}")
    client.logout()
    print_colored('Login...')
    client = Client()
    try:
        client.login(username, password)
        print_colored('Login effettuato')
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('captcha richiesto, riprova tra alcuni minuti')
            exit()
    time.sleep(2)
    followers = client.user_followers(client.user_id)
    print_colored('Followers completato')

totale = set(followings.keys()) - set(followers.keys())
print_colored(f"Totale: {len(totale)}")

for user_id in totale:
    try:
        client.user_unfollow(user_id)
        print_colored(f"Unfollowed user id: {user_id}")
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('captcha richiesto, riprova tra alcuni minuti')
            exit()
        print_colored(f"Errore durante l'unfollow dell'utente {user_id}: {e}")
        client.logout()
        print_colored('Login...')
        client = Client()
        try:
            client.login(username, password)
            print_colored('Login effettuato')
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('captcha richiesto, riprova tra alcuni minuti')
                exit()
        time.sleep(5)

print_colored('Fatto')

client.logout()

import time
import getpass
from instagrapi import Client

def print_colored(text):
    color = "\033[92m"  # Codice di escape ANSI per il colore verde
    print(f"{color}{text}\033[0m")

config_path = r'C:\Users\ReadyToUse\Desktop\Data\config\secret.txt'

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
def remove_followers():
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
    if totale == 0:
        print_colored('nessuno trovato')
        exit()
   
    print_colored(f"Totale: {len(totale)}")
    print(totale)

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
        
    for user_id in followers.keys():
        try:
            client.user_follow(user_id)
            print_colored(f"followed user id: {user_id}")
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('captcha richiesto, riprova tra alcuni minuti')
                exit()
            print_colored(f"Errore durante il follow dell'utente {user_id}: {e}")
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
    client.logout()
def following():
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

    
    print(len(followers.keys()))

    
        
    for user_id in followers.keys():
        try:
            client.user_follow(user_id)
            print_colored(f"followed user id: {user_id}")
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('captcha richiesto, riprova tra alcuni minuti')
                exit()
            print_colored(f"Errore durante il follow dell'utente {user_id}: {e}")
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
    client.logout()
write_credentials(config_path, username, password)
username, password = read_credentials(config_path)
print_colored("Seleziona un'operazione:")
print_colored("1. Unfollow utenti che non ti seguono")
print_colored("2. Segui di nuovo tutti i followers")
print_colored("3. Esci")
choice = input("Inserisci il numero dell'operazione: ")
if choice == '1':
    remove_followers()
elif choice == '2':
   following()
elif choice == '3':
    exit()
else:
   print_colored("Scelta non valida. Riprova.")

print_colored('Completato')



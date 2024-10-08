import time
import getpass
from instagrapi import Client
import bcrypt

def print_colored(text):
    color = "\033[92m" 
    print(f"{color}{text}\033[0m")

config_path = r'./secret.txt'

def write_credentials(file_path, username, password):
    with open(file_path, 'wb') as file:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        file.write(f"{username}\n".encode())
        file.write(hashed_password)

def read_credentials(file_path):
    with open(file_path, 'rb') as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise ValueError("The configuration file must contain at least two lines: username and password.")
        username = lines[0].strip().decode()
        hashed_password = lines[1].strip()
        print_colored('Credentials read')
        return username, hashed_password

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password)

username = input('Enter username: ')
password = getpass.getpass("Enter password: ")

write_credentials(config_path, username, password)
username, stored_password = read_credentials(config_path)

def remove_followers():
    ro = get_to_unfollow()
    client = ro["client"]
    to_unfollow = ro["to_unfollow"]

    print_colored(f"Total to unfollow: {len(to_unfollow)}")
    unfollow_count = 0
    for user_id in to_unfollow:
        if unfollow_count >= 250:
            print_colored("Reached the limit of 250 unfollows.")
            exit()
        try:
            client.user_unfollow(user_id)
            unfollow_count += 1
            print_colored(f"[{unfollow_count}]: Unfollowed user id: {user_id}")
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('Captcha required, try again in a few minutes')
                exit()
            print_colored(f"Error unfollowing user {user_id}: {e}")
            client.logout()
            print_colored('Logging in again...')
            client = Client()
            try:
                client.login(username, password)
                print_colored('Login successful')
            except Exception as e:
                if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                    print('Captcha required, try again in a few minutes')
                    exit()
            time.sleep(5)

    client.logout()

def follow_back():
    try:
        client = Client()
        print_colored('Client configured')
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('Captcha required, try again in a few minutes')
            exit()
    try:
        if not verify_password(stored_password, password):
            print_colored('Invalid password')
            exit()
        client.login(username, password)
        print_colored('Login successful')
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('Captcha required, try again in a few minutes')
            exit()
    
    try:
        followers = client.user_followers(client.user_id)
        print_colored('Followers retrieved')
    except Exception as e:
        print_colored(f"Error retrieving followers: {e}")
        client.logout()
        print_colored('Logging in again...')
        client = Client()
        try:
            client.login(username, password)
            print_colored('Login successful')
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('Captcha required, try again in a few minutes')
                exit()
        time.sleep(2)
        followers = client.user_followers(client.user_id)
        print_colored('Followers retrieved')
    following_count = 0
    for user_id in followers.keys():
        if following_count >= 250:
            print_colored("Reached the limit of 250 unfollows.")
            exit()
        
        try:
            client.user_follow(user_id)
            following_count+=1
            print_colored(f"[{following_count}]: Followed user id: {user_id}")
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('Captcha required, try again in a few minutes')
                exit()
            print_colored(f"Error following user {user_id}: {e}")
            client.logout()
            print_colored('Logging in again...')
            client = Client()
            try:
                client.login(username, password)
                print_colored('Login successful')
            except Exception as e:
                if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                    print('Captcha required, try again in a few minutes')
                    exit()
            time.sleep(5)
    client.logout()

def get_to_unfollow():
    try:
        client = Client()
        print_colored('Client configured')
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('Captcha required, try again in a few minutes')
            exit()
    try:
        if not verify_password(stored_password, password):
            print_colored('Invalid password')
            exit()
        client.login(username, password)
        print_colored('Login successful')
    except Exception as e:
        if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
            print('Captcha required, try again in a few minutes')
            exit()
    try:
        followings = client.user_following(client.user_id)
        print_colored('Following retrieved')
    except Exception as e:
        print_colored(f"Error retrieving followings: {e}")
        client.logout()
        print_colored('Logging in again...')
        client = Client()
        try:
            client.login(username, password)
            print_colored('Login successful')
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('Captcha required, try again in a few minutes')
                exit()
        time.sleep(2)
        followings = client.user_following(client.user_id)
        print_colored('Following retrieved')

    try:
        followers = client.user_followers(client.user_id)
        print_colored('Followers retrieved')
    except Exception as e:
        print_colored(f"Error retrieving followers: {e}")
        client.logout()
        print_colored('Logging in again...')
        client = Client()
        try:
            client.login(username, password)
            print_colored('Login successful')
        except Exception as e:
            if isinstance(e, Exception) and 'ChallengeResolve' in str(e):
                print('Captcha required, try again in a few minutes')
                exit()
        time.sleep(2)
        followers = client.user_followers(client.user_id)
        print_colored('Followers retrieved')

    if followings:
        to_unfollow = set(followings.keys()) - set(followers.keys())
    else:
        print('No followings found')
        exit()
    
    return {"client": client, "to_unfollow": to_unfollow}

def list_not_followers():
    
    ro = get_to_unfollow()
    client = ro["client"]
    to_unfollow = ro["to_unfollow"]

    print_colored(f"Total to unfollow: {len(to_unfollow)}")
    for user_id in to_unfollow:
        uname = client.username_from_user_id(user_id)
        with open("./to-unfollow.txt", 'a') as file:
            file.write(uname + "\n")
        print(uname)

    client.logout()


print("Select an operation:")
print("1. Unfollow users who don't follow you back")
print("2. Follow back all followers")
print("3. list_not_followers")
choice = input("Enter the number of the operation: ")

if choice == '1':
    remove_followers()
elif choice == '2':
    follow_back()
elif choice == '3':
    list_not_followers()
else:
    print("Invalid choice. Try again.")

print_colored('Completed')

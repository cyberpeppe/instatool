# Instagram Unfollow Automation Tool

This repository contains a Python tool to automate the "unfollow" action on Instagram using the `instagrapi` library. The main goal is to simplify the management of followed profiles, allowing users to easily remove profiles they no longer wish to follow.

## Key Features

- **Secure Authentication**: Utilizes user-provided Instagram account credentials securely and stores them locally.
- **Error Handling**: Automatically handles errors during the "unfollow" process, including connection issues, challenge requests (such as Captchas), and other Instagram-imposed limitations.
- **Ease of Use**: Once configured with the appropriate credentials, the tool automatically performs the "unfollow" action for all profiles that the user is following but are not following back.

## Additional Features Based on Python Code

- **Credential Management**: Stores Instagram account credentials securely in a local file (`secret.txt`), ensuring ease of access without exposing sensitive information in the code.
  
- **Automatic Login and Error Handling**: Attempts to login to Instagram upon running the script, handling potential challenges (like Captchas) by prompting the user to retry later.
  
- **Followers and Following Analysis**: Retrieves the list of followers and accounts being followed by the user, identifying profiles that do not reciprocate the follow.

- **Unfollow Automation**: Automatically unfollows profiles that do not follow back, enhancing user control over their followed list.

- **Follow Automation**: Automatically follows profiles that follow you.
## Usage Instructions

### Initial Setup

1. Clone the repository to your computer:

    ```bash
    git clone https://github.com/cyberpeppe/instatool.git
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Make the Bash script executable:

    ```bash
    chmod +x instatool.sh
    ```

### Running the Tool

4. Start the Python script to perform the unfollow automation:

    ```bash
    ./instatool.sh
    ```

5. The program will connect to your Instagram account, retrieve the list of your followers and followings, then perform the "unfollow" action for users who are not following you back.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, open issues to report problems or suggest improvements, and propose changes through pull requests. Your contributions are welcome!

## License

This project is released under the MIT. See the `LICENSE.txt` file for more details.

---

© 2024 Project Name. Created by cyberpeppe (https://github.com/cyberpeppe).

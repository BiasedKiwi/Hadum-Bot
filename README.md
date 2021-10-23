![Hadum](https://github.com/shadawcraw/Hadum/blob/master/assets/logo.png)

# Hadum

[![CodeFactor](https://www.codefactor.io/repository/github/shadawcraw/hadum-bot/badge)](https://www.codefactor.io/repository/github/shadawcraw/hadum-bot) ![python](https://img.shields.io/static/v1?label=python&message=^3.8&color=blue) ![license](https://img.shields.io/static/v1?label=license&message=GPL-3.0&color=success) ![build](https://img.shields.io/circleci/build/github/shadawcraw/Hadum-Bot/master)

👋 Hi! I'm Hadum, a multipurpose Discord bot, written in Python.

## 😎 Features

-   👨‍⚖️ A Fully Functional Moderation component: manage your staff, members and permissions all in one bot.
-   🗿 Memes.
-   🤖 Support Chatbot (_Coming Soon™_)

## 👻 Commands

Hadum Features a wide(-ish) set of commands to choose from.

| Command  |             Usage              |                                 Description |
| :------- | :----------------------------: | ------------------------------------------: |
| ping     |            `h.ping`            | Get Latency between bot and Discord Servers |
| coinflip |          `h.coinflip`          |                                Flip a coin! |
| kick     |    `h.kick [user] [reason]`    |                 Kick a user from your guild |
| masskick |      `h.masskick [users]`      |              Kicks multiple users at a time |
| ban      |    `h.ban [user] [reason]`     |                     Permanently Bans a user |
| massban  |      `h.massban [users]`       |               Bans multiple users at a time |
| purge    | `h.purge [number_of_messages]` |      Delete messages in the current channel |
| meme     | `h.meme`                       |  Get a random meme from r/dankmemes         |
| reddit   |  `h.reddit [name_of_subreddit]`|  Get a random post from the subreddit entered |

## 👩‍💻 Command Line Args

Hadum Features a few CLI args to choose from (more coming soon)

| Name/Flag |                        Description |
| :-------- | ---------------------------------: |
| `-q`      | Skip the 'Hadum' loading animation |
| `-v`      |         Show error logs in console |
| `-h`      |                           Get help |

To use them, enter

```shell
python main.py /[ARG_FLAG]  # Windows
python3 main.py -[ARG_FLAG] # Linux/Unix-like/Windows WSL
```

## 🖥 Hosting on your own machine

So, you edited the code to your own liking and now you want to host it on your own machine? No problem! There are 3 ways of installing the bot:

1. (NOTE: This is now deprecated, use Docker instead.)
   For an automatic install, run `bash scripts/install.sh` (Linux/Unix or Windows WSL only) in the **root directory** of the project

2. For a Docker Installation, run the following command (don't ignore comments!):

   ```shell
   docker run -it $(docker build --build-args token=BOT_TOKEN -q .)  # Replace 'BOT_TOKEN' with your token.
   ```

3. Or by following the steps below for a manual installation of the bot:

   1. Clone the repository using

   ```shell
   git clone https://github.com/shadawcraw/Hadum.git
   cd Hadum  # Accessing the project directory
   ```

   2. To install the dependencies, Run in the root folder of the project the following command:

   ```shell
   python -m pip  --no-cache-dir -r requirements.txt  # Windows
   python3 -m pip3 --no-cache-dir -r requirements.txt # Windows WSL, Linux and UNIX-Like systems (OSX)
   ```

   In a Bash/ZSH shell or in Windows WSL.

   3. Then, create a file named ".env" in the **root folder** of the project.

   4. Once that is done, enter the following lines into the .env file created earlier:
      `TOKEN="[YOUR_TOKEN_HERE]"`
      Remember to put the variable name in ALL CAPS and replace the brackets and the text inside it with your own [token](https://www.writebots.com/discord-bot-token/).

   5. After that, you're all set! Run the `run.sh` file or enter `python main.py` for Windows and `python3 main.py` for Linux and Unix-like systems.

## 📈 Todo List

### Moderation

- [x] Add masskick and massban commands. 
- [ ] Add support for reasons in massban/masskick commands.

## ♻ Changelog

See [CHANGELOG.md](https://github.com/shadawcraw/Hadum/blob/master/CHANGELOG.md)

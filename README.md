![Hadum](https://github.com/shadawcraw/Hadum/blob/master/assets/logo.png) 

<h1 align="center">Hadum</h1>

<h4 align="center">👋 Hi! I'm Hadum, a multipurpose Discord bot, written in Python.</h4>

<h1 align="center">
<img src="https://www.codefactor.io/repository/github/hadumdev/hadum-bot/badge">
<img src="https://img.shields.io/static/v1?label=python&message=^3.8&color=blue">
<img src="https://img.shields.io/static/v1?label=license&message=GPL-3.0&color=success">
<img src="https://github.com/HadumDev/Hadum-Bot/actions/workflows/run_tests.yml/badge.svg"> </br>
<img src="https://github.com/HadumDev/Hadum-Bot/actions/workflows/codeql-analysis.yml/badge.svg">
   <a href="https://discord.com/api/oauth2/authorize?client_id=776117946183188480&permissions=8&scope=bot"><img src="https://img.shields.io/badge/Discord-Invite-blue"></a>
<img src="https://img.shields.io/badge/code%20style-black-000000.svg">
</h1>

## 🏗 Note

This bot is still in heavy development and has no "actual" release yet, be sure to come back once in a while!

## 😎 Features

- 👨‍⚖️ A Fully Functional Moderation component: manage your staff, members and permissions all in one bot.
- 🗿 Memes.
- 🤖 Support Chatbot (_Coming Soon™_)

## 👻 Commands

Hadum Features a wide(-ish) set of commands to choose from.

| Command  |             Usage              |                                  Description |
| :------- | :----------------------------: | -------------------------------------------: |
| ping     |            `h.ping`            |  Get Latency between bot and Discord Servers |
| coinflip |          `h.coinflip`          |                                 Flip a coin! |
| kick     |    `h.kick [user] [reason]`    |                  Kick a user from your guild |
| masskick |      `h.masskick [users]`      |               Kicks multiple users at a time |
| ban      |    `h.ban [user] [reason]`     |                      Permanently Bans a user |
| massban  |      `h.massban [users]`       |                Bans multiple users at a time |
| purge    | `h.purge [number_of_messages]` |       Delete messages in the current channel |
| meme     |            `h.meme`            |           Get a random meme from r/dankmemes |
| reddit   | `h.reddit [name_of_subreddit]` | Get a random post from the subreddit entered |
| autopostmeme | `h.reddit [n_of_memes]`    | Get memes witthout even asking for them!     |

## 👩‍💻 Command Line Args

Hadum Features a few CLI args to choose from.

| Name/Flag |                        Description |
| :-------- | ---------------------------------: |
| `-q`      | Skip the 'Hadum' loading animation |
| `-v`      |         Show error logs in console |
| `-h`      |                           Get help |
| `-V`      | Show useful info about the bot version  |
| `-d`      | Do not load extensions             |

To use them, enter

```shell
python main.py /[ARG_FLAG]  # Windows
python3 main.py -[ARG_FLAG] # Linux/Unix-like/Windows WSL
```

## 🖥 Self-hosting

So, you edited the code to your own liking and now you want to host it on your own machine? No problem! There are 2 ways of installing the bot:

<details>
   <summary>Docker Install.</summary>

   1. For a Docker Installation, edit the following lines in your Dockerfile:

      1. Line 16: Replace the brackets and text inside with your own [Discord Bot Token](https://discord.com/developers/applications)

      2. Line 18 & 19: Replace the brackets and text inside with your own [Reddit Application Secret and ID](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/)

      3. Line 20: Replace the brackets and text inside with your own Reddit Username (don't include 'u/  '!!)

   2. Then, you can build the bot using the following command:
   ```shell
   $ docker build .
   ```

</details>

<details>
   <summary>Manual Install.</summary>

   1. For a manual install, follow these instructions (**NOTE: All the commands that will be mentioned are for Linux only.**):
      
      1. Clone the repository using the following commands:
      ```shell
      $ git clone https://github.com/shadawcraw/Hadum-Bot.git  # Clone the repository
      $ cd Hadum-Bot  # Access the repository's folder
      ``` 

      2. Create a file named '.env' in the root folder of the project with the following command:
      ```shell
      $ touch .env
      ```

      3. Enter the following text inside the file we just created (replace the brackets and text inside with your own info.):
      ```shell
      $ echo TOKEN=[YOUR_DISCORD_BOT_TOKEN] > .env
      $ echo REDDIT_CLIENT_SECRET=[YOUR_REDDIT_APPLICATION_SECRET] > .env
      $ echo REDDIT_CLIENT_ID=[YOUR_REDDIT_APPLICATION_ID] > .env
      ```
      Find out your Reddit Application ID & Secret [with this guide!](https://www.geeksforgeeks.org/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/)

      4. Install the dependencies using pip (Python 3.8 or higher required)
      ```shell
      $ pip3 install --no-cache-dir -r requirements.txt
      ```

      5. After that, you're all set! You can now run the bot using the following command:
      ```shell
      $ cd src/
      $ python3 main.py -v
      ```

</details>
</br>

## 📈 Todo List

### Moderation

- [x] Add masskick and massban commands.
- [ ] Add support for reasons in massban/masskick commands.

### Miscellaneous

- [ ] Add a role manager to create roles and assign them easily.

## ♻ Changelog

See [CHANGELOG.md](https://github.com/shadawcraw/Hadum/blob/master/CHANGELOG.md) 

## License

Hadum is licensed under the GPL v3.0 License. See [LICENSE](https://github.com/HadumDev/Hadum-Bot/blob/master/LICENSE) for details.

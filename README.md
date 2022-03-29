# twitter-bot-gremio



Create a BOT that conects to the Twitter's API and, everyday at 07:03 PM, it twits "GREMIO".


# File Tree

``` bash
 ┣ 📂.vscode
 ┃ ┗ 📜launch.json
 ┣ 📂bot_gremio
 ┃ ┣ 📜app.py
 ┃ ┣ 📜credentials.py
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜__main__.py
 ┣ 📜.gitignore
 ┣ 📜LICENSE
 ┣ 📜Procfile
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜runtime.txt
 ```
 
- app.py: it connects to the Twitter's API to twit the desired text
- credential.py: secret keys to access to the Twitter's API
- Procfile: file to set which file will run
- requirements.txt: Modules to install via pip
- runtime.txt: File to set which language and version was used

# Deploy
The deploy was made using heroku, that you can deploy 5 apps for free.

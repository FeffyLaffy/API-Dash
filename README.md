# API Dash

First [Muse Dash](https://store.steampowered.com/app/774171/Muse_Dash/) Private Server made with flask (python).

## Features
- [x] login account (Disocrd method).
- [x] Custom announcement.
- [x] Custom Music Tag.
- [x] MongoDB create account and get account data

## Supported platform
- [Windows](https://www.microsoft.com/en-us/windows). Tested with Windows 10 and 11.

## Requirements
Required python >= 3.5

Required Discord Developer Client ID and Secert for oauth

## PIP lists to install
Authlib==1.0.1
discord-oauth2==0.2
Flask==2.1.3
pymongo==4.2.0

## How to redirect traffic to development server
### Windows `host` file
- You need open notepad with admin and open folder called `C:\Windows\System32\drivers\etc\hosts` add three domain at the last bottom then save it.
```text
127.0.0.1 prpr-muse-dash.peropero.net
127.0.0.1 us-musedash.peropero.net
127.0.0.1 user-us.peropero.net
```

### mitmproxy
1. Install mitmproxy
2. Install proxy Root CA certificates
3. Set windows proxy setting to localhost:8080
4. Run this
```
mitmproxy -s mitm-addon/redirect-traffic.py
```

## Important

Before you build this project make sure you create a cert/key SSL for the server [here to edit file name cert and key](https://github.com/FeffyLaffy/API-Dash/blob/0c4690de1b40a78bfca189115ac994bfe9c10af4/main.py#L255)

if got any question direct message me at discord Asatako#4152 or join [Discord server](https://discord.gg/8fzZPKvA4j) at here have a nice day 👍 :)

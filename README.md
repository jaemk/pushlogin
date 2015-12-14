# pushlogin
Sends pushbullet notification on successful ssh login

Requires:
    * 'pushbullet.py' lib: (https://github.com/randomchars/pushbullet.py)
    * A pushbullet api key.

clone this repo and create a virtualenv in push\_login `virtaulenv -p python3.5 pushpy`, `pip install -r requirements.txt`, fix the shebang line in 'push\_login.py' 

Create a file 'push.conf' in push\_login containing:
    `key = apikeytexthere`

Add a line to your /etc/bash.bashrc (for all users) or ~/.bashrc (for current user only)
    `/path/to/ssh_login.py`
    

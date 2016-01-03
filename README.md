# pushlogin.py
Sends pushbullet notification on successful ssh login

Requires:
* 'pushbullet.py' lib: (https://github.com/randomchars/pushbullet.py)
* A pushbullet api key.
* clone this repo and create a virtualenv in pushlogin `virtaulenv -p python3.x pbenv`
  * `pip install -r requirements.txt`
* rename settings_copy.py to settings.py
  * update settings.py with _your_ secret pushbullet key
  * update settings.py with the virtual env name (default is pbenv)   


Add a line to your /etc/bash.bashrc (for all users) or ~/.bashrc (for current user only)
    `/path/to/ssh_login.py`
    

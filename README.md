iagobot
=======

simple Whatsapp bridge to and from IRC based on irclib and yowsup

### Current Features

1. Send messages to one IRC channel from one groups whatsapp
2. Send messages to one group whatsapp from one IRC channel
3. Let users join the group whatsapp by telling the bot to `add` them (leave / join when you like)
4. Send images and locations to whatsapp - see a clickable URL on IRC
5. Get notifications about joining / leaving whatsapp users on IRC

### Installation

1. `apt-get install python-irclib python-dateutil`
2. `git clone https://github.com/cybertim/iagobot.git`
3. `cd iagobot`
4. `git submodule init`
5. `git submodule update`

### Configuration

1. copy `config.py.example` to `config.py`
2. edit the `config.py` with your fav editor
3. set all settings according to your own wishes
4. run `./bot.py` while testing
5. or run `./boy.py > log.txt &` to launch it in the background

### Setup for the Impatient

1. First register your ***iagobot*** with whatsapp (see registration with whatsapp) and set the correct settings in the `config.py`
2. Keep the `wa_group` empty for the first run
3. Start the bot by executing `./bot.py` and keep the log open
4. Start a normal whatsapp chat with the iagobot
5. Say `help` and iagobot will tell you all the options
6. Let the bot create a group by saying `create`, after the creation you can tell the bot to `add` you
7. Check your log for ***!!!!!!!! JID: 123123123-123123123@g.us !!!!!!!!***
8. And copy this JID (all numbers including the `@g.us`) in the `wa_group` setting of the `config.py` so the bot knows the exact group when its restarted

Now ***everybody*** (new users) who likes to ***enter the group whatsapp*** can add the iagobots phone number to its contact list and ask him to `add`
***Remember*** to add every new person to the `config.py` so the iagobot knows what name to show on irc when a person chats on whatsapp (else you will see `unknown` on IRC).

### Registration Whatsapp

You can register an extra phone number (buy an extra simcard) to use with this bot.
To register to whatsapp and get the correct password:

1. go to http://whitesoft.dyndns.org:2222/whatsapp_sms and request an sms
2. clone yowsup (or use yowsup delivered with iagobot)
3. use: `./yowsup-cli --register <code from sms>`
4. copy / paste the password from the output to the `config.py`

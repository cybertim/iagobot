iagobot
=======

simple Whatsapp bridge to and from IRC based on irclib and yowsup

### Configuration

1. copy 'config.py.example' to 'config.py'
2. edit the 'config.py' with your fav editor
3. set all settings according to your own wishes
4. run './bot.py'

### Usage Information

You can set a whatsapp 'jid' of the whatsapp group in the 'config.py' but if you invite the 'iagobot' to a groupschat it will be the default group for the running session.
This is also an easy way to retreive the 'whatsapp group jid' from the logs and set it as a default in the 'config.py'

Currently the bot can only join 1 channel and 1 groupschat.

### Registration Whatsapp

You can register an extra phone number (by an extra simcard) to use with this bot.
To register to whatsapp and get the correct password:

1. go to http://whitesoft.dyndns.org:2222/whatsapp_sms and request an sms
2. clone yowsup (or use yowsup delivered with iagobot)
3. use: ./yowsup-cli --register <code from sms>
4. copy / paste the password from the output to the 'config.py'

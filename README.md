iagobot
=======

simple Whatsapp bridge to and from IRC based on irclib and yowsup

### Configuration

1. copy 'config.py.example' to 'config.py'
2. edit the 'config.py' with your fav editor
3. set all settings according to your own wishes
4. run './bot.py'

### Usage Information

First register your 'iagobot' with whatsapp (see registration with whatsapp) and set the correct settings in the config.py.
Keep the 'wa_group' empty for the first run.
Start the bot by executing './bot.py' and keep the log open.

Start a whatsapp chat with the bot (use the new registered phone number set in the 'config.py')
You can say 'help' and see all the options.
Let the bot create a group by saying 'create', after the creation you can tell the bot to 'add' you.

Check your log for "!!!!!!!! JID: 123123123-123123123@g.us !!!!!!!!"
And copy this JID (all numbers including the '@g.us') in the 'wa_group' setting of the 'config.py' so the bot knows the exact group when its restarted.

Now everybody who likes to enter the group whatsapp can add the bots phone number to its contact list and ask him to 'add'.

Remember to add every new person to the 'config.py' so the bot knows what name to show on irc when a person chats on whatsapp.

Currently the bot can only join 1 channel and 1 groupschat.

### Registration Whatsapp

You can register an extra phone number (buy an extra simcard) to use with this bot.
To register to whatsapp and get the correct password:

1. go to http://whitesoft.dyndns.org:2222/whatsapp_sms and request an sms
2. clone yowsup (or use yowsup delivered with iagobot)
3. use: ./yowsup-cli --register <code from sms>
4. copy / paste the password from the output to the 'config.py'

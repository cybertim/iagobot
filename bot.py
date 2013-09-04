#!/usr/bin/python
import time
import base64
from irclib import IRC, ServerConnectionError
from Yowsup.connectionmanager import YowsupConnectionManager
from config import *

ycm = YowsupConnectionManager()
signalsInterface = ycm.getSignalsInterface()
methodsInterface = ycm.getMethodsInterface()

client = IRC()
try:
    irc = client.server().connect(irc_server, irc_port, irc_nickname)
except ServerConnectionError as x:
    print x
    exit(1)

def ircOnPubMsg(connection, event):
    text = event.source().split('!')[0] + "> " + event.arguments()[0]
    if wa_group == "":
        print "set a whatsapp group first!"
    else:
        methodsInterface.call("message_send", (wa_group, text.encode("utf-8")))

def ircOnPrivMsg(connection, event):
    print event.arguments

def ircOnConnect(connection, event):
    irc.join(irc_channel)

def ircOnDisconnect(connection, event):
    print "irc disconnected"
    exit(0)

def waOnAuthFailed(username, reason):
    print "Logging failed because %s" % reason

def waOnAuthSuccess(username):
    print "Logged in with %s" % username
    methodsInterface.call("ready")

def waOnMessageReceived(messageId, jid, messageContent, timestamp, wantsReceipt, pushName, isBroadCast):
    repeatMessage(messageId, jid, messageContent)

def repeatMessage(messageId, jid, messageContent):
    try:
        nick = wa_contacts[jid[:11]]
    except KeyError:
        nick = "unknown"
    irc.privmsg(irc_channel, "[" + nick + "] " + messageContent)
    methodsInterface.call("message_ack", (jid, messageId))

def waOnGroupMessageReceived(messageId, jid, author, messageContent, timestamp, wantsReceipt, pushName):
    if wa_group == "":
        print "setting group to " + jid
        global wa_group
        wa_group = jid
    repeatMessage(messageId, jid, messageContent)

wa_password = base64.b64decode(bytes(wa_password.encode('utf-8')))

# whatsapp handlers

signalsInterface.registerListener("auth_fail", waOnAuthFailed)
signalsInterface.registerListener("auth_success", waOnAuthSuccess)
signalsInterface.registerListener("message_received", waOnMessageReceived)
signalsInterface.registerListener("group_messageReceived", waOnGroupMessageReceived)

# irc handlers

irc.add_global_handler("disconnect", ircOnDisconnect)
irc.add_global_handler("welcome", ircOnConnect)
irc.add_global_handler("privmsg", ircOnPrivMsg)
irc.add_global_handler("pubmsg", ircOnPubMsg)

methodsInterface.call("auth_login", (wa_username, wa_password))

# main loop
client.process_forever()

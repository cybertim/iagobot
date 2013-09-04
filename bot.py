#!/usr/bin/python
import time
import base64
from irclib import IRC, ServerConnectionError
from Yowsup.connectionmanager import YowsupConnectionManager
from config import *

ycm = YowsupConnectionManager()
signalsInterface = ycm.getSignalsInterface()
methodsInterface = ycm.getMethodsInterface()
# temp var for the creation of group
creator = ""

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

def waOnGroupCreate(groupJid):
    global wa_group
    wa_group = groupJid
    print irc_channel + " group created! !!!!!! JID: " + groupJid + " !!!!!!"
    text = irc_channel + " was created, please type 'add' to join"
    methodsInterface.call("message_send", (creator, text.encode("utf-8")))

def waGroupCreateFail(errorCode):
    print irc_channel + " creation failed: " + errorCode

def waOnAuthFailed(username, reason):
    print "Logging failed because %s" % reason

def waOnAuthSuccess(username):
    print "Logged in with %s" % username
    methodsInterface.call("ready")

def waOnMessageReceived(messageId, jid, messageContent, timestamp, wantsReceipt, pushName, isBroadCast):
    if messageContent.lower() == "add":
        text = "you have been added to " + irc_channel
        methodsInterface.call("message_send", (jid, text.encode("utf-8")))
        methodsInterface.call("group_addParticipant", (wa_group, jid))
        methodsInterface.call("message_send", (jid, text.encode("utf-8")))
    if messageContent.lower() == "help":
        text = "say 'create' to let me create the groupschat if it is not existing yet or say 'add' and I will add you to the existing " + irc_channel
        methodsInterface.call("message_send", (jid, text.encode("utf-8")))
    if messageContent.lower() == "create":
        global creator
        creator = jid
        text = "say 'add' and I will add you to " + irc_channel
        methodsInterface.call("message_send", (jid, text.encode("utf-8")))
        methodsInterface.call("group_create", (irc_channel,))
    methodsInterface.call("message_ack", (jid, messageId))

def waOnGroupMessageReceived(messageId, jid, author, messageContent, timestamp, wantsReceipt, pushName):
    if wa_group == "":
        print "setting group to " + jid
        global wa_group
        wa_group = jid
    try:
        nick = wa_contacts[author[:11]]
    except KeyError:
        nick = "unknown"
    irc.privmsg(irc_channel, "[" + nick + "] " + messageContent)
    methodsInterface.call("message_ack", (jid, messageId))

wa_password = base64.b64decode(bytes(wa_password.encode('utf-8')))

# whatsapp handlers
signalsInterface.registerListener("auth_fail", waOnAuthFailed)
signalsInterface.registerListener("auth_success", waOnAuthSuccess)
signalsInterface.registerListener("message_received", waOnMessageReceived)
signalsInterface.registerListener("group_messageReceived", waOnGroupMessageReceived)
signalsInterface.registerListener("group_createSuccess", waOnGroupCreate)
signalsInterface.registerListener("group_createFail", waGroupCreateFail)
# irc handlers
irc.add_global_handler("disconnect", ircOnDisconnect)
irc.add_global_handler("welcome", ircOnConnect)
irc.add_global_handler("privmsg", ircOnPrivMsg)
irc.add_global_handler("pubmsg", ircOnPubMsg)

methodsInterface.call("auth_login", (wa_username, wa_password))

# main loop
client.process_forever()

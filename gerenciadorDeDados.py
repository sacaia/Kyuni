import discord
import json
import dados
import re

def serverJaRegistrado(serverID):
    file = open("data/servers.txt", "r")
    for linha in file:
        l = linha[:-1]
        try:
            server = json.loads(l)
            if(server["serverID"] == serverID):
                file.close()
                return True
        except:
            pass

    file.close()
    return False

def getServer(serverID):
    file = open("data/servers.txt", "r")
    for linha in file:
        l = linha[:-1]
        try:
            server = json.loads(l)
            if (server["serverID"] == serverID):
                file.close()
                return dados.Server(server["serverID"], server["logChannelID"], server["rolepickerIDs"])
        except:
            pass

    file.close()
    return None

def registrarServer(server):
    file = open("data/servers.txt", "a")
    file.write(json.dumps(server.__dict__) + "\n")
    file.close()

def updateServer(server):
    fileR = open("data/servers.txt", "r")
    linhas = fileR.readlines()
    novasLinhas = []
    for linha in linhas:
        l = linha[:-1]
        sv = json.loads(l)
        if (sv["serverID"] == server.serverID):
            sv["logChannelID"] = server.logChannelID
            sv["rolepickerIDs"] = server.rolepickerIDs
            linha = json.dumps(sv) + "\n"
        novasLinhas.append(linha)
    fileR.close()

    fileW = open("data/servers.txt", "w")
    fileW.writelines(novasLinhas)
    fileW.close()

def getLogChannelID(serverID):
    file = open("data/servers.txt", "r")
    linhas = file.readlines()
    for linha in linhas:
        l = linha[:-1]
        server = json.loads(l)
        if (server["serverID"] == serverID):
            file.close()
            return server["logChannelID"]
    file.close()
    return None

def hasEmoji(str):
    emojis = dados.EMOJIS()

    for emoji in emojis:
        if(emoji in str):
            return True

    return False

def getEmojisFromMessage(message):
    unicodeEmojis = []
    customEmojis = []

    i = 0
    while i < len(message.content):
        if (message.content[i] in dados.EMOJIS()):
            unicodeEmojis.append((i, message.content[i:i + re.search(r'\s|\w', message.content[i:] + " ").start()]))
            i += re.search(r'\s|\w', message.content[i:] + " ").start()
        else:
            i += 1
    for customEmoji in re.findall(r'<:\w*:\d*>', message.content):
        customEmojis.append((message.content.index(customEmoji), customEmoji))

    i = 0
    for i in range(len(unicodeEmojis)):
        for j in range(len(customEmojis)):
            if (customEmojis[j][0] < unicodeEmojis[i][0]):
                unicodeEmojis.insert(i, customEmojis[j])
                customEmojis.remove(customEmojis[j])
                break

    return unicodeEmojis + customEmojis

def getRolesFromMessage(message):
    roles = []

    for role in re.findall(r'<@&\d*>', message.content):
        roles.append((message.content.index(role), role))

    return roles

def getCorrespondingRole(message, emoji):
    emojis = getEmojisFromMessage(message)
    roles = getRolesFromMessage(message)
    i=0
    achou = False

    for i in range(len(emojis)):
        if(emoji == emojis[i][1]):
            achou = True
            break

    if(not achou):
        return None

    for role in message.role_mentions:
        if(roles[i][1] == role.mention):
            return role

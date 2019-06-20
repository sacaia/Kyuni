import discord
import random
import os
import json
import dados
import gerenciadorDeDados
import discord.ext
from discord.ext import tasks, commands

segredo = "9PMofakzvoMUAvvqhGTWa4G0e3KR6a9U"
token = "NTg4ODYyNzAzNDYwOTQxODU0.XQLYow.CU-brir30Kn9QhuWHyXKYOd4Sak"

activity = discord.Activity()
activity.name = ".help | Esperando alguem para ajudar"
activity.type = discord.ActivityType.playing
activity.state = "Observando"
activity.details = "Caso precise de ajuda use \".help\""
activity.timestamps = {"start": 1000}

##############EMBED-HELP##############
embed_help = discord.Embed()
embed_help.colour = discord.Colour.dark_purple()
#embed_help.color = discord.Color.dark_purple()
embed_help.title = "Lista de comandos"
embed_help.description = "Para usar qualquer comando basta usar `.<comando>`\n"
embed_help.description +="**Ações:**\n`bite` `slap` `cry` `highfive` `lick` `pat` `hug` `cuddle` `nuzzle` `kiss`"
embed_help.set_footer(text="Para informações sobre cada comando use `.help <comando>`")
##############EMBED-BITE##############
embed_bite = discord.Embed()
embed_bite.colour = discord.Colour.dark_purple()
embed_bite.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589096897751285761/bite.jpg")
embed_bite.title = "Bite help"
embed_bite.description = "`.bite @user` : *Morde um ou mais usuarios*\n"
embed_bite.description +="Escolhe uma imagem ou um gif aleatório para ser exibido\n\n"
embed_bite.description +="**Extenções**\n`-img` : Necessariamente escolhe uma imagem\n`-gif` : Necessariamente escolhe um gif"
embed_bite.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-SLAP##############
embed_slap = discord.Embed()
embed_slap.colour = discord.Colour.dark_purple()
embed_slap.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589144364161302563/slap.jpg")
embed_slap.title = "Slap help"
embed_slap.description = "`.slap @user` : *Estapeia um ou mais usuarios*\n"
embed_slap.description +="Escolhe um gif aleatório para ser exibido\n"
embed_slap.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-CRY##############
embed_cry = discord.Embed()
embed_cry.colour = discord.Colour.dark_purple()
embed_cry.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589269732406984704/cry.png")
embed_cry.title = "Cry help"
embed_cry.description = "`.cry` : *Exibe um gif de choro aleatorio*\n"
#embed_cry.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-LICK##############
embed_lick = discord.Embed()
embed_lick.colour = discord.Colour.dark_purple()
embed_lick.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589151423359352852/lick.jpg")
embed_lick.title = "Lick help"
embed_lick.description = "`.lick @user` : *Lambe um ou mais usuarios*\n"
embed_lick.description +="Escolhe um gif aleatório para ser exibido\n"
embed_lick.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-HIGHFIVE##############
embed_highfive = discord.Embed()
embed_highfive.colour = discord.Colour.dark_purple()
embed_highfive.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589152146646237192/highfive.png")
embed_highfive.title = "Highfive help"
embed_highfive.description = "`.highfive @user` : *Highfive um ou mais usuarios*\n"
embed_highfive.description +="Escolhe uma imagem ou um gif aleatório para ser exibido\n"
embed_highfive.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-PAT##############
embed_pat = discord.Embed()
embed_pat.colour = discord.Colour.dark_purple()
embed_pat.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589152745462956053/pat.jpg")
embed_pat.title = "Pat help"
embed_pat.description = "`.pat @user` : *Acaricia um ou mais usuarios*\n"
embed_pat.description +="Escolhe uma imagem ou um gif aleatório para ser exibido\n"
embed_pat.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-HUG##############
embed_hug = discord.Embed()
embed_hug.colour = discord.Colour.dark_purple()
embed_hug.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589110871775641662/hug.jpg")
embed_hug.title = "Hug help"
embed_hug.description = "`.hug @user` : *Abraça um ou mais usuarios*\n"
embed_hug.description +="Escolhe uma imagem ou um gif aleatório para ser exibido\n\n"
embed_hug.description +="**Extenções**\n`-img` : Necessariamente escolhe uma imagem\n`-gif` : Necessariamente escolhe um gif"
embed_hug.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-CUDDLE##############
embed_cuddle = discord.Embed()
embed_cuddle.colour = discord.Colour.dark_purple()
embed_cuddle.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589243610789183505/cuddle.jpg")
embed_cuddle.title = "Cuddle help"
embed_cuddle.description = "`.cuddle @user` : *Abraça amorosamente um ou mais usuarios*\n"
embed_cuddle.description +="Escolhe uma imagem ou um gif aleatório para ser exibido\n\n"
embed_cuddle.description +="**Extenções**\n`-img` : Necessariamente escolhe uma imagem\n`-gif` : Necessariamente escolhe um gif"
embed_cuddle.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-NUZZLE##############
embed_nuzzle = discord.Embed()
embed_nuzzle.colour = discord.Colour.dark_purple()
embed_nuzzle.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589250328487133226/nuzzle.jpg")
embed_nuzzle.title = "Nuzzle help"
embed_nuzzle.description = "`.nuzzle @user` : *Esfrega o rosto em um ou mais usuarios*\n"
embed_nuzzle.description +="Escolhe um gif aleatório para ser exibido\n"
embed_nuzzle.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-KISS##############
embed_kiss = discord.Embed()
embed_kiss.colour = discord.Colour.dark_purple()
embed_kiss.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589152146646237192/highfive.png")
embed_kiss.title = "Kiss help"
embed_kiss.description = "`.kiss @user` : *Beija um ou mais usuarios*\n"
embed_kiss.description +="Escolhe uma imagem ou um gif aleatório para ser exibido\n\n"
embed_kiss.description +="**Extenções**\n`-img` : Necessariamente escolhe uma imagem\n`-gif` : Necessariamente escolhe um gif"
embed_kiss.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
######################################
#client = discord.Client()
client = commands.Bot(command_prefix=".")
client.activity = activity

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #await client.get_channel(588893416746647553).send("ready to rock ;3")


@client.event
async def on_guild_join(guild):
    if(not gerenciadorDeDados.serverJaRegistrado(guild.id)):
        gerenciadorDeDados.registrarServer(dados.Server(guild.id))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.lower().strip()

####################.BITE###########################
    if message.content.startswith('.bite'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        if ("-img" in message.content):
            file = discord.File("bite\\img\\" + str(random.choice(os.listdir("bite\\img\\"))), filename="bite.jpg")
        elif ("-gif" in message.content):
            file = discord.File("bite\\gif\\" + str(random.choice(os.listdir("bite\\gif\\"))), filename="bite.gif")
        else:
            imgOrGif = random.randint(0,1000)
            if (imgOrGif < 700):
                file = discord.File("bite\\gif\\" + str(random.choice(os.listdir("bite\\gif\\"))), filename="bite.gif")
            else:
                file = discord.File("bite\\img\\" + str(random.choice(os.listdir("bite\\img\\"))), filename="bite.jpg")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** mordeu "
        else:
            ret = "**" + str(message.author.nick) + "** mordeu "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]

        await message.channel.send(ret, file=file)
        return
####################.SLAP###########################
    if message.content.startswith('.slap'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        file = discord.File("slap\\gif\\" + str(random.choice(os.listdir("slap\\gif\\"))), filename="slap.gif")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** deu um tapa em "
        else:
            ret = "**" + str(message.author.nick) + "** deu um tapa em "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]

        await message.channel.send(ret, file=file)
        return
####################.CRY###########################
    if message.content.startswith('.cry'):

        file = discord.File("cry\\gif\\" + str(random.choice(os.listdir("cry\\gif\\"))), filename="cry.gif")

        await message.channel.send(file=file)
        return
####################.HIGHFIVE###########################
    if message.content.startswith('.highfive'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        file = discord.File("highfive\\gif\\" + str(random.choice(os.listdir("highfive\\gif\\"))), filename="highfive.gif")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** highfive "
        else:
            ret = "**" + str(message.author.nick) + "** highfive "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]
        ret += "!"

        await message.channel.send(ret, file=file)
        return
####################.LICK###########################
    if message.content.startswith('.lick'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        file = discord.File("lick\\gif\\" + str(random.choice(os.listdir("lick\\gif\\"))), filename="lick.gif")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** lambeu "
        else:
            ret = "**" + str(message.author.nick) + "** lambeu "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]

        await message.channel.send(ret, file=file)
        return
####################.PAT###########################
    if message.content.startswith('.pat'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        file = discord.File("pat\\gif\\" + str(random.choice(os.listdir("pat\\gif\\"))), filename="pat.gif")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** acariciou "
        else:
            ret = "**" + str(message.author.nick) + "** acariciou "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]
        ret += " ❤"

        await message.channel.send(ret, file=file)
        return
####################.HUG###########################
    elif message.content.startswith('.hug'):
        if(len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        if ("-img" in message.content):
            file = discord.File("hug\\img\\" + str(random.choice(os.listdir("hug\\img\\"))), filename="hug.jpg")
        elif ("-gif" in message.content):
            file = discord.File("hug\\gif\\" + str(random.choice(os.listdir("hug\\gif\\"))), filename="hug.gif")
        else:
            imgOrGif = random.randint(0,1000)
            if (imgOrGif < 600):
                file = discord.File("hug\\gif\\" + str(random.choice(os.listdir("hug\\gif\\"))), filename="hug.gif")
            else:
                file = discord.File("hug\\img\\" + str(random.choice(os.listdir("hug\\img\\"))), filename="hug.jpg")

        if(message.author.nick == None):
            ret = "**" + str(message.author.name) + "** abraçou "
        else:
            ret = "**" + str(message.author.nick) + "** abraçou "

        for mention in message.mentions:
            if(mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret)-2)]

        await message.channel.send(ret, file=file)
        return
####################.CUDDLE###########################
    elif message.content.startswith('.cuddle'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        if ("-img" in message.content):
            file = discord.File("cuddle\\img\\" + str(random.choice(os.listdir("cuddle\\img\\"))), filename="cuddle.jpg")
        elif ("-gif" in message.content):
            file = discord.File("cuddle\\gif\\" + str(random.choice(os.listdir("cuddle\\gif\\"))), filename="cuddle.gif")
        else:
            imgOrGif = random.randint(0, 1000)
            if (imgOrGif < 500):
                file = discord.File("cuddle\\gif\\" + str(random.choice(os.listdir("cuddle\\gif\\"))), filename="cuddle.gif")
            else:
                file = discord.File("cuddle\\img\\" + str(random.choice(os.listdir("cuddle\\img\\"))), filename="cuddle.jpg")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** abraçou "
        else:
            ret = "**" + str(message.author.nick) + "** abraçou "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]
        ret += " 💞"

        await message.channel.send(ret, file=file)
        return
####################.NUZZLE###########################
    if message.content.startswith('.nuzzle'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        file = discord.File("nuzzle\\gif\\" + str(random.choice(os.listdir("nuzzle\\gif\\"))), filename="nuzzle.gif")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** se esfregou em "
        else:
            ret = "**" + str(message.author.nick) + "** se esfregou em "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]

        await message.channel.send(ret, file=file)
        return
####################.KISS###########################
    elif message.content.startswith('.kiss'):
        if (len(message.mentions) == 0):
            await message.channel.send("Por favor, mencione, pelo menos, um usuario")
            return

        if ("-img" in message.content):
            file = discord.File("kiss\\img\\" + str(random.choice(os.listdir("kiss\\img\\"))), filename="kiss.jpg")
        elif ("-gif" in message.content):
            file = discord.File("kiss\\gif\\" + str(random.choice(os.listdir("kiss\\gif\\"))), filename="kiss.gif")
        else:
            imgOrGif = random.randint(0, 1000)
            if (imgOrGif < 500):
                file = discord.File("kiss\\gif\\" + str(random.choice(os.listdir("kiss\\gif\\"))), filename="kiss.gif")
            else:
                file = discord.File("kiss\\img\\" + str(random.choice(os.listdir("kiss\\img\\"))), filename="kiss.jpg")

        if (message.author.nick == None):
            ret = "**" + str(message.author.name) + "** beijou "
        else:
            ret = "**" + str(message.author.nick) + "** beijou "

        for mention in message.mentions:
            if (mention.nick == None):
                ret = ret + "**" + str(mention.name) + "**, "
            else:
                ret = ret + "**" + str(mention.nick) + "**, "
        ret = ret[:(len(ret) - 2)]
        ret += " 💗"

        await message.channel.send(ret, file=file)
        return
####################.LOG###########################
    elif message.content.startswith('.log'):
        print(message.author.id)
        if(not message.author.permissions.has("ADMINISTRATOR")):
            await message.channel.send("Desculpe-me <@" + str(message.author.id) + "> você não tem permissão para isso")
        if(not len(message.channel_mentions) == 1):
            await message.channel.send("Por favor, mencione um canal para ser o canal de registro")

####################.HELP###########################
    elif message.content.startswith('.help'):
        if ("bite" in message.content):
            await message.channel.send(embed=embed_bite)
            return

        elif ("slap" in message.content):
            await message.channel.send(embed=embed_slap)
            return

        elif ("cry" in message.content):
            await message.channel.send(embed=embed_cry)
            return

        elif ("highfive" in message.content):
            await message.channel.send(embed=embed_highfive)
            return

        elif ("lick" in message.content):
            await message.channel.send(embed=embed_lick)
            return

        elif ("pat" in message.content):
            await message.channel.send(embed=embed_pat)
            return

        elif ("hug" in message.content):
            await message.channel.send(embed=embed_hug)
            return

        elif ("cuddle" in message.content):
            await message.channel.send(embed=embed_cuddle)
            return

        elif ("nuzzle" in message.content):
            await message.channel.send(embed=embed_nuzzle)
            return

        elif ("kiss" in message.content):
            await message.channel.send(embed=embed_kiss)
            return

        await message.channel.send(embed=embed_help)
        return

@client.event
async def on_message_delete(message):
    if message.author == client.user:
         return

    embed = discord.Embed(colour=discord.Colour.dark_purple(), title="Message deleted", description="**At:** <#"+ str(message.channel.id) + ">\n**Author:** <@" + str(message.author.id) + ">\n" + str(message.content))
    await client.get_channel(588893416746647553).send(embed=embed)
    return

@client.event
async def on_message_edit(before, after):
    if before.author == client.user or after.author == client.user:
        return

    embed = discord.Embed(colour=discord.Colour.dark_purple(), title="Message edited", description="**At:** <#"+ str(before.channel.id) + ">\n**Author:** <@" + str(before.author.id) + ">\n\n***Before:*** \n" + str(before.content) + "\n\n***After:*** \n" + str(after.content))
    await client.get_channel(588893416746647553).send(embed=embed)
    return




client.run(token)
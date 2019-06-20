import discord
from discord.ext import tasks, commands
import discord.ext
import asyncio

import dados
import gerenciadorDeDados

import random
import os
import re
import json

##############ACTIVITY##############
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
embed_help.description +="**Ações:**\n`bite` `slap` `cry` `highfive` `blush` `lick` `pat` `hug` `cuddle` `nuzzle` `kiss`\n"
embed_help.description +="**Staff:**\n`clear` `log` `rolepicker`\n"
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
##############EMBED-BLUSH##############
embed_blush = discord.Embed()
embed_blush.colour = discord.Colour.dark_purple()
embed_blush.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/591156702448189450/blush.jpg")
embed_blush.title = "Blush help"
embed_blush.description = "`.blush` : *Aleatoriamente exibe um gif ou imagem de alguem corando*\n"
#embed_blush.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
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
##############EMBED-CLEAR##############
embed_clear = discord.Embed()
embed_clear.colour = discord.Colour.dark_purple()
#embed_clear.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589152146646237192/highfive.png")
embed_clear.title = "Clear help"
embed_clear.description = "`.clear <qtd>` : *deleta a `<qtd>` de mensagens no canal*\n`cl <qtd>` também pode ser utilizado\n\n"
embed_clear.description +="**Parâmetros**\n`<qtd>` : Deve ser um _numero inteiro_ correspondente a quantidade de mensagens que se deseja apagar (limite de 100 mensagens por vez)"
#embed_clear.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-LOG##############
embed_log = discord.Embed()
embed_log.colour = discord.Colour.dark_purple()
#embed_log.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589152146646237192/highfive.png")
embed_log.title = "Log help"
embed_log.description = "`.log <#canal>` : *define `<#canal>` como o canal de log do servidor*\n"
embed_log.description +="Caso um canal já tenha sido definido este será atualizado para o novo `<#canal>`\n\n"
embed_log.description +="**Parâmetros**\n`<#canal>` : Deve ser uma __mensão a um canal textual__ correspondente ao canal que se deseja mandar as mensagens de log\n\n"
embed_log.description +="**Extenções**\n`-clear` : Não necessita de parâmetros. Remove o canal de log do servidor"
#embed_log.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
##############EMBED-ROLEPICKER##############
embed_rolepicker = discord.Embed()
embed_rolepicker.colour = discord.Colour.dark_purple()
#embed_rolepicker.set_thumbnail(url="https://cdn.discordapp.com/attachments/588893416746647553/589152146646237192/highfive.png")
embed_rolepicker.title = "Rolepicker help"
embed_rolepicker.description = "`.rolepicker <#canal>` : *Espera receber um `rolepicker` valido no `<#canal>` especificado*\n"
embed_rolepicker.description +="Um `rolepicker` é qualquer mensagem que contem uma mesma quantidade de __menções de cargos__ e __emojis__. A ordem dos cargos irá indicar qual é o emoji corresponde e vice-versa\n"
embed_rolepicker.description +="A mensagem pode conter textos, menções, imagens, etc... desde que a restrição acima seja atingida\n"
embed_rolepicker.description +="Para **editar** o `rolepicker` basta editar a mensagem, mantendo a quantidade de __menções de cargos__ iguais a de __emojis__\n"
embed_rolepicker.description +="Para **excluir** o `rolepicker` basta excluir a mensagem\n\n"
embed_rolepicker.description +="**Parâmetros**\n`<#canal>` : Deve ser uma __mensão a um canal textual__ correspondente ao canal que se deseja mandar a mensagens de log\n\n"
#embed_log.set_footer(text="@everyone e @here, bem como cargos não são parâmetros válidos")
######################################

client = commands.Bot(command_prefix=".")
client.remove_command("help")
client.activity = activity
#client.__setattr__("command_prefix", "!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #await client.get_channel(588893416746647553).send("ready to rock ;3")

@client.event
async def on_guild_join(guild):
    if(not gerenciadorDeDados.serverJaRegistrado(guild.id)):
        gerenciadorDeDados.registrarServer(dados.Server(guild.id))

@client.event
async def on_message_delete(message):
    if message.author == client.user:
         return

    logChannelID = gerenciadorDeDados.getLogChannelID(message.guild.id)
    if(logChannelID != None):
        embed = discord.Embed(colour=discord.Colour.dark_purple(), title="Message deleted", description="**At:** <#"+ str(message.channel.id) + ">\n**Author:** <@" + str(message.author.id) + ">\n" + str(message.content))
        await client.get_channel(logChannelID).send(embed=embed)
    return

@client.event
async def on_message_edit(before, after):
    if before.author == client.user or after.author == client.user:
        return

    logChannelID = gerenciadorDeDados.getLogChannelID(before.guild.id)
    if (logChannelID != None):
        embed = discord.Embed(colour=discord.Colour.dark_purple(), title="Message edited", description="**At:** <#"+ str(before.channel.id) + ">\n**Author:** <@" + str(before.author.id) + ">\n\n***Before:*** \n" + str(before.content) + "\n\n***After:*** \n" + str(after.content))
        await client.get_channel(logChannelID).send(embed=embed)
    return

@client.event
async def on_raw_message_delete(payload):
    channel = client.get_channel(payload.channel_id)
    if(payload.cached_message is not None):
        message = payload.cached_message

        if(message.author.id == client.user.id):
            return

    if(payload.guild_id is not None):
        guild = client.get_guild(payload.guild_id)
        server = gerenciadorDeDados.getServer(guild.id)
        if (payload.message_id in server.rolepickerIDs):
            server.removeRolepicker(payload.message_id)
            gerenciadorDeDados.updateServer(server)

@client.event
async def on_raw_message_edit(payload):
    channel = client.get_channel(int(payload.data["channel_id"]))
    message = await channel.fetch_message(payload.message_id)
    if(payload.data["guild_id"] is not None):
        guild = client.get_guild(int(payload.data["guild_id"]))
        server = gerenciadorDeDados.getServer(guild.id)
        if (message.id in server.rolepickerIDs):
            emojis = gerenciadorDeDados.getEmojisFromMessage(message)
            await message.clear_reactions()
            for i in range(min(len(gerenciadorDeDados.getRolesFromMessage(message)), len(emojis))):
                await message.add_reaction(emojis[i][1])

@client.event
async def on_raw_reaction_add(payload):
    if(payload.user_id == client.user.id):
        return

    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = client.get_guild(payload.guild_id)
    server = gerenciadorDeDados.getServer(guild.id)
    emoji = payload.emoji

    if(emoji.is_custom_emoji()):
        emoji = "<:" + emoji.name + ":" + str(emoji.id) + ">"
    else:
        emoji = emoji.name

    if(message.id in server.rolepickerIDs):
        member = guild.get_member(payload.user_id)
        role = gerenciadorDeDados.getCorrespondingRole(message, emoji)
        if(role is None):
            for reaction in message.reactions:
                if (str(reaction.emoji) == emoji):
                    await reaction.remove(message.author)
        else:
            await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    if(payload.user_id == client.user.id):
        return

    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = client.get_guild(payload.guild_id)
    server = gerenciadorDeDados.getServer(guild.id)
    emoji = payload.emoji

    if (emoji.is_custom_emoji()):
        emoji = "<:" + emoji.name + ":" + str(emoji.id) + ">"
    else:
        emoji = emoji.name

    if (message.id in server.rolepickerIDs):
        member = guild.get_member(payload.user_id)
        role = gerenciadorDeDados.getCorrespondingRole(message, emoji)
        await member.remove_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.lower().strip()
    if message.content.startswith(client.command_prefix + "cl"):
        message.content = message.content.replace(client.command_prefix + "cl", client.command_prefix + "clear", 1)

    await client.process_commands(message)

####################.BITE###########################
@client.command()
@commands.guild_only()
async def bite(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    if ("-img" in ctx.message.content):
        file = discord.File("bite\\img\\" + str(random.choice(os.listdir("bite\\img\\"))), filename="bite.jpg")
    elif ("-gif" in ctx.message.content):
        file = discord.File("bite\\gif\\" + str(random.choice(os.listdir("bite\\gif\\"))), filename="bite.gif")
    else:
        imgOrGif = random.randint(0,1000)
        if (imgOrGif < 700):
            file = discord.File("bite\\gif\\" + str(random.choice(os.listdir("bite\\gif\\"))), filename="bite.gif")
        else:
            file = discord.File("bite\\img\\" + str(random.choice(os.listdir("bite\\img\\"))), filename="bite.jpg")

    ret = "**" + ctx.message.author.display_name + "** mordeu "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "

    ret = ret[:(len(ret) - 2)]

    await ctx.send(ret, file=file)
    return

####################.SLAP###########################
@client.command()
@commands.guild_only()
async def slap(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    file = discord.File("slap\\gif\\" + str(random.choice(os.listdir("slap\\gif\\"))), filename="slap.gif")

    ret = "**" + ctx.message.author.display_name + "** deu um tapa em "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "

    ret = ret[:(len(ret) - 2)]

    await ctx.send(ret, file=file)
    return

####################.CRY###########################
@client.command()
@commands.guild_only()
async def cry(ctx):

    file = discord.File("cry\\gif\\" + str(random.choice(os.listdir("cry\\gif\\"))), filename="cry.gif")

    await ctx.send(file=file)
    return

####################.HIGHFIVE###########################
@client.command()
@commands.guild_only()
async def highfive(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    file = discord.File("highfive\\gif\\" + str(random.choice(os.listdir("highfive\\gif\\"))), filename="highfive.gif")

    ret = "**" + ctx.message.author.display_name + "** highfive "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "

    ret = ret[:(len(ret) - 2)]
    ret += "!"

    await ctx.send(ret, file=file)
    return

####################.BLUSH###########################
@client.command()
@commands.guild_only()
async def blush(ctx):
    if ("-img" in ctx.message.content):
        file = discord.File("blush\\img\\" + str(random.choice(os.listdir("blush\\img\\"))), filename="blush.jpg")
    elif ("-gif" in ctx.message.content):
        file = discord.File("blush\\gif\\" + str(random.choice(os.listdir("blush\\gif\\"))), filename="blush.gif")
    else:
        imgOrGif = random.randint(0,1000)
        if (imgOrGif < 600):
            file = discord.File("blush\\gif\\" + str(random.choice(os.listdir("blush\\gif\\"))), filename="blush.gif")
        else:
            file = discord.File("blush\\img\\" + str(random.choice(os.listdir("blush\\img\\"))), filename="blush.jpg")

    ret = "**" + ctx.message.author.display_name + "** corou"

    await ctx.send(ret, file=file)
    return

####################.LICK###########################
@client.command()
@commands.guild_only()
async def lick(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    file = discord.File("lick\\gif\\" + str(random.choice(os.listdir("lick\\gif\\"))), filename="lick.gif")

    ret = "**" + ctx.message.author.display_name + "** lambeu "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "
    ret = ret[:(len(ret) - 2)]

    await ctx.send(ret, file=file)
    return

####################.PAT###########################
@client.command()
@commands.guild_only()
async def pat(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    file = discord.File("pat\\gif\\" + str(random.choice(os.listdir("pat\\gif\\"))), filename="pat.gif")

    ret = "**" + ctx.message.author.display_name + "** acariciou "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "
    ret = ret[:(len(ret) - 2)]
    ret += " ❤"

    await ctx.send(ret, file=file)
    return

####################.HUG###########################
@client.command()
@commands.guild_only()
async def hug(ctx):
    if(len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    if ("-img" in ctx.message.content):
        file = discord.File("hug\\img\\" + str(random.choice(os.listdir("hug\\img\\"))), filename="hug.jpg")
    elif ("-gif" in ctx.message.content):
        file = discord.File("hug\\gif\\" + str(random.choice(os.listdir("hug\\gif\\"))), filename="hug.gif")
    else:
        imgOrGif = random.randint(0,1000)
        if (imgOrGif < 600):
            file = discord.File("hug\\gif\\" + str(random.choice(os.listdir("hug\\gif\\"))), filename="hug.gif")
        else:
            file = discord.File("hug\\img\\" + str(random.choice(os.listdir("hug\\img\\"))), filename="hug.jpg")

    ret = "**" + ctx.message.author.display_name + "** abraçou "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "
    ret = ret[:(len(ret)-2)]

    await ctx.send(ret, file=file)
    return

####################.CUDDLE###########################
@client.command()
@commands.guild_only()
async def cuddle(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    if ("-img" in ctx.message.content):
        file = discord.File("cuddle\\img\\" + str(random.choice(os.listdir("cuddle\\img\\"))), filename="cuddle.jpg")
    elif ("-gif" in ctx.message.content):
        file = discord.File("cuddle\\gif\\" + str(random.choice(os.listdir("cuddle\\gif\\"))), filename="cuddle.gif")
    else:
        imgOrGif = random.randint(0, 1000)
        if (imgOrGif < 500):
            file = discord.File("cuddle\\gif\\" + str(random.choice(os.listdir("cuddle\\gif\\"))), filename="cuddle.gif")
        else:
            file = discord.File("cuddle\\img\\" + str(random.choice(os.listdir("cuddle\\img\\"))), filename="cuddle.jpg")

    ret = "**" + ctx.message.author.display_name + "** abraçou "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "
    ret = ret[:(len(ret) - 2)]
    ret += " 💞"

    await ctx.send(ret, file=file)
    return

####################.NUZZLE###########################
@client.command()
@commands.guild_only()
async def nuzzle(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    file = discord.File("nuzzle\\gif\\" + str(random.choice(os.listdir("nuzzle\\gif\\"))), filename="nuzzle.gif")

    ret = "**" + ctx.message.author.display_name + "** se esfregou em "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "
    ret = ret[:(len(ret) - 2)]

    await ctx.send(ret, file=file)
    return

####################.KISS###########################
@client.command()
@commands.guild_only()
async def kiss(ctx):
    if (len(ctx.message.mentions) == 0):
        await ctx.send("Por favor, mencione, pelo menos, um usuario")
        return

    if ("-img" in ctx.message.content):
        file = discord.File("kiss\\img\\" + str(random.choice(os.listdir("kiss\\img\\"))), filename="kiss.jpg")
    elif ("-gif" in ctx.message.content):
        file = discord.File("kiss\\gif\\" + str(random.choice(os.listdir("kiss\\gif\\"))), filename="kiss.gif")
    else:
        imgOrGif = random.randint(0, 1000)
        if (imgOrGif < 500):
            file = discord.File("kiss\\gif\\" + str(random.choice(os.listdir("kiss\\gif\\"))), filename="kiss.gif")
        else:
            file = discord.File("kiss\\img\\" + str(random.choice(os.listdir("kiss\\img\\"))), filename="kiss.jpg")

    ret = "**" + ctx.message.author.display_name + "** beijou "

    for mention in ctx.message.mentions:
        ret = ret + "**" + mention.display_name + "**, "
    ret = ret[:(len(ret) - 2)]
    ret += " 💗"

    await ctx.send(ret, file=file)
    return

####################.clear###########################
@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, qtd: int):
    if(qtd > 100):
        qtd = 100
    await ctx.message.channel.delete_messages(await ctx.message.channel.history(limit=qtd+1, oldest_first=False).flatten())

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("Desculpe-me <@" + str(ctx.message.author.id) + "> você não tem permissão para isso")
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("<@" + str(ctx.message.author.id) + ">, especifique quantas mensagens deseja limpar")
    elif isinstance(error, discord.ext.commands.errors.BadArgument):
        await ctx.send("<@" + str(ctx.message.author.id) + ">, quantidade de mensagens invalida")
    else:
        print(error)

####################.LOG###########################
@client.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def log(ctx):
    if ("-clear" in ctx.message.content):
        server = gerenciadorDeDados.getServer(ctx.message.guild.id)
        gerenciadorDeDados.updateServer(server)

    else:
        if(not len(ctx.message.channel_mentions) == 1):
            await ctx.send("Por favor, mencione um canal para ser o canal de registro")

        server = gerenciadorDeDados.getServer(ctx.message.guild.id)
        server.setLogChannelID(ctx.message.channel_mentions[0].id)
        gerenciadorDeDados.updateServer(server)
        await ctx.send("O canal de log foi atualizado para <#" + str(ctx.message.channel_mentions[0].id) + "> com sucesso")

@log.error
async def log_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("Desculpe-me <@" + str(ctx.message.author.id) + "> você não tem permissão para isso")

####################.rolePicker###########################
@client.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def rolepicker(ctx, ):
    if(not len(ctx.message.channel_mentions) == 1):
        await ctx.send("Mencione o canal em que pretende criar o rolepicker.\nCaso tenha alguma duvida consulte `.help rolepicker` e tente novamente.")
        return

    def check(m):
        return m.channel == ctx.message.channel_mentions[0] and m.author == ctx.message.author
    try:
        await ctx.send("<@" + str(ctx.message.author.id) + ">, você tem 10 minutos para criar o rolepicker em: <#" + str(ctx.message.channel_mentions[0].id) + ">")
        msg = await client.wait_for('message',timeout=600.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("tempo esgotado")
    else:
        if not(len(msg.role_mentions) > 0 and (len(re.findall(r'<:\w*:\d*>', msg.content)) > 0 or gerenciadorDeDados.hasEmoji(msg.content))):
            await ctx.send("Desculpe-me, <@" + str(ctx.message.author.id) + ">, não pude criar o rolepicker.\nCaso tenha alguma duvida consulte `.help rolepicker` e tente novamente.")
        elif(len(gerenciadorDeDados.getRolesFromMessage(msg)) != len(gerenciadorDeDados.getEmojisFromMessage(msg))):
            await ctx.send(ctx.message.author.mention + ", a quantidade de cargos e emojis tem de ser igual.\nCaso tenha alguma duvida consulte `.help rolepicker` e tente novamente.")
        else:
            server = gerenciadorDeDados.getServer(ctx.guild.id)
            server.addRolepicker(msg.id)
            gerenciadorDeDados.updateServer(server)

            for emoji in gerenciadorDeDados.getEmojisFromMessage(msg):
                await msg.add_reaction(emoji[1])

            await ctx.send("rolepicker criado com sucesso!")



@rolepicker.error
async def rolepicker_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("Desculpe-me <@" + str(ctx.message.author.id) + "> você não tem permissão para isso")
    else:
        print(error)

####################.HELP###########################
@client.command()
async def help(ctx):
    if ("bite" in ctx.message.content):
        await ctx.send(embed=embed_bite)
        return

    elif ("slap" in ctx.message.content):
        await ctx.send(embed=embed_slap)
        return

    elif ("cry" in ctx.message.content):
        await ctx.send(embed=embed_cry)
        return

    elif ("highfive" in ctx.message.content):
        await ctx.send(embed=embed_highfive)
        return

    elif ("blush" in ctx.message.content):
        await ctx.send(embed=embed_blush)
        return

    elif ("lick" in ctx.message.content):
        await ctx.send(embed=embed_lick)
        return

    elif ("pat" in ctx.message.content):
        await ctx.send(embed=embed_pat)
        return

    elif ("hug" in ctx.message.content):
        await ctx.send(embed=embed_hug)
        return

    elif ("cuddle" in ctx.message.content):
        await ctx.send(embed=embed_cuddle)
        return

    elif ("nuzzle" in ctx.message.content):
        await ctx.send(embed=embed_nuzzle)
        return

    elif ("kiss" in ctx.message.content):
        await ctx.send(embed=embed_kiss)
        return

    elif ("clear" in ctx.message.content):
        await ctx.send(embed=embed_clear)
        return

    elif ("log" in ctx.message.content):
        await ctx.send(embed=embed_log)
        return

    elif ("rolepicker" in ctx.message.content):
        await ctx.send(embed=embed_rolepicker)
        return

    await ctx.send(embed=embed_help)
    return


client.run(dados.TOKEN())
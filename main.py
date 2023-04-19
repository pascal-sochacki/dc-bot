import os

import discord
import mysql.connector
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    database="quotes",
    passwd="mauFJcuf5dhRMQrjj"
)


@bot.command()
async def ping(ctx):
    cursorObject = dataBase.cursor()
    cursorObject.execute("SELECT * FROM test")
    myresult = cursorObject.fetchall()

    print(myresult)

    await ctx.send('pong')

@bot.command()
async def pong(ctx):
    cursorObject = dataBase.cursor()

    sql = "INSERT INTO test (NAME, DISCORD_NAME) values (%s, %s)"
    val = ("John", "Highway 21")
    cursorObject.execute(sql, val)
    dataBase.commit()

    await ctx.send('pong')

bot.run(TOKEN)

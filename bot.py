import discord
from config import settings
from discord.ext import commands
from discord import Activity, ActivityType

VERSION = '0.1'
TOKEN = settings['token']
bot = commands.Bot(command_prefix='!')
@bot.command()
async def скажи(ctx, arg)
	await ctx.send(arg)
@bot.event
async def on_ready()
	print("[OK!]Бот запустился.")
	print("[INFO]Версия бота = VERSION")
	await bot.change_presence(status=discord.Status.do_not_disturb,activity=Activity(name="sad songs",type=ActivityType.listening))

bot.run(TOKEN)
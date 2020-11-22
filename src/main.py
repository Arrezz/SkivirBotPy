import discord
import op
import author as writers
import finance
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

#Defining the client secret

with open('../secret.txt') as f:
    token = f.readline()

#Defining all the commands, see individual command files for details

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def opgg(ctx, *args):
    await ctx.send(op.handleCommand(args))

@bot.command()
async def author(ctx):
    await ctx.send(writers.handleCommand())

@bot.command()
async def boats(ctx, *args):
    await ctx.send(finance.handleCommand(args))


print('Woo boy we running')

bot.run(token)

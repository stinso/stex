# bot.py
import discord
import os

from discord.ext import commands, tasks
from stex_client.public import Public
from dotenv import load_dotenv


############### DISCORD ###############
TOKEN = DISCORD_TOKEN="NzY5MTY1MDUxNzg0OTg2NjI0.X5LCxg.MLtgOs6zCtFpekJ4ME7-oqxeQkw"

############### STEX ###############
public = Public()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='ping', help="Answers with pong")
async def ping(ctx):
    await ctx.send("pong")


@bot.command(name='price', help="The price")
async def price(ctx):
    await ctx.send(public.currencies_by_id(71))

bot.run(TOKEN)


ping = public.ping() #https://apidocs.stex.com/#/Public/get_public_ping

if ping['success']:
    print("Welcome champ :)")

    ################## Your code here ##################
    print(public.currencies_by_id(71))
    print(public.currency_pairs_by_id(80))

else:
    print("Something went wrong :(")


"""
public.currencies() #https://apidocs.stex.com/#/Public/get_public_currencies
public.currencies_by_id(1) #https://apidocs.stex.com/#/Public/get_public_currencies__currencyId_
public.markets() #https://apidocs.stex.com/#/Public/get_public_markets
public.pairs_groups() #https://apidocs.stex.com/#/Public/get_public_pairs_groups
public.currency_pairs_list('BTC') #https://apidocs.stex.com/#/Public/get_public_currency_pairs_list__code_
public.pairs_groups_by_id(1) #https://apidocs.stex.com/#/Public/get_public_currency_pairs_group__currencyPairGroupId_
public.currency_pairs_by_id(1) #https://apidocs.stex.com/#/Public/get_public_currency_pairs__currencyPairId_
public.ticker() #https://apidocs.stex.com/#/Public/get_public_ticker
public.ticker_by_currency_pair_id(1) #https://apidocs.stex.com/#/Public/get_public_ticker__currencyPairId_
public.trades_by_currency_pair_id(1, {'limit': 1}) #https://apidocs.stex.com/#/Public/get_public_trades__currencyPairId_
public.orderbook_by_currency_pair_id(1, {'limit_bids': 1, 'limit_asks': 1}) #https://apidocs.stex.com/#/Public/get_public_orderbook__currencyPairId_
public.chart(1, '1D') #https://apidocs.stex.com/#/Public/get_public_chart__currencyPairId___candlesType_
"""
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import csv
import io
import os
import discord
from discord.ext import commands
from discord import Intents

def app_run(token):

    intents =Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='!',intents=intents)


    @client.event
    async def on_ready():
        print(("{client.user} is now running"))



    @client.command()
    async def stocky(ctx,name):
        company = name
        data = yf.download(company,period="1d",interval="1m")
        data.to_csv("stock.csv")

        df = pd.read_csv("stock.csv")

        trace1=go.Scatter(x=df['Datetime'],y=df['High'],name = 'High prices in usd')
        trace2=go.Scatter(x=df['Datetime'],y=df['Low'],name = 'Low prices in usd')
        trace3=go.Scatter(x=df['Datetime'],y=df['Open'],name = 'Open prices in usd')
        trace4=go.Scatter(x=df['Datetime'],y=df['Close'],name = 'Close prices in usd')
        trace5=go.Scatter(x=df['Datetime'],y=df['Adj Close'],name = 'Adj close prices in usd')


        fig2 = go.Figure(data = [trace1,trace2,trace3,trace5])
        fig1 = go.Figure(data=[trace4])

        fig2.update_layout(
            title = 'Stock prices',
            plot_bgcolor = 'rgb(230, 230,230)',
            showlegend = True
        )
        fig1.update_layout(
            title = 'Closing Stock prices',
            plot_bgcolor = 'rgb(230, 230,230)',
            showlegend = True
        )



        if not os.path.exists("images"):
            os.makedirs("images")
        
        fig1.write_image("images/fig1.png",engine = "kaleido")
        fig2.write_image("images/fig2.png",engine = "kaleido")

        with open("images/fig1.png","rb") as im1 , open("images/fig2.png","rb") as im2:
            file1 = discord.File(im1 , filename="fig1.png")
            file2 = discord.File(im2, filename="fig2.png") 



        channel_id = "your-id"
        channel = client.get_channel(channel_id)

        await channel.send(file = file1)
        await channel.send(file = file2)

        #await channel.send(file=discord.File(image1,filename="fig1.png"))
        #await channel.send(file=discord.File(image2,filename="fig2.png"))
    
    client.run(token)

    
    




if __name__ == "__main__":
    token = "your-token"
    app_run(token)
        


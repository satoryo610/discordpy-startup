#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = "Njk2OTU1MzgwODczNTYwMTA0.XowQWA.zL_kS3YLquRYybe6_ORa7o6NjV8" #トークン
CHANNEL_ID = 696951090477924418 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '9:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('出席確認の時間です。')
    if now == '14:50':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('出席確認の時間です。')

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

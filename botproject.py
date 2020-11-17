#pip install -U discord.py
import discord
#pip install requests
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #유저조회 중복 방지
    if message.author.bot:
        return

    if "!" in message.content:
        if message.content.startswith('!유저조회'):
            if "#" in message.content:
                #await message.channel.send(message.content)
                userName = message.content.split("#")[1]

                userData = getUserData(userName)
                e = discord.Embed(title=userData['tierRank'], color=3447003)
                e.set_author(name = "[ " + userData['userName'] + " ]" + " 조회 결과")
                e.set_thumbnail(url=userData['userImage'])

                for item in userData["result"]:
                    Game = item["ChampName"] + " - " + item["GameResult"]
                    KDA = item["Kill"] + " / " + item["Death"] + " / " + item["assist"]
                    e.add_field(name=Game, value=KDA, inline=False)

                await message.channel.send(userName, embed=e)
                getUserData(userName)

            else:
                await message.channel.send('값이 잘못 요청되었습니다.')
                await message.channel.send('!유저조회#<유저명>')
        elif message.content.startswith('!help'):
            await message.channel.send('[Some body Help me💦]\n \n!유저조회#<롤 닉네임> \nUser의 10판의 전적을 검색합니다.\n예시: !유저요청#LoL_JoinBot  '
                                       '\n\n그 외의 기능은 개발자의 귀차니즘으로 인해 개발되지 않습니다..')
        elif message.content.startswith('!?'):
            await message.channel.send('https://tenor.com/view/umm-confused-blinking-okay-white-guy-blinking-gif-7513882')
        elif message.content.startswith('아!'):
            await message.channel.send('https://tenor.com/view/%EA%B4%B4%EB%AC%BC%EC%A5%90-%EB%A7%90%EB%8C%80%EA%BE%B8%ED%95%98%EC%A7%80%EB%A7%88-streamer-mad-angry-gif-16583846')
        else:
            await message.channel.send('명령어를 재대로 입력해주세요')

def getUserData (userName):
    response = requests.get("http://3964bf147c56.ngrok.io/?name="+userName)
    json_val = response.json()
    return json_val

client.run('token')
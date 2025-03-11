from game import Game
from bot import Bot
from human import Human


human=Bot("Ante")
bot=Bot("Bot")
n=0
human_cnt=0
bot_cnt=0
while n<1000:
    game=Game(human,bot)
    if n<=500:
        winner=game.play("p1")
    else:
        winner=game.play("p2")
    if(winner==1):
        human_cnt+=1
    elif(winner==-1):
        bot_cnt+=1
    n+=1

print("\n\n")
print("human_cnt: ",human_cnt)
print("bot_cnt: ",bot_cnt)
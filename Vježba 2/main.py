from game import Game
from bot import Bot
from human import Human

human=Human("Ante")
bot=Bot("Bot")
game=Game(human,bot)
game.play()
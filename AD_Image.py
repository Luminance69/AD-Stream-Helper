import pyautogui as gui
import json
from dota2gsipy.server import GSIServer
from dota2gsipy.map import DOTA2GameState
from time import sleep

from Scripts.TakeScreenshot import TakeScreenshot



regions = json.load(open("Data/Regions.json", "r"))

token = json.load(open("Data/Token.json", "r"))

server = GSIServer(("127.0.0.1", 3000),token)
server.start_server()

prev_game_state = None



while True:
    sleep(1/30)

    if server.game_state.map.state != prev_game_state:
        prev_game_state = server.game_state.map.state

        if server.game_state == DOTA2GameState.DOTA_GAMERULES_STATE_STRATEGY_TIME:
            TakeScreenshot()
import json
import os
import secrets
from pynput.mouse import Listener

from Scripts.TakeScreenshot import TakeScreenshot
from Scripts.OpenImage import OpenImage
from Scripts.FindDota import FindDota



# Setup screenshot locations

def on_click(x, y, button, pressed):
    if not pressed:
        return
    
    global regions
    regions.append(x)
    regions.append(y)

    if len(regions) <= 2:
        print("click on the bottom right corner of the first region")
    elif len(regions) <= 4:
        print("click on the top left corner of the second region")
    elif len(regions) <= 6:
        print("click on the bottom right corner of the second region")
    else:
        print("done")
        print(regions)

        with open("Data/Regions.json", "w") as f:
            json.dump(regions, f)

        TakeScreenshot(regions)

        OpenImage("Data/Draft_Radiant.png")
        OpenImage("Data/Draft_Dire.png")

        listener.stop()


# Setup Dota GSI

def SetupGSI():
    dota_path = FindDota()

    if dota_path == None:
        print("Dota 2 not found")
        return
    
    if not os.path.exists(dota_path + "/game/dota/cfg/gamestate_integration"):
        os.mkdir(dota_path + "/game/dota/cfg/gamestate_integration")

    # Generate secure token

    token = secrets.token_hex(64)

    with open("Data/Token.json", "w") as f:
        json.dump(token, f)

    with open(dota_path + "/game/dota/cfg/gamestate_integration/ad_stream_helper.cfg", "w") as f:
        f.write(f'''
"Dota 2 Integration Configuration"
{{
    "uri"           "http://127.0.0.1:3000"
    "timeout"       "5.0"
    "buffer"        "0.1"
    "throttle"      "0.5"
    "heartbeat"     "30.0"
    "auth"
    {{
        "token"      "{token}"
    }}
    "data"
    {{
        "provider"      "1"
        "map"           "1"
        "player"        "1"
        "hero"          "1"
        "abilities"     "1"
        "items"         "1"
    }}
}}''')



# Main

if __name__ == "__main__":
    if not os.path.exists("Data"):
        os.mkdir("Data")

    with Listener(on_click=on_click) as listener:
        print("Click on the top left corner of the first region")

        regions = []

        listener.join()

        print("Screenshot setup complete")

    SetupGSI()
    
    print("Dota 2 GSI setup complete")
# Installation instructions:

1. Download and extract ZIP folder (I'd recommend putting it somewhere that isnt your Downloads folder)

2. Open the folder in terminal\
   Windows: Open folder in file explorer -> click address bar -> type `cmd` -> enter\
   Linux: You probably already know how to do this\
   MacOS: Good luck lol idfk how this OS works

3. Make sure Python 3 is installed by running `python3 --version` in the terminal.\
   I haven't tested this script on versions of Python other than 3.10, so your mileage may vary.\
   Pretty sure it won't work with <3.6.\
   If Python 3 isn't installed, you can find a download here https://www.python.org/downloads/

4. Make sure pip3 is installed by running `pip3 --version` in the terminal.\
   If pip3 isn't installed, reinstall Python and make sure to check the option to install pip

5. Run `python3 Setup.py` and follow the prompts to complete the setup.\
   I would recommend opening dota and starting a bot match of AD before you start the setup.

6. Assuming you did everything correctly, you should now have everything setup:\
   a. /Data/ should contain 2 .png files and 2 .json files\
   b. [...]/dota 2 beta/game/dota/cfg/gamestate_integration/ad_stream_helper.cfg

7. You can now point your OBS to the 2 image files in /Data/

8. Finally, to start the listener program, run `python3 AD_Image.py`\
   While the listener is running, it will constantly check the Dota game state, and will take screenshots when the game enters the strategy phase.

Notes:\
I might add OBS integration at some later date so that it automatically starts with OBS, idk.\
Also might add some integration to automatically change scenes based on Dota game state, although that should probably be its own thing

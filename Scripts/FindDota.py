import os
import sys

def FindDota():
    default_path = {
        'linux': os.getenv("HOME") + '/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/dota 2 beta', # No idea if this is the same for all systems, linux be weird sometimes
        'win32': 'C:/Program Files (x86)/Steam/steamapps/common/dota 2 beta',
        'darwin': '/Applications/Steam.app/Contents/MacOS/steamapps/common/dota 2 beta' # TODO: verify this is correct, although who the fuck plays dota on a mac
    }[sys.platform]

    # Check if default path points to a real folder
    if os.path.exists(default_path):
        return default_path
    else:
        # Ask user to input their Dota path
        path = input("Please specify your dota 2 beta path: ")

        # Check to see that the end of the path makes sense, and that the path exists
        if not (path[-28:] == "steamapps/common/dota 2 beta" and os.path.exists(path)):
            raise RuntimeError
        else:
            return path

print(FindDota())
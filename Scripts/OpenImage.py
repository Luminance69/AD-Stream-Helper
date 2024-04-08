import sys
import subprocess

def OpenImage(path):
    imageViewerFromCommandLine = {
        'linux':'xdg-open',
        'win32':'explorer',
        'darwin':'open'
    }[sys.platform]
    
    subprocess.run([imageViewerFromCommandLine, path])
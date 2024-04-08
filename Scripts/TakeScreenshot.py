import pyautogui as gui

def TakeScreenshot(regions):
    # Take Screenshot
    image = gui.screenshot()

    # Save the two regions as separate PNG files
    image.crop(regions[0:4]).save("Data/Draft_Radiant.png")
    image.crop(regions[4:8]).save("Data/Draft_Dire.png")
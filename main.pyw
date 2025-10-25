import tkinter as tk
import random
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import POINTER, cast
import time

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

IntervalRandomizeBool = False
VolumeGradientBool = False
gradientNum = 0
RandomizeIntervalTime = 2000

def RandomizeInterval():
    if IntervalRandomizeBool:
        VolumeRandomize()
    else:
        app.after(500, RandomizeInterval)
        return
    app.after(RandomizeIntervalTime, RandomizeInterval)

def VolumeRandomize():
    num = random.randrange(0, 100)
    num = num / 100
    volume.SetMasterVolumeLevelScalar(num, None)

def FrameUpdate():
    # Update Logic

    global gradientNum
    global gradientPositiveState
    
    if VolumeGradientBool:
        
        volume.SetMasterVolumeLevelScalar(gradientNum / 100, None)

        if gradientNum == 100:
            gradientPositiveState = False
        elif gradientNum == 0:
            gradientPositiveState = True

        if gradientPositiveState:
            gradientNum += 2
        else:
            gradientNum -= 2

    VolumeText.config(text=round(volume.GetMasterVolumeLevelScalar() * 100))
    app.after(50, FrameUpdate)

def ToggleIntervalRandomize():
    global IntervalRandomizeBool
    if IntervalRandomizeBool == True:
        IntervalRandomizeBool = False
        IntervalRandomizer.config(
            bg="red")
    else:
        IntervalRandomizeBool = True
        IntervalRandomizer.config(
            bg="green")

def VolumeGradient():
    global VolumeGradientBool
    if VolumeGradientBool:
        VolumeGradientBool = False
        GradientEnable.config(bg="red")
        return
    
    VolumeGradientBool = True
    GradientEnable.config(bg="green")
    gradientPositiveState = True
    return
    

app = tk.Tk()
app.title("Volume Controller")

VolumeText = tk.Label(app, 
    text="50")
VolumeText.pack()

RandomizeVolumeButton = tk.Button(app, 
    text="Randomize Volume", 
    command=VolumeRandomize)
RandomizeVolumeButton.pack()

GradientEnable = tk.Button(app, 
    text="VolumeGradient", 
    command=VolumeGradient,
    bg="red",
    fg="white")
GradientEnable.pack()

IntervalRandomizer = tk.Button(app, 
    text="Randomize Regurarly", 
    command=ToggleIntervalRandomize, 
    bg="red", 
    fg="white")
IntervalRandomizer.pack()

app.after(RandomizeIntervalTime, RandomizeInterval)
app.after(100, FrameUpdate)
app.mainloop()
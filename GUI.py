import PySimpleGUI as sg
from Python4Physics import *

"""
GUI
"""

def massConv(kg = 0, u = 0):
    if kg != 0:
        return massConvKg(kg)
    else:
        return massConvU(u)

def event_loop():
    while True:
        event, values = window.read()    
        if event in (None, "Cancel"):
            break
        try:
            converted_value = massConv(u = float(values["-uInput-"]))
            print(converted_value)
            window["-kgOutput-"].Update(converted_value)
           
        except:
            pass
        try:
            converted_value = massConv(kg = float(values["-kgInput-"]))
            window["-uOutput-"].Update(converted_value)
        except:
            pass
        try:
            window["-wlOutput-"].Update(wlPhoton(float(values["-fotonEnergyInput-"])))
        except:
            pass
                           
    window.Close()

layout = [[sg.Text("Convert u to kg:"), sg.InputText(key="-uInput-", size=(5,1)), sg.Text("", key="-kgOutput-", size=(30,1))],
          [sg.Text("Convert kg to u:"), sg.InputText(key="-kgInput-", size=(5,1)), sg.Text("", key="-uOutput-", size=(30,1))],
          [sg.Text("Convert foton energy to wavelength:"), sg.InputText(key="-fotonEnergyInput-", size=(7,1)), sg.Text("", key="-wlOutput-", size=(20,1))],
          [sg.Button("Ok"), sg.Button("Cancel")]]

window = sg.Window("Physics stuff", layout)

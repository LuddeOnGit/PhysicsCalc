import PySimpleGUI as sg
from Python4Physics import *

"""
GUI
"""

def event_loop():
    while True:
        event, values = window.read()    
        if event in (None, "Cancel"):
            break
        if values["-uInput-"] != " ":
            window["-kgOutput-"].Update(massConvU(float(values["-uInput-"])))
        if values["-kgInput-"] != " ":
            window["-uOutput-"].Update(massConvKg(float(values["-kgInput-"])))
        if values["-fotonEnergyInput-"] != " ":
            window["-wlOutput-"].Update(wlPhoton(float(values["-fotonEnergyInput-"])))
        if event == "Mass":
            window["-missingMassOutput-"].Update(massLeft(float(values["-beforeMassInput-"]), float(values["-afterMassInput-"])))
        if event == "Energy":
            window["-energyOutput-"].Update(mass(massLeft(float(values["-beforeMassInput-"]), float(values["-afterMassInput-"]))))

    window.Close()

layout = [[sg.Text("Convert u to kg:"), sg.InputText(" ", key="-uInput-", size=(5,1)), sg.Text("", key="-kgOutput-", size=(30,1))],
          [sg.Text("Convert kg to u:"), sg.InputText(" ", key="-kgInput-", size=(5,1)), sg.Text("", key="-uOutput-", size=(30,1))],
          [sg.Text("Convert foton energy to wavelength:"), sg.InputText(" ", key="-fotonEnergyInput-", size=(7,1)), sg.Text("", key="-wlOutput-", size=(20,1))],
          [sg.Text("Calculate missing mass (before, after):"), sg.InputText(" ", key=("-beforeMassInput-"), size=(7,1)), sg.InputText(" ", key=("-afterMassInput-"), size=(7,1)), sg.Text("", key=("-massOutput-"), size=(8,1)),
           sg.Text("", key=("-missingEnergyOutput-"), size=(15,1)), sg.Button("Energy"), sg.Button("Mass")],
          [sg.Button("Ok"), sg.Button("Cancel")]]

window = sg.Window("Physics stuff", layout)

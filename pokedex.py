import PySimpleGUI as sg
import requests

def type(input_poke):
    type_list = list()
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + input_poke).json()
    for type in pokemon['types']:
        type_list.append(type['type']['name'])
    return(type_list)

def double_damage_type(input_poke):
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + input_poke).json()
    double_damage_type_list = list()
    for type in pokemon['types']:
        damage_type = requests.get(type['type']['url']).json()
        for double_damage_poke in damage_type['damage_relations']['double_damage_from']:
            double_damage_type_list.append(double_damage_poke['name'])
    return(double_damage_type_list)

def double_damage_poke(input_poke):
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + input_poke).json()
    double_damage_poke_list = list()
    for type in pokemon['types']:
        damage_type = requests.get(type['type']['url']).json()
        for double_damage_poke in damage_type['damage_relations']['double_damage_from']:
            dd_poke = requests.get(double_damage_poke['url']).json()
            for i in range(5):
                double_damage_poke_list.append(dd_poke['pokemon'][i]['pokemon']['name'])
    return(double_damage_poke_list)
    
def ability(input_poke):
    ability_list = list()
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + input_poke).json()
    for ability in pokemon['abilities']:
        ability_list.append(ability['ability']['name'])
    return(ability_list)
    
# Define the window's contents
layout = [[sg.Text("Enter name of pokemon: ")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Pokedex', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello there! Thanks for using Pokedex')
    sg.popup('NAME: ', type(values['-INPUT-']), '\nDOUBLE DAMAGE FROM: ', double_damage_type(values['-INPUT-']), '\nDOUBLE DAMAGE FROM POKEMON LIST: ', double_damage_poke(values['-INPUT-']), '\nABILTIES: ', ability(values['-INPUT-']))

# Finish up by removing from the screen
window.close()

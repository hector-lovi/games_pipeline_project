import pandas as pd
import numpy as np
import time
import random

def firstView():
    games = pd.read_csv('..\\output\\gData.csv')

    print('____INFO____')
    print('.... \n ....')
    print('Este dataset contiene información sobre videojuegos')
    print('¿Cuantos juegos? \nUn total de ' + str(len(games)) + ' videojuegos')
    time.sleep(0.5)
    print('..... \n ....')
    time.sleep(0.5)
    print('¿Qué información voy a poder consultar?')
    time.sleep(0.5)
    print('· Títulos como este -> ' + random.choice(list(games.name)))
    time.sleep(0.25)
    print('· Filtrado por hasta {} géneros de videojuegos'.format(len(games['genre(s)'].unique())))
    time.sleep(0.25)
    print('· Fechas, de {} a {}'.format(games[['year']].min(),games[['year']].max()))
    time.sleep(0.25)
    print('· Múltiples plataformas:\n', games.platform.unique())
    time.sleep(0.25)
    print('· Puntuaciones de metascore o de usuarios')
    time.sleep(0.25)
    print('· Links para más información')

def findName(nombre):
    games = pd.read_csv('..\\output\\gData.csv')
    nombre = nombre.lower()
    
    if nombre not in list(games.name):
        search = nombre[:-1]
        optSearch = games[games['name'].str.contains(search, case=False, na=False)].name.unique()
        
        if not list(optSearch):
            print('Juego no encontrado..')
            
        else:    
            print('No hemos encontrado el juego {}. Prueba con estas opciones similares: '.format(nombre.upper()))
            for option in optSearch:
                print('- ',option)

    else:
        return games[games.name == nombre]

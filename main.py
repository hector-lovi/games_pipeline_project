import argparse
import pandas as pd
from src.cleanData import cleanup as cl
from src.gameInfo import firstView, findName

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = 'Bienvenid@, aquí podrás recopilar información sobre videojuegos')

    parser.add_argument('-n, --name', help = 'Filtra a través del nombre del juego')
    parser.add_argument('-g, --genre', help = 'Filtra la lista por género')
    parser.add_argument('-p, --platform', help = 'Filtra la lista por plataformas')
    parser.add_argument('-y, --year', help = 'Filtra la lista por años', type = int)
    parser.add_argument('--meta', help = 'Filtra la lista por la nota de metacritics', type = float)
    parser.add_argument('--user', help = 'Filtra la lista por la nota de los usuarios', type = float)
    parser.add_argument('--mean', help = 'Filtra la lista por la nota media entre metacritics y usuarios', type = float)
      
    args = parser.parse_args()

    name = args.name
    genre = args.genre
    platform = args.platform
    year = args.year
    meta = args.meta
    user = args.user
    mean = args.mean


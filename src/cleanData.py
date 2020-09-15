import pandas as pd
import numpy as np
import re
import time

# Limpieza de datos

def dropDuplicates(df):
    # eliminar valores duplicados
    df.drop_duplicates(subset=['name', 'platform'], ignore_index=True, inplace=True)
    
    return df

def nullNum(df):
    # comprobar valores nulos
    null = df.isnull().sum()[df.isnull().sum() > 0]
    

def notNull(df):
    # sustituir valores nulos por 'unknown'
    d = {}
    v = 'unknown'
    
    for c,k in enumerate(df.isnull().sum()):
        if k > 0:
            d[df.columns[c]] = v
            
    df.fillna(value = d, inplace=True)
    
    return df

def lower(df, *arg):
    # lower() 'name', 'platform', 'developer', 'publisher', 'genre(s)'
    columns = [c for c in arg]
    
    for c in columns:
        df[c] = [e.lower() for e in df[c]]
    
    return df

def monthYearDecade(df):
    # extraer mes, año y decada
    df['month'] = [re.search(r'\w{3}', m).group() for m in df['release_date']]
    df['year'] = [int(re.search(r'\d{4}', m).group()) for m in df['release_date']]
    df['decade'] = pd.cut(df.year, bins=[1989,1999,2009,2019], labels=range(1990,2020,10))
    
    return df

def link(df):
    # crear links
    domain = 'https://www.metacritic.com'
    df['link'] = domain + df['link']
    
    return df

def toFloat(df):
    # data metascore to float
    df['metascore'] = df['metascore'] / 10
    
    return df

def toNumeric(df):
    # str to numeric
    df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
    df['user_score'] = df['user_score'].replace(np.nan, 0, regex=True)
    
    return df

def createMean(df):
    # crear mean_score
    df['mean_score'] = df[['metascore', 'user_score']].mean(axis=1)
    
    return df

# Clean Dataset
def cleanup(path):
    print('.....\n.....')
    time.sleep(0.5)
    print('.....\n.....')
    time.sleep(0.5)
    print('clean dataset...')
    time.sleep(1)
    print('.....\n.....')
    time.sleep(0.5)
    print('.....\n.....')
    time.sleep(0.5)
    data = pd.read_csv(path)
    data = dropDuplicates(data)
    data = notNull(data)
    data = lower(data, 'name', 'platform', 'genre(s)')
    data = monthYearDecade(data)
    data = link(data)
    data = toFloat(data)
    data = toNumeric(data)
    data = createMean(data)

    data.to_csv('C:\\Users\\heclo\\Data\\projects\\games_pipeline_project\\output\\gData.csv')
    return print('Dataset cleanup!')

cleanup('C:\\Users\\heclo\\Data\\projects\\games_pipeline_project\\input\\metacritic_games.csv')
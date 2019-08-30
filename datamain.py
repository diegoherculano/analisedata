import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

##Extração total
def scrape_stats(base_url, year_start, year_end):
    years = range(year_start,year_end+1,1)

    final_df = pd.DataFrame()

    for year in years:
        print('Extraindo ano {}'.format(year))
        req_url = base_url.format(year)
        req = requests.get(req_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find('table', {'id':'totals_stats'})
        df = pd.read_html(str(table))[0]
        df['Year'] = year
        final_df = final_df.append(df)
    return final_df


url =  'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'
df = scrape_stats(url, 2013, 2018)

##Pega indexes
drop_indexes = df[df['Rk'] =='Rk'].index
df.drop(drop_indexes, inplace=True) #Elima os valores do index passados

numeric_cols = df.columns.drop(['Player', 'Pos', 'Tm'])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

#Outra ordem
#grouped_df = df.groupby('Player', as_index=False).sum()

#Ordena Data Frame
sorted_df = df.sort_values(by=['Age', '3P'], axis=0, ascending=[True, False])
#sorted_df = grouped_df.sort_values(by=['3P'], axis=0, ascending=[False])
print(sorted_df[['Player', 'Age', '3P']].head())

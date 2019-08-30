import pandas as pd
import requests
from bs4 import BeautifulSoup

# Execução do Request GET para obter o conteúdo da página
req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
if req.status_code == 200: # Status 200 indica que a requisição foi completada
    print('Requisição bem sucedida!')
    content = req.content # obtém conteúdo da página


soup = BeautifulSoup(content, 'html.parser')
# Utilizando somente o nome da tag HTML
table = soup.find(name='table')
# Especificando atributos da tag
table = soup.find(name='table', attrs={'id':'totals_stats'})
# Usando find_all
table = soup.find_all(name='table')

# Lendo como Data Frame
table_str = str(table)
df = pd.read_html(table_str)[0]
print(df.head())

# Limpando dados desnecessários
drop_indexes = df[df['Rk'] == 'Rk'].index # Pega indexes onde a coluna 'Rk' possui valor 'Rk'
df.drop(drop_indexes, inplace=True) # elimina os valores dos index passados da tabela

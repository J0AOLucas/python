#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd

path = "https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/01_raw/2020/rodada-3.csv"

df = pd.read_csv(path) #Dados CSV já são dataframe.
df.head()

Existem funções do pandas que fazem a busca de PDF, png, JPG, txt e etc. Não somente csv
UCL datasets é um bom site para buscar dados.
Mesmo que haja várias colunas, o código não vai conseguir imprimir todas.
# In[ ]:





# In[ ]:





# In[44]:


#Só saberei o que significa cada coluna quando eu ver o dicionário de dados
print(df.columns)


# # Exercícios
# 
 2. Exiba os nomes dos atletas e seus respectivos times com preço acuma de 20 cartoetas no dataset em questão
# In[45]:


exe = df[['atletas.nome', 'atletas.clube.id.full.name']] 
exe


# In[48]:


#MELHOR FILTRO

filtro = df['atletas.preco_num'] > 20
jogadores_caros = df[filtro]
jogadores_caros[['atletas.nome', 'atletas.clube.id.full.name']]

3. Exiba a média dos preços dos jogadores
# In[51]:


media = df['atletas.preco_num'].mean()
print(f'{media:.2f}')


# In[ ]:




4. Exiba o nome dos jogadores que mitou/mitaram na rodada(Jogadores com maior quantidade de pontos)
# In[65]:


valor_maximo = df['atletas.pontos_num'].max()
filtro = df['atletas.pontos_num'] >= valor_maximo
mitaram = df[filtro]
mitaram[['atletas.nome', 'atletas.clube.id.full.name']]

Ou
# In[67]:


best = df[['atletas.nome', 'atletas.pontos_num', 'atletas.clube.id.full.name']]
best[best['atletas.pontos_num'] > 20]


# In[ ]:


#Buscando a quantidade de instâncias ou linhas


# In[77]:


filtro = df['atletas.status_id'] == 'Provável'
escalaveis = df[filtro]
escalaveis['atletas.nome'].count()


# In[78]:


#Ou


# In[80]:


filtro = df['atletas.status_id'] == 'Provável'
df[filtro]['atletas.nome'].count()


# In[ ]:






# coding: utf-8

# In[44]:


import numpy as np
import pandas as pd
dataFrame = pd.read_csv('weather.csv').head()


# In[45]:


dataFrame


# In[5]:


#seleciona sempre as colunas
dataFrame['TEMP']


# In[6]:


dataFrameTranspose = dataFrame.T


# In[7]:


dataFrameTranspose


# In[9]:


dataFrameTranspose[2]


# In[10]:


dataFrameTranspose[2]['TIME']


# In[11]:


dtNovo = pd.DataFrame([['Tadeu'],['Gabriel'],['Luis Fernando']], index=[4,3,4])
dtNovo


# In[12]:


dtNovo[0][4]


# In[14]:


dataFrame


# In[15]:


dataFrame[['TEMP', 'PRESSURE']]


# In[16]:


dataFrame['TEMP'][[2,4]]


# In[21]:


#slicing
dataFrame[1:4]



# In[26]:


#slicing
dataFrame[2:4][['TEMP','PRESSURE']]


# In[25]:


dataFrameTranspose


# In[28]:


dataFrameTranspose[3:5]


# In[31]:


#mesmo resultado que Out[26]
dataFrameTranspose[3:5][[2,3]]


# In[32]:


dataFrame['TEMP']


# In[33]:


#dos quatro primeiros
dataFrame['TEMP'][:4]


# In[37]:


dataFrameTranspose['DAY':'TEMP']


# In[38]:



#using ioc and iloc


# In[52]:


capitals = pd.DataFrame(
    [
        ["Ngerulmud",391,1.87],
        ["Vatican City",826,100],
        ["Yaren",1100,10.91],
        ["Funafuti",4492,45.48],
        ["City of San Marino",4493]
    ],
    index=["Palau","Vatican City", "Nauru", "Tuvalu", "San Marino"],
    columns=['Capital','Population','Percentage']
)


# In[54]:


capitals


# In[64]:


#uma única operação
capitals.loc['Nauru','Population']


# In[65]:


#duas operações
capitals['Population']['Nauru']


# In[67]:


#uma unica operação filtrando
capitals.loc['Palau':'Nauru',['Population','Capital']]


# In[71]:


#Select the rows of San Marino and Vatican
#loc funciona apenas como label e não como position (index)
capitals.loc[['San Marino', 'Vatican City']]


# In[73]:


#seleciona o indice 1 e 4 do dataframe
capitals.iloc[[4,1]]


# In[74]:


#seleciona todas colunas exceto a primeiro de capitals
capitals.iloc[[4,1], 1:]


# In[76]:


#retorno as duas primeiras linhas
capitals[[True, True, False, False, False]]


# In[77]:


#retorna apenas as capitais com porcentagme superior a 25
capitals[capitals['Percentage'] > 25]


# In[119]:


grades = pd.DataFrame(
    [
        [10,9],
        [7,8],
        [6,7],
        [6,5],
        [5,2]
    ],
    index = ['Tadeu','Jose Carlos','Maria','Amanda','Sertão'],
    columns=['test_1','test_2']
)


# In[81]:


grades


# In[83]:


#Os estudantes que tiveram uma nota na segunda prova menor ou igual a primeira
grades[grades['test_2'] <= grades['test_1']]


# In[120]:


#adicionei 1 as notas da prova 2 do tadeu e da amanda
grades.loc[['Amanda', 'Tadeu'], 'test_2'] += 1


# In[111]:


grades


# In[112]:


reprovado = grades < 6
aprovado = grades >=6


# In[117]:


grades[reprovado] = "Fail"
grades[aprovado]= "Passou"
grades


# In[121]:


grades = pd.DataFrame(
    [
        [10,9],
        [7,8],
        [6,7],
        [6,5],
        [5,2]
    ],
    index = ['Tadeu','Jose Carlos','Maria','Amanda','Sertão'],
    columns=['test_1','test_2']
)


# In[122]:


grades


# In[123]:


grades.mean(axis=1)


# In[124]:


grades.mean(axis=1) > 6


# In[125]:


grades['passou']=grades.mean(axis=1) > 6


# In[126]:


grades


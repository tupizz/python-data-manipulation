

```python
import numpy as np
import pandas as pd
dataFrame = pd.read_csv('weather.csv').head()
```


```python
dataFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MONTH</th>
      <th>DAY</th>
      <th>TIME</th>
      <th>TEMP</th>
      <th>PRESSURE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>6.8</td>
      <td>10207</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>5.8</td>
      <td>10214</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>5.7</td>
      <td>10220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>6.0</td>
      <td>10225</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>4.5</td>
      <td>10230</td>
    </tr>
  </tbody>
</table>
</div>




```python
#seleciona sempre as colunas
dataFrame['TEMP']
```




    0    6.8
    1    5.8
    2    5.7
    3    6.0
    4    4.5
    Name: TEMP, dtype: float64




```python
dataFrameTranspose = dataFrame.T
```


```python
dataFrameTranspose
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MONTH</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>DAY</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>TIME</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>TEMP</th>
      <td>6.8</td>
      <td>5.8</td>
      <td>5.7</td>
      <td>6.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>PRESSURE</th>
      <td>10207.0</td>
      <td>10214.0</td>
      <td>10220.0</td>
      <td>10225.0</td>
      <td>10230.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataFrameTranspose[2]
```




    MONTH           1.0
    DAY             1.0
    TIME            3.0
    TEMP            5.7
    PRESSURE    10220.0
    Name: 2, dtype: float64




```python
dataFrameTranspose[2]['TIME']
```




    3.0




```python
dtNovo = pd.DataFrame([['Tadeu'],['Gabriel'],['Luis Fernando']], index=[4,3,4])
dtNovo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Tadeu</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Gabriel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Luis Fernando</td>
    </tr>
  </tbody>
</table>
</div>




```python
dtNovo[0][4]

```




    4            Tadeu
    4    Luis Fernando
    Name: 0, dtype: object




```python
dataFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MONTH</th>
      <th>DAY</th>
      <th>TIME</th>
      <th>TEMP</th>
      <th>PRESSURE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>6.8</td>
      <td>10207</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>5.8</td>
      <td>10214</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>5.7</td>
      <td>10220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>6.0</td>
      <td>10225</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>4.5</td>
      <td>10230</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataFrame[['TEMP', 'PRESSURE']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TEMP</th>
      <th>PRESSURE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6.8</td>
      <td>10207</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.8</td>
      <td>10214</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.7</td>
      <td>10220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
      <td>10225</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.5</td>
      <td>10230</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataFrame['TEMP'][[2,4]]
```




    2    5.7
    4    4.5
    Name: TEMP, dtype: float64




```python
#slicing
dataFrame[1:4]


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MONTH</th>
      <th>DAY</th>
      <th>TIME</th>
      <th>TEMP</th>
      <th>PRESSURE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>5.8</td>
      <td>10214</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>5.7</td>
      <td>10220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>6.0</td>
      <td>10225</td>
    </tr>
  </tbody>
</table>
</div>




```python
#slicing
dataFrame[2:4][['TEMP','PRESSURE']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TEMP</th>
      <th>PRESSURE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>5.7</td>
      <td>10220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
      <td>10225</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataFrameTranspose
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MONTH</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>DAY</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>TIME</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>TEMP</th>
      <td>6.8</td>
      <td>5.8</td>
      <td>5.7</td>
      <td>6.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>PRESSURE</th>
      <td>10207.0</td>
      <td>10214.0</td>
      <td>10220.0</td>
      <td>10225.0</td>
      <td>10230.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataFrameTranspose[3:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>TEMP</th>
      <td>6.8</td>
      <td>5.8</td>
      <td>5.7</td>
      <td>6.0</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>PRESSURE</th>
      <td>10207.0</td>
      <td>10214.0</td>
      <td>10220.0</td>
      <td>10225.0</td>
      <td>10230.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#mesmo resultado que Out[26]
dataFrameTranspose[3:5][[2,3]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>TEMP</th>
      <td>5.7</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>PRESSURE</th>
      <td>10220.0</td>
      <td>10225.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataFrame['TEMP']
```




    0    6.8
    1    5.8
    2    5.7
    3    6.0
    4    4.5
    Name: TEMP, dtype: float64




```python
#dos quatro primeiros
dataFrame['TEMP'][:4]
```




    0    6.8
    1    5.8
    2    5.7
    3    6.0
    Name: TEMP, dtype: float64




```python
dataFrameTranspose['DAY':'TEMP']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>DAY</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>TIME</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>TEMP</th>
      <td>6.8</td>
      <td>5.8</td>
      <td>5.7</td>
      <td>6.0</td>
      <td>4.5</td>
    </tr>
  </tbody>
</table>
</div>




```python

#using ioc and iloc

```


```python
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
```


```python
capitals

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capital</th>
      <th>Population</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Palau</th>
      <td>Ngerulmud</td>
      <td>391</td>
      <td>1.87</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>Vatican City</td>
      <td>826</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Nauru</th>
      <td>Yaren</td>
      <td>1100</td>
      <td>10.91</td>
    </tr>
    <tr>
      <th>Tuvalu</th>
      <td>Funafuti</td>
      <td>4492</td>
      <td>45.48</td>
    </tr>
    <tr>
      <th>San Marino</th>
      <td>City of San Marino</td>
      <td>4493</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#uma única operação
capitals.loc['Nauru','Population']
```




    1100




```python
#duas operações
capitals['Population']['Nauru']
```




    1100




```python
#uma unica operação filtrando
capitals.loc['Palau':'Nauru',['Population','Capital']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population</th>
      <th>Capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Palau</th>
      <td>391</td>
      <td>Ngerulmud</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>826</td>
      <td>Vatican City</td>
    </tr>
    <tr>
      <th>Nauru</th>
      <td>1100</td>
      <td>Yaren</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Select the rows of San Marino and Vatican
#loc funciona apenas como label e não como position (index)
capitals.loc[['San Marino', 'Vatican City']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capital</th>
      <th>Population</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>San Marino</th>
      <td>City of San Marino</td>
      <td>4493</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>Vatican City</td>
      <td>826</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#seleciona o indice 1 e 4 do dataframe
capitals.iloc[[4,1]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capital</th>
      <th>Population</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>San Marino</th>
      <td>City of San Marino</td>
      <td>4493</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>Vatican City</td>
      <td>826</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#seleciona todas colunas exceto a primeiro de capitals
capitals.iloc[[4,1], 1:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>San Marino</th>
      <td>4493</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>826</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#retorno as duas primeiras linhas
capitals[[True, True, False, False, False]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capital</th>
      <th>Population</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Palau</th>
      <td>Ngerulmud</td>
      <td>391</td>
      <td>1.87</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>Vatican City</td>
      <td>826</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
#retorna apenas as capitais com porcentagme superior a 25
capitals[capitals['Percentage'] > 25]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Capital</th>
      <th>Population</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Vatican City</th>
      <td>Vatican City</td>
      <td>826</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Tuvalu</th>
      <td>Funafuti</td>
      <td>4492</td>
      <td>45.48</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
grades
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_1</th>
      <th>test_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tadeu</th>
      <td>10</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Jose Carlos</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Maria</th>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Amanda</th>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Sertão</th>
      <td>5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Os estudantes que tiveram uma nota na segunda prova menor ou igual a primeira
grades[grades['test_2'] <= grades['test_1']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_1</th>
      <th>test_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tadeu</th>
      <td>10</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Amanda</th>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Sertão</th>
      <td>5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
#adicionei 1 as notas da prova 2 do tadeu e da amanda
grades.loc[['Amanda', 'Tadeu'], 'test_2'] += 1
```


```python
grades
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_1</th>
      <th>test_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tadeu</th>
      <td>10</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Jose Carlos</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Maria</th>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Amanda</th>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Sertão</th>
      <td>5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
reprovado = grades < 6
aprovado = grades >=6
```


```python
grades[reprovado] = "Fail"
grades[aprovado]= "Passou"
grades
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_1</th>
      <th>test_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tadeu</th>
      <td>Passou</td>
      <td>Passou</td>
    </tr>
    <tr>
      <th>Jose Carlos</th>
      <td>Passou</td>
      <td>Passou</td>
    </tr>
    <tr>
      <th>Maria</th>
      <td>Passou</td>
      <td>Passou</td>
    </tr>
    <tr>
      <th>Amanda</th>
      <td>Passou</td>
      <td>Fail</td>
    </tr>
    <tr>
      <th>Sertão</th>
      <td>Fail</td>
      <td>Fail</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

```


```python
grades
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_1</th>
      <th>test_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tadeu</th>
      <td>10</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Jose Carlos</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Maria</th>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Amanda</th>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Sertão</th>
      <td>5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
grades.mean(axis=1)
```




    Tadeu          9.5
    Jose Carlos    7.5
    Maria          6.5
    Amanda         5.5
    Sertão         3.5
    dtype: float64




```python
grades.mean(axis=1) > 6
```




    Tadeu           True
    Jose Carlos     True
    Maria           True
    Amanda         False
    Sertão         False
    dtype: bool




```python
grades['passou']=grades.mean(axis=1) > 6
```


```python
grades
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>test_1</th>
      <th>test_2</th>
      <th>passou</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tadeu</th>
      <td>10</td>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Jose Carlos</th>
      <td>7</td>
      <td>8</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Maria</th>
      <td>6</td>
      <td>7</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Amanda</th>
      <td>6</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Sertão</th>
      <td>5</td>
      <td>2</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



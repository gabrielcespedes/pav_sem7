import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

def calidad_datos(datos):
  tipos = pd.DataFrame(datos.dtypes, columns = ['tipo'])
  nan = pd.DataFrame(datos.isna().sum(), columns = ['nan'])
  nan_prop = pd.DataFrame(datos.isna().sum()/datos.shape[0]*100, columns = ['porcentaje_nan'])  
  ceros = pd.DataFrame([datos.loc[datos[col] == 0, col].shape[0]  for col in datos.columns], \
                       columns = ['ceros'], index = datos.columns)
  ceros_prop = pd.DataFrame([datos.loc[datos[col] == 0, col].shape[0]/datos.shape[0]*100  for col in datos.columns],\
                       columns = ['porcentaje_ceros'], index = datos.columns)
  
  resumen = datos.describe(include = 'all').T
  resumen['IQR'] = resumen['75%'] - resumen['25%']
  resumen['lim_inf'] = resumen['25%'] - resumen['IQR']*1.5
  resumen['lim_sup'] = resumen['75%'] + resumen['IQR']*1.5

  resumen['atipicos'] = datos.apply(lambda x: sum(np.where((x < resumen['lim_inf'][x.name]) | (x > resumen['lim_sup'][x.name]), 1, 0)) \
                                    if x.name in resumen['lim_inf'].dropna().index else 0)
  
  return pd.concat([tipos, nan, nan_prop, ceros, ceros_prop, resumen], axis = 1).sort_values('tipo')

def graficos(calidad, datos, cols):
  num_cols = len(cols)
  num_rows = (num_cols + 2) // 3
  plt.figure(figsize = (15, 3 * num_rows))
  for n, i in enumerate(cols):
    plt.subplot(num_rows, 3, n+1)
    if calidad.loc[i, 'tipo'] == 'object':
      sns.countplot(y = datos[i], order = datos[i].value_counts().iloc[:16].index)
      plt.title(f'Frecuencias para {i}')
      plt.tight_layout()
    else:
      sns.distplot(datos[i])
      plt.title(f'Distribución para {i}')
      plt.tight_layout()



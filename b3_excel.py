import matplotlib.pyplot as fig
import statistics as st
import numpy as ny
import xlrd3
import scipy.stats as sci
from scipy.stats import norm

wb = xlrd3.open_workbook('B3.xlsx')
plan = wb.sheet_by_name("IBOV")
lin = plan.nrows
col = plan.ncols

dados = []

for i in range (col):
    coluna = plan.col_values(i)
    dados.append(coluna)

dias = ny.arange(lin)
dados = ny.array(dados)
retorno = (dados[1,1:lin] - dados[1,0:lin-1])/dados[1,0:lin-1]
print(retorno)
print(dias)
print(dados)

fig.subplot(221)
fig.plot(dias, dados[1], color='black')
fig.xlabel('dias')
fig.title('IBOV - COTAÇÃO DIÁRIA')

fig.subplot(222)
fig.plot(dias[1:], retorno, color='black')
fig.xlabel('dias')
fig.title('RETORNO DIÁRIO IBOV')

fig.subplot(223)
fig.hist(retorno,bins=20,color='yellow',density=True)
fig.xlabel('Classes')
fig.ylabel('Frequências')
fig.title('Histograma dos Retornos')
xmin, xmax= fig.xlim()
media= st.mean(retorno)
desvio=st.pstdev(retorno)
eixo_x = ny.linspace(xmin,xmax, 100)
eixo_y=norm.pdf(eixo_x,media, desvio)
fig.plot(eixo_x,eixo_y, color='black')

fig.subplot(224)
sci.probplot(retorno,dist="norm", plot=fig)
fig.title('Caudas de Distribuição - IBOV')
fig.ylabel('Valores Ordenados')
fig.xlabel('Quantis Teóricos')

fig.show()


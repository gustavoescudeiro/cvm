import pandas as pd
import wget
from zipfile import ZipFile
import os

url_base = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/'

arquivos_zip = []
for ano in range(2011,2022):
    arquivos_zip.append(f'itr_cia_aberta_{ano}.zip')
arquivos_zip

for arq in arquivos_zip:
    wget.download(url_base+arq)

for arq in arquivos_zip:
    ZipFile(arq, 'r').extractall('CVM')

nomes = ['BPA_con', 'BPA_ind', 'BPP_con', 'BPP_ind',
         'DFC_MD_con', 'DFC_MD_ind', 'DFC_MI_con',
         'DFC_MI_ind', 'DMPL_con', 'DMPL_ind', 'DRE_con',
        'DRE_ind', 'DVA_con', 'DVA_ind']

cwd = os.getcwd() # diretorio atual
for nome in nomes:
    arquivo = pd.DataFrame()
    for ano in range(2011,2022):
        arquivo = pd.concat([arquivo, pd.read_csv(cwd+f'\\CVm\\itr_cia_aberta_{nome}_{ano}.csv', sep = ';',decimal = ',', encoding = 'ISO-8859-1')])
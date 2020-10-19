import os
from params import *

def createFilesFolder():

    if not os.path.exists(filesFolderName):
        os.makedirs(filesFolderName)

    for mutacao in mutacaoArray:
        for cruzamento in cruzamentoArray:
            for populacao in populacaoArray:
                for geracoes in geracoesArray:
                    
                    path = f'files/{mutacao}-{cruzamento}-{populacao}-{geracoes}'

                    if not os.path.exists(path):
                        os.makedirs(path)
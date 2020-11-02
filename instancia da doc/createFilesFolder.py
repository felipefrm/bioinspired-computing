import os
import shutil
from params import *

def createFilesFolder():

    if os.path.exists(filesFolderName):
        shutil.rmtree(filesFolderName)
    os.makedirs(filesFolderName)

    for mutacao in mutacaoArray:
        for cruzamento in cruzamentoArray:
            for populacao in populacaoArray:
                for geracoes in geracoesArray:
                    
                    path = f'{filesFolderName}/{mutacao}-{cruzamento}-{populacao}-{geracoes}'
                    os.makedirs(path)
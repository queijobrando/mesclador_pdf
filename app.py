import PyPDF2 
import os

ferramenta = PyPDF2.PdfMerger()

lista_arquivos = os.listdir('arquivos')
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf":
        ferramenta.append(f"arquivos/{arquivo}")

ferramenta.write("arquivo_pronto/PDF Final.pdf")

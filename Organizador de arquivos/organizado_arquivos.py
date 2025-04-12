import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
print(caminho)

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locals = {
    "imagens": [".png", ".jpg", ".jpeg", ".svg", ".webp"],
    "Videos": [".mp4"],
    "Executaveis":[".exe"],
    "Planinhas":[".xlsx"],
    "Pdfs":[".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locals:
        if extensao in locals[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

# model/csv_model.py
import pandas as pd

def tentar_codificacoes(caminho_arquivo, codificacoes=['utf-8', 'latin1', 'cp1252', 'ISO-8859-1', 'utf-8-sig']):
    for cod in codificacoes:
        try:
            df = pd.read_csv(caminho_arquivo, encoding=cod)
            return df, cod
        except Exception:
            continue
    raise RuntimeError("Nenhuma codificação funcionou para ler o arquivo.")

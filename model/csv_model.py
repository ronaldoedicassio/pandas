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

def remover_ultima_linha_em_branco(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove a última linha do DataFrame se ela estiver completamente vazia.
    """
    if df is not None and not df.empty:
        if df.tail(1).isnull().all(axis=1).bool():
            return df.iloc[:-1]
    return df 
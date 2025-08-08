# controller/csv_controller.py
import os
import pandas as pd
from model.csv_model import tentar_codificacoes
from view.csv_view import mostrar_codificacao, mostrar_dataframe, mostrar_erro

def processar_csv(caminho_arquivo):
    try:
        df_novo, codificacao_usada = tentar_codificacoes(caminho_arquivo)
        mostrar_codificacao(codificacao_usada, 1.0)
        mostrar_dataframe(df_novo)

        # Nome do arquivo UTF-8
        nome_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
        caminho_utf8 = f"{nome_base}_utf8.csv"

        # Verifica se já existe
        if os.path.exists(caminho_utf8):
            print(f"📂 Arquivo UTF-8 já existe: {caminho_utf8}")
            df_existente = pd.read_csv(caminho_utf8, encoding='utf-8')

            # Junta os dados (sem duplicar)
            df_combinado = pd.concat([df_existente, df_novo], ignore_index=True)

            # Remove duplicatas se quiser (opcional)
            df_combinado.drop_duplicates(inplace=True)

            # Salva tudo novamente
            df_combinado.to_csv(caminho_utf8, index=False, encoding='utf-8')
            print(f"✅ Dados adicionados ao final de: {caminho_utf8}")
        else:
            # Remover linhas em branco das linhas duplicadas que não serão salvas
            df = df.dropna(how='all')
            # Salva novo arquivo
            df_novo.to_csv(caminho_utf8, index=False, encoding='utf-8')
            print(f"✅ Arquivo salvo como UTF-8: {caminho_utf8}")

    except RuntimeError as e:
        mostrar_erro(str(e))
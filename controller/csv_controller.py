# controller/csv_controller.py
import os
import pandas as pd
from model.csv_model import remover_ultima_linha_em_branco, tentar_codificacoes
from view.csv_view import mostrar_codificacao, mostrar_dataframe, mostrar_erro

def processar_csv(caminho_arquivo):
    try:
        df_novo, codificacao_usada = tentar_codificacoes(caminho_arquivo)
        mostrar_codificacao(codificacao_usada, 1.0)
        mostrar_dataframe(df_novo)

        # Nome do arquivo utf-8-sig
        nome_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
        caminho_utf8 = f"{nome_base}_utf8.csv"

        # Verifica se já existe
        if os.path.exists(caminho_utf8):
            print(f"📂 Arquivo utf-8-sig já existe: {caminho_utf8}")
            df_existente = pd.read_csv(caminho_utf8, encoding='utf-8-sig')

            # Junta os dados (sem duplicar)
            df_combinado = pd.concat([df_existente, df_novo], ignore_index=True)

            # Remove duplicatas se quiser (opcional)
            df_combinado.drop_duplicates(inplace=True)

            # Remover linhas em branco das linhas duplicadas que não serão salvas
            df_combinado = df_combinado.dropna(how='all')

            # Remove a última linha em branco se existir
            df_combinado = remover_ultima_linha_em_branco(df_combinado)

            # Salva tudo novamente
            df_combinado.to_csv(caminho_utf8, index=False, encoding='utf-8-sig')
            print(f"✅ Dados adicionados ao final de: {caminho_utf8}")
        else:
            # Remove duplicatas se quiser (opcional)
            df_novo.drop_duplicates(inplace=True)

            # Remover linhas em branco das linhas duplicadas que não serão salvas
            df_novo = df_novo.dropna(how='all')

            # Salva novo arquivo
            df_novo.to_csv(caminho_utf8, index=False, encoding='utf-8-sig')
            print(f"✅ Arquivo salvo como utf-8-sig: {caminho_utf8}")

    except RuntimeError as e:
        mostrar_erro(str(e))
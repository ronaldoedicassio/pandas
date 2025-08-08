# view/csv_view.py
def mostrar_codificacao(codificacao, confianca):
    print(f"Codificação detectada: {codificacao} (confiança: {confianca:.2f})")

def mostrar_dataframe(df):
    print("Primeiras linhas do arquivo:")
    print(df.head())

def mostrar_erro(mensagem):
    print(f"❌ {mensagem}")

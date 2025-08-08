# main.py
from controller.csv_controller import processar_csv

if __name__ == "__main__":
    caminho = 'data.csv'  # substitua pelo caminho real
    processar_csv(caminho)

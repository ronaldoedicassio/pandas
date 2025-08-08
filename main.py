# main.py
from controller.csv_controller import processar_csv

if __name__ == "__main__":
    caminho = 'data.csv'  
    processar_csv(caminho)

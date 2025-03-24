# processa_dados.py
import pandas as pd
import os
from datetime import datetime

def processar_dados():
    """
    Processa os dados brutos de vendas.
    Agrega dados por categoria, região e calcula métricas.
    """
    print("Processando dados...")
    
    # Verificar se o arquivo existe
    if not os.path.exists("dados_brutos/vendas.csv"):
        print("Erro: Arquivo de dados brutos não encontrado!")
        return
    
    # Carregar dados brutos
    df = pd.read_csv("dados_brutos/vendas.csv")
    
    # Converter coluna de data para datetime
    df['data'] = pd.to_datetime(df['data'])
    
    # Criar dados agregados por categoria
    df_categoria = df.groupby("categoria").agg({
        "valor_total": "sum",
        "quantidade": "sum",
        "produto": "count"
    }).reset_index()
    df_categoria.rename(columns={"produto": "num_vendas"}, inplace=True)
    
    # Criar dados agregados por região
    df_regiao = df.groupby("regiao").agg({
        "valor_total": "sum",
        "quantidade": "sum",
        "produto": "count"
    }).reset_index()
    df_regiao.rename(columns={"produto": "num_vendas"}, inplace=True)
    
    # Criar dados agregados por dia
    df['dia'] = df['data'].dt.date
    df_diario = df.groupby("dia").agg({
        "valor_total": "sum",
        "quantidade": "sum",
        "produto": "count"
    }).reset_index()
    df_diario.rename(columns={"produto": "num_vendas"}, inplace=True)
    
    # Criar pasta para dados processados
    os.makedirs("dados_processados", exist_ok=True)
    
    # Salvar dados processados
    df_categoria.to_csv("dados_processados/vendas_por_categoria.csv", index=False)
    df_regiao.to_csv("dados_processados/vendas_por_regiao.csv", index=False)
    df_diario.to_csv("dados_processados/vendas_por_dia.csv", index=False)
    
    print("Dados processados com sucesso!")

if __name__ == "__main__":
    processar_dados()
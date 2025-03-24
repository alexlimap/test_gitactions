# gera_relatorio.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def gerar_relatorio():
    """
    Gera relatórios e visualizações a partir dos dados processados.
    Cria gráficos e um relatório de resumo em texto.
    """
    print("Gerando relatório...")
    
    # Verificar se os arquivos existem
    arquivos_requeridos = [
        "dados_processados/vendas_por_categoria.csv",
        "dados_processados/vendas_por_regiao.csv",
        "dados_processados/vendas_por_dia.csv"
    ]
    
    for arquivo in arquivos_requeridos:
        if not os.path.exists(arquivo):
            print(f"Erro: Arquivo {arquivo} não encontrado!")
            return
    
    # Carregar dados processados
    df_categoria = pd.read_csv("dados_processados/vendas_por_categoria.csv")
    df_regiao = pd.read_csv("dados_processados/vendas_por_regiao.csv")
    df_diario = pd.read_csv("dados_processados/vendas_por_dia.csv")
    df_diario['dia'] = pd.to_datetime(df_diario['dia'])
    
    # Criar pasta para relatórios
    os.makedirs("relatorios", exist_ok=True)
    
    # Figura 1: Vendas por categoria
    plt.figure(figsize=(12, 6))
    plt.bar(df_categoria["categoria"], df_categoria["valor_total"])
    plt.title("Vendas por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor Total (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("relatorios/vendas_por_categoria.png")
    plt.close()
    
    # Figura 2: Top 5 regiões
    top_regioes = df_regiao.sort_values("valor_total", ascending=False).head(5)
    plt.figure(figsize=(12, 6))
    plt.bar(top_regioes["regiao"], top_regioes["valor_total"])
    plt.title("Top 5 Regiões por Vendas")
    plt.xlabel("Região")
    plt.ylabel("Valor Total (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("relatorios/top_regioes.png")
    plt.close()
    
    # Figura 3: Vendas diárias
    plt.figure(figsize=(12, 6))
    plt.plot(df_diario["dia"], df_diario["valor_total"])
    plt.title("Vendas Diárias")
    plt.xlabel("Data")
    plt.ylabel("Valor Total (R$)")
    plt.tight_layout()
    plt.savefig("relatorios/vendas_diarias.png")
    plt.close()
    
    # Gerar relatório de texto
    data_relatorio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open("relatorios/resumo_vendas.txt", "w") as f:
        f.write(f"RELATÓRIO DE VENDAS - Gerado em {data_relatorio}\n")
        f.write("="*50 + "\n\n")
        
        f.write("RESUMO GERAL\n")
        f.write("-"*30 + "\n")
        f.write(f"Total de vendas: {df_categoria['num_vendas'].sum()}\n")
        f.write(f"Quantidade total de itens: {df_categoria['quantidade'].sum()}\n")
        f.write(f"Valor total: R$ {df_categoria['valor_total'].sum():.2f}\n\n")
        
        f.write("POR CATEGORIA\n")
        f.write("-"*30 + "\n")
        for _, row in df_categoria.iterrows():
            f.write(f"{row['categoria']}: R$ {row['valor_total']:.2f} ({row['num_vendas']} vendas)\n")
        
        f.write("\nTOP 5 REGIÕES\n")
        f.write("-"*30 + "\n")
        for _, row in top_regioes.iterrows():
            f.write(f"{row['regiao']}: R$ {row['valor_total']:.2f} ({row['num_vendas']} vendas)\n")
    
    print("Relatório gerado com sucesso!")
    print(f"Arquivos de relatório salvos na pasta 'relatorios/'")

if __name__ == "__main__":
    gerar_relatorio()
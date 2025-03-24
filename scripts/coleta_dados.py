# coleta_dados.py
import pandas as pd
from faker import Faker
import os
import random

def coletar_dados():
    """
    Coleta dados simulados usando a biblioteca Faker.
    Gera dados de vendas fictícios com produtos, quantidades e valores.
    """
    print("Coletando dados simulados...")
    
    # Inicializar o Faker
    fake = Faker('pt_BR')
    
    # Criar lista de produtos fictícios
    produtos = [
        "Notebook", "Smartphone", "Tablet", "Monitor", 
        "Teclado", "Mouse", "Headset", "Webcam", 
        "Impressora", "Roteador"
    ]
    
    # Gerar dados de vendas fictícios
    dados = []
    for _ in range(1000):  # Criar 1000 registros
        produto = random.choice(produtos)
        quantidade = random.randint(1, 10)
        preco_unitario = round(random.uniform(50, 5000), 2)
        
        dados.append({
            "data": fake.date_between(start_date="-30d", end_date="today"),
            "produto": produto,
            "categoria": fake.word(ext_word_list=["Eletrônicos", "Informática", "Acessórios", "Periféricos"]),
            "vendedor": fake.name(),
            "regiao": fake.state(),
            "quantidade": quantidade,
            "preco_unitario": preco_unitario,
            "valor_total": quantidade * preco_unitario
        })
    
    # Converter para DataFrame
    df = pd.DataFrame(dados)
    
    # Salvar os dados brutos
    os.makedirs("dados_brutos", exist_ok=True)
    df.to_csv("dados_brutos/vendas.csv", index=False)
    
    print(f"Dados coletados com sucesso! {len(df)} registros gerados.")


if __name__ == "__main__":
    coletar_dados()

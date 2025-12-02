import re
import pandas as pd

print("INICIANDO ANÁLISE LUADELI")
try:
    with open('conversa_whatsapp.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    exit()
padrao_regex = r'^(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([^:]+): (.+)$' 
dados_extraidos = [] 

for linha in linhas:
    match = re.match(padrao_regex, linha)
    if match:
        data, hora, autor, mensagem = match.groups()
        if autor != "Luadeli":
            dados_extraidos.append({
                "Hora": hora,
                "Autor": autor,
                "Mensagem": mensagem.lower()
            })

df = pd.DataFrame(dados_extraidos) #df significa DataFrame (tabela dos dados) Seria tipo uma matriz ou vetor de struct no C (acredito)

df['Hora_Cheia'] = df['Hora'].str[:2] #limpeza da hora quebrada, deixei o horário cheio para agrupar
picos_de_horario = df['Hora_Cheia'].value_counts().sort_index() 

# Produtos (Catálogo)
texto_completo = " ".join(df['Mensagem']) # As aspas são um espaço em branco 
#entre uma mensagem e outra eu pedi que colocasse um espaço em branco para as palavras não grudarem e ficar em um texto horizontal unico


#Precisei especificar os sabores dos cookies para que o resultado não some cookie como uma coisa só 
produtos_alvo = {
    'Cookie de Pistache': 'pistache',
    'Cookie Kinder Bueno': 'kinder',
    'Cookie Red Velvet': 'red velvet',
    'Brownie': 'brownie',
    'Banoffee': 'banoffee',
    'Pavê': 'pavê',
    'Cookie Tradicional': 'tradicional'
}

ranking_produtos = {}
for produto, sabor in produtos_alvo.items():
    ranking_produtos[produto] = texto_completo.count(sabor)


ranking_ordenado = dict(sorted(ranking_produtos.items(), key=lambda item: item[1], reverse=True)) # Ordena do maior para o menor

top_clientes = df['Autor'].value_counts().head(3) # o .value_counts() é um algoritmo de ordenação como em C - Ele agrupa, ordena do maior para o menor e depois devolve uma lista mais organizada


termos_pagamento = {
    'Pix': 'pix',
    'Cartão (Geral)': 'cartao',     
    'Cartão de Crédito': 'credito', 
    'Cartão de Débito': 'debito',   
    'Dinheiro': 'dinheiro'
}
analise_pagamento = {}
for forma_pagamento, palavra_chave in termos_pagamento.items():
    analise_pagamento[forma_pagamento] = texto_completo.count(palavra_chave)

total_cartao_geral = analise_pagamento['Cartão (Geral)']
total_especificos = analise_pagamento['Cartão de Crédito'] + analise_pagamento['Cartão de Débito']
analise_pagamento['Cartão (Geral)'] = total_cartao_geral - total_especificos

print(f"\n>> TOTAL DE MENSAGENS ANALISADAS: {len(df)}")

print("\n>> DEMANDA POR HORARIO:")
print(picos_de_horario)

print("\n>> CLIENTES VIP (RECORRENCIA):")
print(top_clientes)

print(f"\n>> RANKING DE PRODUTOS:")
for produto, qtd in ranking_ordenado.items():
    if qtd > 0:
        print(f"- {produto}: {qtd} pedidos")

print(f"\n>> PREFERENCIA DE PAGAMENTO:")
for forma, qtd in analise_pagamento.items():
    if qtd > 0:
        print(f"- {forma}: {qtd} mencionados")

# Insights
if not picos_de_horario.empty and ranking_ordenado and not top_clientes.empty:
    
    melhor_hora = picos_de_horario.idxmax()
    produto_campeao = list(ranking_ordenado.keys())[0]
    cliente_vip_nome = top_clientes.index[0]
    cliente_vip_qtd = top_clientes.values[0]
   
    print(f"="*40)
    print(f"INSIGHTS DAS VENDAS DE NOVEMBRO")
    print(f"="*40)
    print(f"1. TIMING: O pico de vendas acontece as {melhor_hora}h. Postar 30min antes.")
    print(f"2. OFERTA: O carro-chefe e '{produto_campeao}'.")
    print(f"3. FIDELIDADE: O '{cliente_vip_nome}' comprou {cliente_vip_qtd} vezes. Enviar brinde!")
    print(f"4. CHECKOUT: {sum(analise_pagamento.values())} clientes perguntaram sobre pagamento. Facilitar chave Pix na Bio.")
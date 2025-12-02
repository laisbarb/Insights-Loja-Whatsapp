# 🍪 Luadeli Analytics - WhatsApp Sales Intelligence

> **Projeto de Inteligência de Dados desenvolvido para otimizar a performance de vendas de uma doceria delivery.**

## 🎯 O Desafio de Negócio
A **Luadeli** é uma loja de doces que opera 100% via WhatsApp e Instagram, sem e-commerce estruturado.
**O problema:** Como tomar decisões baseadas em dados (*Data Driven*) se todas as vendas ocorrem em conversas informais de chat, sem métricas claras?

## 💡 A Solução
Desenvolvi um script em **Python** que realiza a mineração de dados (*Data Mining*) dos logs de conversa. O algoritmo transforma texto não estruturado em inteligência estratégica.

**O script responde automaticamente a 4 perguntas vitais:**
1.  ⏰ **Timing:** Qual o melhor horário para postar no Instagram? (Análise de Demanda)
2.  🍪 **Produto:** Qual sabor é o carro-chefe da semana? (Análise de Palavras-Chave)
3.  💎 **CRM:** Quem são os clientes mais fiéis? (Análise de Recorrência/LTV)
4.  💳 **Fricção:** Quais as principais dúvidas no checkout? (Análise de Pagamentos)

## 📊 Principais Insights Gerados
Ao rodar o script com os dados do mês (simulados), identificamos oportunidades claras de **Otimização de Performance**:

* **Horário de Ouro:** O pico de demanda ocorre às **18h**. A estratégia definida foi antecipar as postagens para 17:30h.
* **Trend Alert:** O termo **"Pistache"** superou os sabores tradicionais em volume de busca, indicando uma tendência de consumo.
* **Fidelização:** Identificamos clientes com mais de 5 compras recorrentes para envio de brindes estratégicos.

## 🛠 Stack Tecnológica
* **Python 3.x**
* **Pandas** (Manipulação, Limpeza e Análise de Dados)

## 🔒 Nota sobre Privacidade e LGPD
Este projeto foi desenvolvido utilizando **Dados Sintéticos** (Fictícios).
Embora o script seja funcional para dados reais, optei por simular o dataset para preservar integralmente a privacidade dos clientes e respeitar as normas da **LGPD** (Lei Geral de Proteção de Dados).

---
### 🚀 Como executar o projeto
1. Clone o repositório.
2. Instale a dependência: `pip install pandas`
3. Execute o script: `python analise_whatsapp.py`
4. O relatório estratégico será gerado no terminal.

---
*Desenvolvido por Laís*

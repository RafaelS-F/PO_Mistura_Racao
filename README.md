# PO_Mistura_Racao

# Otimização de Ração Animal (Blending Problem)

Este repositório contém a implementação de um modelo de **Programação Linear (PL)** para resolver o clássico "Problema da Mistura". O objetivo é minimizar o custo de produção de uma ração para frangos de corte, garantindo que todas as exigências nutricionais sejam atendidas.

## Sobre o Projeto

A formulação de rações representa cerca de 70% dos custos na avicultura. Este projeto utiliza otimização matemática para decidir a proporção exata de quatro ingredientes (Milho, Farelo de Soja, Calcário e Óleo de Soja) para criar uma mistura que seja:
1. **Economicamente viável** (Menor custo possível).
2. **Nutricionalmente completa** (Atende aos requisitos de Proteína, Energia e Cálcio).

## Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Biblioteca de Otimização:** [PuLP](https://coin-or.github.io/pulp/)
*   **Tipo de Modelo:** Programação Linear Contínua

## Descrição do Modelo Matemático

### Variáveis de Decisão
*   $x_1$: Proporção de Milho
*   $x_2$: Proporção de Farelo de Soja
*   $x_3$: Proporção de Calcário
*   $x_4$: Proporção de Óleo de Soja

### Função Objetivo
Minimizar $Z = \sum (Custo_i \times x_i)$

### Restrições Principais 
1.  **Nutricionais:** Limites mínimos de Proteína Bruta (20%), Energia Metabolizável (3000 Kcal) e Cálcio (0.9%).
2.  **Balanço de Massa:** A soma das proporções deve ser igual a 100% (1 kg).
3.  **Não-negatividade:** Não é possível ter quantidades negativas de ingredientes.

## Como Executar

### Pré-requisitos
Você precisará ter o Python instalado em sua máquina.

### Instalação
Instale a biblioteca `PuLP` via pip:
pip install pulp


### Rodando o Código
Clone este repositório ou baixe o arquivo PO.py e execute no terminal:
python PO.py

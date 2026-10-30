# 📦 Calculadora de Quebra de Pallets

Programa desenvolvido em **Python** para facilitar o cálculo da quantidade total de unidades em uma quebra de pallets, considerando a quantidade de panos e caixas informadas pelo usuário.

O projeto foi criado como uma prática de programação em Python, utilizando conceitos básicos e intermediários da linguagem, como **funções, loops, tratamento de exceções, entrada de dados e utilização de bibliotecas externas**.

## 🚀 Funcionalidades

* 📦 Calcula a quantidade de unidades provenientes dos pallets.
* 📋 Calcula a quantidade de unidades provenientes das caixas.
* 🧮 Exibe o cálculo detalhado.
* 🔄 Permite realizar vários cálculos sem reiniciar o programa.
* ⚠️ Valida entradas numéricas e informa quando o usuário digita um valor inválido.
* 🎨 Utiliza cores no terminal para melhorar a visualização.
* 🧹 Limpa a tela automaticamente durante a utilização.

## 📐 Como funciona

O programa utiliza dois fatores de conversão:

```text
1 pallet = 280 unidades
1 caixa = 20 unidades
```

O cálculo realizado é:

```text
Panos = quantidade de pallets × 280

Caixas = quantidade de caixas × 20

Total = Panos + Caixas
```

### Exemplo

Se forem informados:

```text
Pallets: 3
Caixas: 5
```

O programa calcula:

```text
3 × 280 = 840 unidades
5 × 20  = 100 unidades

Total geral = 940 unidades
```

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Colorama**

Bibliotecas utilizadas no projeto:

```python
import os
from colorama import Back, Fore, init
```

## 📋 Pré-requisitos

Para executar o programa, é necessário ter o **Python 3** instalado.

Também é necessário instalar a biblioteca `colorama`:

```bash
pip install colorama
```

## ▶️ Como executar

Clone o repositório:

```bash
git clone  https://github.com/hudsondfonseca/calculadora-quebra-pallets.git

Entre na pasta do projeto:

```bash
cd NOME-DO-REPOSITORIO
```

Execute o programa:

```bash
python main.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 main.py
```

## 📂 Estrutura do projeto

```text
calculadora-quebra-pallets/
│
├── main.py
├── README.md
└── requirements.txt
```

## 📦 requirements.txt

O arquivo `requirements.txt` pode conter:

```text
colorama
```

Para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

## 🧠 Conceitos de Python praticados

Este projeto foi desenvolvido como exercício prático para trabalhar conceitos fundamentais da linguagem:

* Variáveis
* Constantes
* Tipos `int` e `str`
* Entrada de dados com `input()`
* Saída de dados com `print()`
* Operações matemáticas
* Estruturas condicionais
* Loops com `while`
* `break` e `continue`
* Funções
* Tratamento de exceções com `try/except`
* F-strings
* Importação de módulos
* Utilização de bibliotecas externas

## 🔮 Possíveis melhorias futuras

Algumas melhorias que podem ser adicionadas ao projeto:

* [ ] Permitir alterar os fatores de conversão.
* [ ] Criar uma interface gráfica.
* [ ] Salvar o histórico dos cálculos.
* [ ] Exportar resultados para um arquivo.
* [ ] Adicionar validação para valores negativos.
* [ ] Criar testes automatizados.
* [ ] Separar a lógica de cálculo da interface do terminal.
* [ ] Criar uma versão web da aplicação.

## 👨‍💻 Objetivo

Este projeto faz parte da minha jornada de aprendizado em **Python e desenvolvimento de software**, servindo como prática para transformar uma necessidade simples do dia a dia em uma aplicação funcional.

---

**Desenvolvido com Python 🐍**

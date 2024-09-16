# VC-X Solutions - Desafio de Código

[**VC-X Solutions**](https://vcx.solutions/) é uma startup do Grupo Senior Sistemas, sediada em
Florianópolis, SC. Nascemos com o propósito de impactar positivamente o mercado e entregar
facilidades em meio a processos complexos. Hoje, oferecemos uma plataforma completa — VC-X Sonar —
que já ajudou centenas de empresas a descomplicar a telecom e TI. E quer saber? Estamos só começando
e vamos revolucionar o mercado, oferecendo soluções cada vez mais automatizadas, conectadas e
eficientes.

Nossa equipe é formada por desenvolvedores apaixonados e comprometidos com a excelência. Priorizamos processos ágeis e as melhores práticas do mercado, criando um ambiente de trabalho ideal para profissionais que se dedicam ao que fazem.

## 1. Objetivo

Este repositório contém um desafio usado para avaliar as habilidades dos candidatos no
desenvolvimento do backend.

É importante notar que resolver o problema de forma satisfatória é apenas uma parte da avaliação.
Também consideramos outras disciplinas de programação, como documentação, testes, histórico de
commits e melhores práticas de codificação.

## 2. Como Participar

2.1. Leia atentamente as especificações para entender completamente o problema e todos os requisitos antes de começar;

2.2. **Faça um fork deste repositório** no Github. Se você não puder criar um fork público, crie um repositório privado e conceda acesso de leitura aos seguintes usuários:

- `gustavo.rosa@vcx.solutions`;

- `hugo.santos@vcx.solutions`.

## 3. Especificação

Você deve implementar uma aplicação para gerenciar dados de livros e autores. Esta aplicação deve
fornecer uma API REST HTTP que atenda aos seguintes requisitos:

### 3.1. Receber um arquivo CSV com autores e importar os dados para o banco de dados

Dado um arquivo CSV contendo vários autores (potencialmente mais de um milhão), crie um comando para
importar esses dados para o banco de dados. O arquivo CSV terá o seguinte formato:

```csv
nome
Luciano Ramalho
Osvaldo Santana Neto
David Beazley
Chetan Giridhar
Brian K. Jones
J.K. Rowling
```

Cada registro de autor no banco de dados deve incluir os seguintes campos:

- id (gerado automaticamente);
- nome.

Você precisará armazenar os dados dos autores para complementar os dados dos livros que serão
armazenados posteriormente (veja o item #3).

### 3.2. Expor dados dos autores através de um endpoint

Crie um endpoint que retorne uma lista de autores. Opcionalmente, permita a busca de autores pelo
nome.

### 3.3. Operações de CRUD (Create, Read, Update, Delete) para Livros

Implemente as seguintes ações na sua API:

- Criar um livro;

- Ler detalhes de um livro;

- Atualizar detalhes de um livro;

- Excluir um livro.

Cada registro de livro deve conter os seguintes campos:

- id (gerado automaticamente);

- nome;

- edição;

- ano de publicação;

- autores (um livro pode ter vários autores).

Para recuperar os dados de um livro, deve ser possível filtrar pelos seguintes campos
(individualmente ou em combinação):

- nome;

- ano de publicação;

- edição;

- autor.

> Esses filtros são opcionais, deve ser possível navegar por todos os registros de livros sem nenhum filtro.

Para criar um livro, use o seguinte payload JSON:

```json
{
 "nome": "Nome do Livro",
 "edição": 1,
 "ano de publicação": 2021,
 "autores": [1, 2, 3]
}
```

## 4. Requisitos do Projeto

- A aplicação deve ser escrita em Python usando o framework Django;

- Use Python 3.11 ou superior;

- Siga as diretrizes de estilo de código PEP-8;

- Certifique-se de que variáveis, código e strings estejam todos em inglês;

- Inclua a documentação do projeto com:

    - Uma breve descrição;

    - Instruções de instalação (setup) e testes;

    - Se você fornecer uma configuração Docker, certifique-se de que também funcione sem Docker;

    - Uma breve descrição do ambiente usado para rodar o projeto (computador, SO, editor de texto/IDE, bibliotecas, etc.).


## 5. Recomendações

- Escreva testes;

- Siga as melhores práticas de programação;

- Use as melhores práticas de git com mensagens de commit claras;

- Seja cuidadoso ao modelar o banco de dados;

- Valorizamos a simplicidade, então configure seu projeto de forma a facilitar nossa avaliação.


Se algo não estiver claro, entre em contato conosco. Boa sorte!

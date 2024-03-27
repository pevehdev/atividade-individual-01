# Projeto Deu Match!

## Objetivo
Este projeto consiste em desenvolver um aplicativo em Python que gerencia a compatibilidade de um candidato com uma vaga de acordo com seu desempenho em diferentes etapas do processo seletivo. O formato de avaliação adotado é uma string no seguinte padrão: eX_tX_pX_sX, onde cada X representa a avaliação do candidato em uma das etapas - entrevista (e), teste teórico (t), teste prático (p) e avaliação de soft skills (s).

## Funcionalidades

- Armazenamento de Resultados: O código armazena os resultados dos candidatos em uma lista, seguindo o formato especificado.
- Busca de Candidatos: Uma função permite que o usuário busque candidatos com base em critérios específicos, informando as notas mínimas desejadas para cada etapa do processo seletivo.

## Execução

Para executar o programa:

Clone este repositório em sua máquina local:
```
git clone https://github.com/pevehdev/atividade-individual-01.git
```
Navegue até o diretório do projeto:
```
cd atividade_individual_01.py
```
Execute o arquivo python:
```
python atividade_individual_01.py
```
## Exemplo de Uso
Suponha que o usuário deseje buscar candidatos com notas mínimas de e=4, t=4, p=8 e s=8. O programa retorna os candidatos que atendem a esses critérios:

<img width="900" alt="consulta" src="">

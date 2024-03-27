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
<img width="600" alt="consulta" src="https://github.com/pevehdev/atividade-individual-01/blob/main/img/Consulta%20Boletim%201.PNG">
Suponha que o usuário deseje buscar candidatos com notas mínimas de E = 4, T = 4, P = 8 e S = 8 que tenham sidos cadastrados anteriormente. 

O programa retorna os candidatos que atendem a esses critérios:

<img width="600" alt="consulta" src="https://github.com/pevehdev/atividade-individual-01/blob/main/img/Consulta%20Boletim%202.PNG">

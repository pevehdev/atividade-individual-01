# -*- coding: utf-8 -*-
"""Atividade Individual 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11jeMKcQ1JbccGGvmO6AS4TXeSSBLOpTQ
"""

#DICIONARIO PARA MOSTRAR O RESULTADO COM O FORMATO 'eX_tX_pX_sX' e também poder
#FAZER COMPARAÇÃO DE UM DICIONARIO "candidatos"
resultado_candidatos = {


}
#DICIONARIO ONDE ARMAZENA APENAS A CHAVE E A NOTA ESSA CHAVE É UTILIZADA PARA COMPARAR
#COM O DICIONARIO ACIMA "resultado_candidatos"
candidatos = {

}
def inserir_na_tabela_resultado (resultado_candidatos,nome, resultadoString):
    resultado_candidatos[nome] = resultadoString
def adicionar_candidato(cadidatos, nome, notas):
  candidatos[nome] = notas



print('######### BEM VINDO A CONSULTA DE BOLETIM##########')
print('Esolha uma opção abaixo: ')
opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n' )

while opcao == '1' or opcao == '2':

    if opcao == '1':

        N = int(input("Quantos candidatos você deseja adicionar? "))
        resultadoString = 'eX_tX_pX_sX'

        for i in range(1, N+1):
            nome = input(f"Digite o nome do candidato {i}: ")
            notas = []
            for j in range(1, 5):
                if j == 1:
                    nota = input(f"Digite a nota {j} da etapa E(Entrevista): ")
                    notas.append(nota)
                    resultadoString = resultadoString.replace('eX', 'e'+nota)
                if j == 2:
                    nota = input(f"Digite a nota {j} da etapa T(Teste Teórico): ")
                    notas.append(nota)
                    resultadoString = resultadoString.replace('tX', 't'+nota)
                if j == 3:
                    nota = input(f"Digite a nota {j} para disciplina P: ")
                    notas.append(nota)
                    resultadoString = resultadoString.replace('pX', 'p'+nota)
                if j == 4:
                    nota = input(f"Digite a nota {j} para disciplina S: ")
                    notas.append(nota)
                    resultadoString = resultadoString.replace('sX', 's'+nota)

            adicionar_candidato(candidatos, nome, notas)
            inserir_na_tabela_resultado(resultado_candidatos, nome, resultadoString)

            for candidato, notas in candidatos.items():
                print(f' {candidato}: {notas}')

        opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n  3 - Sair\n' )

    elif opcao == '2':
            print('Informe a nota mínima para fazer a busca: ')
            E = int(input('Informe a nota da disciplina E: '))
            T = int(input('Informe a nota da disciplina T: '))
            P = int(input('Informe a nota da disciplina P: '))
            S = int(input('Informe a nota da disciplina S: '))

            encontrou_candidato = False  # Marcador booleano para controlar se alguma nota atende às condições

            for candidato, notas in candidatos.items():
                for candidatoResultado, notasResultado in resultado_candidatos.items():
                    # Convertendo as notas para inteiros
                    notas_int = [int(nota) for nota in notas]
                    if notas_int[0] >= E and notas_int[1] >= T and notas_int[2] >= P and notas_int[3] >= S:
                        if {candidatoResultado} == {candidato} :
                            print(f'{candidatoResultado}: {notasResultado}')
                            encontrou_candidato = True  # Marcador é definido como True se pelo menos um candidato for encontrado
             # Se nenhum candidato foi encontrado, imprime "nada"
            if not encontrou_candidato:
                print(' NADA ENCONTRADO, TENTE CADASTRAR UM ALUNO')
            opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n' )

print('**************CONSULTA ENCERRADA****************** ')

#print(" Lista de Candidatos e suas Notas: ")

#for candidato, notas in candidatos.items():
#  print(f' {candidato}: {notas}')

#newdict = list(candidatos.items())
#print(newdict[1][0])
#print(candidatos)

def adicionar_candidato(candidatos, nome, resultado)

resultado_candidatos = {
    "Candidato 1":["e5_t10_p8_s8"],
    "Candidato 2" : ["e10_t7_p7_s8"],
    "Candidato 3" : ["e8_t5_p4_s9"],
    "Candidato 4" : ["e2_t2_p2_s1"],
    "Candidato 5" : ["e10_t10_p8_s9"]

}

def adicionar_disciplina(disciplinas, nome, notas):
  disciplinas[nome] = notas
disciplinas = {}


############CADASTRO DE DISCIPLINAS#####################

for i in range(1, 5):
  nome = input(f"Digite o nome da disciplina {i}: ")
  notas = []
  for j in range(1, 5):
    nota = float(input(f"Digite a nota {j} para {nome}: "))
    notas.append(nota)
  adicionar_disciplina(disciplinas, nome, notas)

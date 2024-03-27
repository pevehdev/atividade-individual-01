
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
print('\n')
print('Esolha uma opção abaixo: ')
print('\n')
opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n' )
print('\n\n')

while opcao == '1' or opcao == '2':

    if opcao == '1':

        N = int(input("Quantos candidatos você deseja adicionar? "))
        resultadoString = 'eX_tX_pX_sX'

        print('\n\n')

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
                    nota = input(f"Digite a nota {j} da etapa P(Teste Prático): ")
                    notas.append(nota)
                    resultadoString = resultadoString.replace('pX', 'p'+nota)
                if j == 4:
                    nota = input(f"Digite a nota {j} da etapa S(Avaliação de Soft Skill): ")
                    notas.append(nota)
                    resultadoString = resultadoString.replace('sX', 's'+nota)
            print('\n\n')
            adicionar_candidato(candidatos, nome, notas)
            inserir_na_tabela_resultado(resultado_candidatos, nome, resultadoString)

            for candidato, notas in candidatos.items():
                print(f' {candidato}: {notas}')
            print('\n\n')
        opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n  3 - Sair \n \n' )

    elif opcao == '2':
            print('Informe a nota mínima para fazer a busca: ')
            E = int(input('Informe a nota da etapa E(Entrevista): '))
            T = int(input('Informe a nota da etapa T(Teste Teórico): '))
            P = int(input('Informe a nota da etapa P(Teste Prático): '))
            S = int(input('Informe a nota da etapa S(Avaliação de Soft Skill): '))
            print('\n\n')

            encontrou_candidato = False  # Marcador booleano para controlar se alguma nota atende às condições

            for candidato, notas in candidatos.items():
                for candidatoResultado, notasResultado in resultado_candidatos.items():
                    # Convertendo as notas para inteiros
                    notas_int = [int(nota) for nota in notas]
                    if notas_int[0] >= E and notas_int[1] >= T and notas_int[2] >= P and notas_int[3] >= S:
                        if {candidatoResultado} == {candidato} :
                            print(f'{candidatoResultado}: {notasResultado}')
                            encontrou_candidato = True  # Marcador é definido como True se pelo menos um candidato for encontrado
            print('\n\n')
             # Se nenhum candidato foi encontrado, imprime "nada"
            if not encontrou_candidato:
                print(' NADA ENCONTRADO, TENTE CADASTRAR UM ALUNO')
            opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair \n \n' )

print('**************CONSULTA ENCERRADA****************** ')

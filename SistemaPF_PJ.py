# 1 - Pessoa Física / 2 - Pessoa Jurídica / 3 - Sair
# 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 3 - Sair
# 1 - Cadastrar Pessoa Jurídica / 2 - Listar Pessoa Jurídica / 3 - Sair
from datetime import date, datetime
from Pessoavf import PessoaFisica, PessoaJuridica, Endereco

def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input("Escolha uma opção: 1 - Pessoa Física / 2 - Pessoa Jurídica / 3 - Remover CPF Pessoa Física / 4 - Remover CNPJ Pessoa Jurídica / 0 - Sair: "))
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 3- Remover Pessoa Física / 4- Atualizar item da lista / 0 - Sair: "))
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome de pessoa física: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente números): "))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos")
                        continue

                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf
                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}')
                            print(f'Data Nascimento: {cada_pf.dataNascimento.strftime("%d/%m/%Y")}')
                            print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao == 3:
                    cpf_remover = input("Digite o CPF que deseja remover: ")
                    pessoa_encontrada = False
                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_remover:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True
                            print("Pessoa removida com sucesso!")
                            break
                    if not pessoa_encontrada:
                        print("Pessoa não encontrada")
                elif opcao_pf == 4:
                    pf_atualizar = input("Digite o CPF da pessoa que deseja atualizar: ")
                    pessoa_encontrada = False
                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_atualizar:
                            cada_pf.nome = input("Digite o novo nome: ")
                            cada_pf.rendimento = float(input("Digite o novo rendimento mensal: "))
                            novo_end_pf = Endereco()
                            novo_end_pf.logradouro = input("Digite o novo logradouro: ")
                            novo_end_pf.numero = input("Digite o novo número: ")
                            end_comercial = input("Este endereço é comercial? S/N: ")
                            novo_end_pf.endereco_Residencial = end_residencial.strip().upper() == 'S'
                            cada_pf.endereco = novo_end_pf
                            pessoa_encontrada = True
                            print("Cadastro PF atualizado com sucesso!")
                            break
                    if not pessoa_encontrada:
                        print("Pessoa não encontrada")
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opção inválida! Por favor, digite uma das opções abaixo:")
    #CADASTRO PESSOA JURÍDICA
        elif opcao == 2:
            while True:
                opcao_pj = int(input("Escolha uma opção: 1 - Cadastrar Pessoa Jurídica / 2 - Listar Pessoa Jurídica / 3 - Remover Pessoa Jurídica / 4 - Atualizar item da lista / 0 - Sair: "))
                if opcao_pj == 1:
                    novapj = PessoaJuridica()
                    novo_end_pj = Endereco()

                    novapj.nome = input("Digite o nome da empresa: ")
                    novapj.cnpj = input("Digite o CNPJ: ")
                    novapj.rendimento = float(input("Digite o rendimento mensal (Digite somente números): "))

                    novo_end_pj.logradouro = input("Digite o logradouro: ")
                    novo_end_pj.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pj.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapj.endereco = novo_end_pj
                    lista_pj.append(novapj)

                    print("Cadastro realizado com sucesso!")

                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f'Nome: {cada_pj.nome}')
                            print(f'CNPJ: {cada_pj.cnpj}')
                            print(f'Endereço: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}')
                            print(f'Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}')
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                
                elif opcao_pj == 3:
                    cnpj_remover = input("Digite o CNPJ que deseja remover: ")
                    empresa_encontrada = False
                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_remover:
                            lista_pj.remove(cada_pj)
                            empresa_encontrada = True
                            print("Empresa removida com sucesso!")
                            break
                    if not empresa_encontrada:
                        print("Empresa não encontrada")                

                elif opcao_pj == 4:
                    cnpj_atualizar = input("Digite o CNPJ da empresa que deseja atualizar: ")
                    pessoa_encontrada = False
                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_atualizar:
                            cada_pj.nome = input("Digite o novo nome: ")
                            cada_pj.rendimento = float(input("Digite o novo rendimento mensal: "))
                            novo_end_pj = Endereco()
                            novo_end_pj.logradouro = input("Digite o novo logradouro: ")
                            novo_end_pj.numero = input("Digite o novo número: ")
                            end_comercial = input("Este endereço é comercial? S/N: ")
                            novo_end_pj.endereco_Comercial = end_comercial.strip().upper() == 'S'
                            cada_pj.endereco = novo_end_pj
                            pessoa_encontrada = True
                            print("Empresa atualizada com sucesso!")
                            break
                    if not pessoa_encontrada:
                        print("Empresa não encontrada")


                elif opcao_pj == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opção inválida! Por favor, digite uma das opções abaixo:")




        elif opcao == 0:
            print("Voltando ao menu inicial!")
            break
        else:
            print("Opção inválida! Por favor, digite uma das opções válidas!")

if __name__ == "__main__":
    main()
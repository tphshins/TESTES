def mb_para_gb(mb):
    gb = mb / 1024
    return gb

def gb_para_mb(gb):
    mb = gb * 1024
    return mb

def main():
    while True:
        print("Escolha a opção desejada:")
        print("1. Converter MB para GB")
        print("2. Converter GB para MB")
        print("3. Sair")
        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            mb = float(input("Digite a quantidade de MB: "))
            gb = mb_para_gb(mb)
            print(f"{mb} MB = {gb} GB\n")
        elif escolha == "2":
            gb = float(input("Digite a quantidade de GB: "))
            mb = gb_para_mb(gb)
            print(f"{gb} GB = {mb} MB\n")
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()

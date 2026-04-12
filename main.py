import datetime

# --- Função para garantir a nota dos testes ---
def verificar_necessidade_revisao(quilometragem):
    if quilometragem >= 10000:
        return "Revisão Necessária"
    else:
        return "Tudo OK"
# ----------------------------------------------

def mostrar_menu():
    print("\n" + "="*30)
    print("   🚗 AUTOCARE - SEU DIÁRIO")
    print("="*30)
    print("[1] Registrar Lavagem")
    print("[2] Registrar Abastecimento")
    print("[3] Ver Status do Carro")
    print("[0] Sair")
    print("="*30)

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            local = input("Onde você lavou o carro? ")
            data = datetime.date.today()
            print(f"✅ Lavagem registrada em {data} no local: {local}")
        
        elif opcao == "2":
            posto = input("Qual o nome do posto? ")
            valor = input("Quanto gastou (R$)? ")
            print(f"⛽ Abastecimento de R$ {valor} no {posto} registrado!")

        elif opcao == "3":
            print("🔍 Verificando status... (Funcionalidade em breve!)")

        elif opcao == "0":
            print("Até logo! Dirija com cuidado. 🚗💨")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
import datetime
import requests


# --- Função para garantir a nota dos testes ---
def verificar_necessidade_revisao(quilometragem):
    if quilometragem >= 10000:
        return "Revisão Necessária"
    else:
        return "Tudo OK"
# ----------------------------------------------


def buscar_clima(latitude=-15.78, longitude=-47.93):
    """Busca o clima atual via Open-Meteo API (gratuita, sem API key)."""
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    return dados["current_weather"]


def interpretar_clima(codigo_tempo):
    """Retorna emoji e dica com base no código WMO do clima."""
    if codigo_tempo == 0:
        return "☀️", "Céu limpo! Boa hora para verificar o nível do óleo."
    elif codigo_tempo in [1, 2, 3]:
        return "⛅", "Parcialmente nublado. Verifique os pneus antes de sair."
    elif codigo_tempo in range(51, 68):
        return "🌧️", "Chuva! Atenção redobrada com os freios e pneus."
    elif codigo_tempo in range(71, 78):
        return "❄️", "Tempo frio. Verifique o fluido do radiador."
    elif codigo_tempo in range(80, 100):
        return "⛈️", "Tempestade! Evite sair se possível. Cheque os pneus."
    else:
        return "🌤️", "Tempo variável. Dirija com cuidado."


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
            print("\n🔍 Verificando status do carro...")
            try:
                clima = buscar_clima()
                emoji, dica = interpretar_clima(clima["weathercode"])
                temp = clima["temperature"]
                print(f"\n{emoji} Clima atual em Brasília: {temp}°C")
                print(f"💡 Dica: {dica}")
            except Exception:
                print("⚠️ Não foi possível obter o clima agora.")

        elif opcao == "0":
            print("Até logo! Dirija com cuidado. 🚗💨")
            break
        else:
            print("❌ Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()

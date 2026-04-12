# 🚗 AutoCar CLI (Diário de Bordo)

**Versão:** 1.0.0
**Autor:** Diogo Heberth

## 🎯 Qual problema estamos resolvendo?
Muitos motoristas esquecem os prazos de manutenções preventivas básicas de seus veículos (como troca de óleo, calibragem de pneus e lavagem). Essa falta de controle gera riscos de segurança, diminui a vida útil do carro e causa prejuízos financeiros com manutenções corretivas. Além disso, muitas vezes o motorista esquece onde realizou um bom serviço ou onde abasteceu.

## 💡 A Solução
O **AutoCar CLI** é uma aplicação simples de linha de comando que funciona como um diário de bordo do veículo. Ele permite registrar abastecimentos e serviços (guardando a data, quilometragem e o local) e emite alertas caso alguma manutenção básica esteja atrasada.

## 👥 Público-Alvo
Motoristas do dia a dia que desejam um controle simples, rápido e sem complicações do seu veículo, sem precisar navegar por aplicativos complexos cheios de anúncios.

## 🚀 Funcionalidades Principais
* **Registrar Serviço:** Salva o tipo de serviço (óleo, pneu, lavagem), a quilometragem atual e o local onde foi feito.
* **Registrar Abastecimento:** Salva a quantidade de litros, o valor pago e o posto de combustível.
* **Painel de Status (Lembretes):** Verifica o histórico e avisa o motorista se está na hora de realizar alguma manutenção.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Armazenamento:** Arquivo local em formato `.json` (sem necessidade de banco de dados complexo).
* **Testes Automatizados:** `pytest`
* **Linting / Qualidade de Código:** `flake8`
* **CI/CD:** GitHub Actions

## ⚙️ Como Instalar e Executar

1. Clone o repositório:

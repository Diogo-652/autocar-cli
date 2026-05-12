from unittest.mock import patch, MagicMock
from main import buscar_clima, interpretar_clima


def test_buscar_clima_retorna_dados_corretos():
    """Testa se buscar_clima processa corretamente a resposta da API."""
    resposta_fake = {
        "current_weather": {
            "temperature": 28.5,
            "weathercode": 0,
            "windspeed": 10.0
        }
    }

    mock_response = MagicMock()
    mock_response.json.return_value = resposta_fake
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response) as mock_get:
        resultado = buscar_clima()
        mock_get.assert_called_once()
        assert resultado["temperature"] == 28.5
        assert resultado["weathercode"] == 0


def test_interpretar_clima_ceu_limpo():
    emoji, dica = interpretar_clima(0)
    assert emoji == "☀️"
    assert "óleo" in dica


def test_interpretar_clima_chuva():
    emoji, dica = interpretar_clima(61)
    assert emoji == "🌧️"
    assert "freios" in dica


def test_interpretar_clima_tempestade():
    emoji, dica = interpretar_clima(95)
    assert emoji == "⛈️"


def test_interpretar_clima_nublado():
    emoji, dica = interpretar_clima(2)
    assert emoji == "⛅"

from main import verificar_necessidade_revisao

def test_revisao_ok():
    assert verificar_necessidade_revisao(5000) == "Tudo OK"

def test_revisao_necessaria():
    assert verificar_necessidade_revisao(10500) == "Revisão Necessária"

def test_revisao_no_limite():
    assert verificar_necessidade_revisao(10000) == "Revisão Necessária"
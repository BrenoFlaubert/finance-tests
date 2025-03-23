from app.models import Lancamento

def test_criar_lancamento():
    lancamento = Lancamento(valor=100, descricao="Teste")
    assert lancamento.valor == 100
    assert lancamento.descricao == "Teste"
    assert isinstance(lancamento.id, int)

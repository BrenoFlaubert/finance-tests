import pytest
from app.models import Lancamento
from app.services import LancamentoService

@pytest.fixture
def service():
    return LancamentoService()

def test_fluxo_completo(service):
    l1 = service.cadastrar(Lancamento(valor=100, descricao="Compra"))
    l2 = service.cadastrar(Lancamento(valor=200, descricao="Venda"))
    
    assert len(service.listar()) == 2
    assert service.excluir(l1.id) is True
    assert len(service.listar()) == 1

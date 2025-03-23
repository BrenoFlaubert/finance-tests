import pytest
from app.models import Lancamento
from app.services import LancamentoService

@pytest.fixture
def service():
    return LancamentoService()

def test_mesmo_valor_nao_altera_outros(service):
    l1 = service.cadastrar(Lancamento(valor=500, descricao="Teste 1"))
    l2 = service.cadastrar(Lancamento(valor=500, descricao="Teste 2"))
    
    assert l1.id != l2.id

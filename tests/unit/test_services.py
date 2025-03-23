import pytest
from app.models import Lancamento
from app.services import LancamentoService

@pytest.fixture
def service():
    return LancamentoService()

def test_cadastrar_lancamento(service):
    lancamento = Lancamento(valor=200, descricao="Unit Test")
    resultado = service.cadastrar(lancamento)
    assert resultado == lancamento

def test_listar_vazio(service):
    assert service.listar() == []

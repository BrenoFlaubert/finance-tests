import pytest
from app.models import Lancamento
from app.services import LancamentoService

@pytest.fixture
def service():
    return LancamentoService()

def test_listar_apos_cadastro(service):
    service.cadastrar(Lancamento(valor=500, descricao="Integrado"))
    assert len(service.listar()) == 1

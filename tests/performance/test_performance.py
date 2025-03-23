import pytest
from app.models import Lancamento
from app.services import LancamentoService
import time

@pytest.fixture
def service():
    return LancamentoService()

def test_cadastro_massivo(service):
    inicio = time.time()
    
    for i in range(1000):
        service.cadastrar(Lancamento(valor=i, descricao=f"Teste {i}"))
    
    fim = time.time()
    assert len(service.listar()) >= 1000
    assert fim - inicio < 5  # Teste deve rodar em menos de 5 segundos

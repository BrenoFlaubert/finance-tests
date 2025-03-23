class LancamentoService:
    def __init__(self):
        self.lancamentos = []

    def cadastrar(self, lancamento):
        self.lancamentos.append(lancamento)
        return lancamento

    def listar(self):
        return self.lancamentos

    def excluir(self, id_lancamento):
        for l in self.lancamentos:
            if l.id == id_lancamento:
                self.lancamentos.remove(l)
                return True
        return False

    def atualizar(self, lancamento_atualizado):
        for i, l in enumerate(self.lancamentos):
            if l.id == lancamento_atualizado.id:
                self.lancamentos[i] = lancamento_atualizado
                return lancamento_atualizado
        return None

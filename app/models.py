class Lancamento:
    _id = 0 
    
    def __init__(self, valor, descricao):
        Lancamento._id += 1
        self.id = Lancamento._id
        self.valor = valor
        self.descricao = descricao

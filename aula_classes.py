# criar classe Cliente e seus atributos/Caracteristicas
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ["Basic", "HD", "Premium 4k"]
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception('O plano não existe ou não é valido!')
        print('Bem vindo: ', self.nome, '\nSeu plano atual: ', self.plano)
    
    # metodos/Funçoes/ações que o objeto pode fazer
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
            print('Novo plano ativado: ', self.plano)
        else:
            print('Plano inválido!')
            # raise Exception('Plano informado inválido!')
        
        
        
# instanciar(chamar) classe e passar seus atributos com argumentos.
new_client = Cliente('Davi','davi@email.com','Premium 4k')
print(new_client.plano)
new_client.mudar_plano('HD')
print(new_client.plano)

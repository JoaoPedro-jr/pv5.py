
for i in range(3):
    tentativas = 3 - (i - 1)
    print('Bem-vindo a infinit , efetue o login:')
    usuario = input('digite o nome do usuario:')
    senha = int(input('digite a senha:'))
    if usuario == 'admin' and senha == 1234:
        print('usuario autenticado , acesso liberado')
        break
    elif i == 4:
        print('usuario bloqueado')
        break

    else:
        print(f'usuario ou senha invalidos , restão {tentativas} tentativas')
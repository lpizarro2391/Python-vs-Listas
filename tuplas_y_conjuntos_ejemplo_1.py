valid_alpha_user = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-_."

while True:
    user = input("Ingrese el nombre de usuario")
    if (len(user)>4):
        a = set(valid_alpha_user)
        b= set (user)
        if len(b-a)>0:
            print("Usuario invalido.")
            continue
        else:
            print("Usuario Válido")
            break
    else:
        print("Usuario inválido.")

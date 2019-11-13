def read_player_command():
    move = ''
    while move not in ['z','q','s','d']:
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

#read_player_command()

     
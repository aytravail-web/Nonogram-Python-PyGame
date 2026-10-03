# Model/debug

# Pour simplifier le debuggage,
# mise en place de la fonction debug qui affichera les messages
# si la variable DEBUG définie ici est à True
#

DEBUG = False


def debug(msg: str) -> None:
    """
    Affiche à l'écran si DEBUG vaut TRUE

    :param msg: Message à afficher
    :return: Rien
    """
    global DEBUG
    if DEBUG:
        print(msg)
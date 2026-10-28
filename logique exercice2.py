

def chainage_arriere(objectif, faits, regles, visites=None):
    if objectif in faits:
        return True

    if visites is None:
        visites = set()

    if objectif in visites:
        return False

    visites = visites | {objectif}

    for conditions, conclusion in regles:
        if conclusion == objectif:
            if all(
                chainage_arriere(c, faits, regles, visites)
                for c in conditions
            ):
                return True

    return False

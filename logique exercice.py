
#chanage avant
def chainage_avant(faits, regles):
    faits = set(faits)
    changement = True

    while changement:
        changement = False

        for conditions, conclusion in regles:
            if conditions.issubset(faits):
                if conclusion not in faits:
                    faits.add(conclusion)
                    changement = True

    return faits

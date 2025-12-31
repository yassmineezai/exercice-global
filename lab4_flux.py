def saisir_notes(max_notes=10, seuil=10):
    notes = []
    compteur = 0

    while compteur < max_notes:
        saisie = input(f"Note {compteur + 1} (/20) ou 'stop' pour terminer : ").lower()
        if saisie == "stop":
            break

        try:
            note = float(saisie)
        except ValueError:
            print("Saisie invalide. Recommence.")
            continue

        if 0 <= note <= 20:
            notes.append(note)
            compteur += 1
        else:
            print("Note hors plage. Elle doit être entre 0 et 20.")
            continue

    else:
        print("Nombre maximum de notes atteint.")

    print("\n📋 Résultats des étudiants :")
    for index, note in enumerate(notes, start=1):
        statut = (
            "Mention Très Bien" if note >= 16 else
            "Mention Bien" if note >= 14 else
            "Mention Assez Bien" if note >= 12 else
            "Admis" if note >= seuil else
            "Rattrapage" if note >= 8 else
            "Refusé"
        )
        print(f"Étudiant {index} → Note : {note} → Statut : {statut}")

    if notes:
        moyenne = sum(notes) / len(notes)
        mention_globale = (
            "Très Bien" if moyenne >= 16 else
            "Bien" if moyenne >= 14 else
            "Assez Bien" if moyenne >= 12 else
            "Admis" if moyenne >= seuil else
            "Refusé"
        )
        print(f"\n📊 Moyenne de la classe : {moyenne:.2f} → Mention globale : {mention_globale}")
    else:
        print("\nAucune note valide saisie.")

# Appel de la fonction
saisir_notes()

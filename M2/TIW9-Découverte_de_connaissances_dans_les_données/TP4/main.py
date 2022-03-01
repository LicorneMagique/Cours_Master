from prefixspan import PrefixSpan
import csv
import sys
import json


def getEchangesParPoint(useLateralite=False, useCoup=False, useZone=False, useType=False):
    gagnants = dict() # Map<Nom, gagnant: boolean>
    currentActions = list()
    f = 0
    for action in CSV_DICT_LINES:
        currentActions.append(action)
        if action["Score"] != "":
            gagnant = "F" if f < int(action["Points F"]) else "B"
            f = int(action["Points F"])
            for line in currentActions:
                gagnants[line["Nom"]] = line["Nom"].strip().startswith(gagnant)
            currentActions = list()
    echangesParPointGagnant = list()
    echangesParPointPerdant = list()
    actionsEchangeCourantGagnant = list()
    actionsEchangeCourantPerdant = list()
    for action in CSV_DICT_LINES:
        lateralite = action["Latéralité"].strip().replace(" ", "-")
        coup = action["Coup"].strip().replace(" ", "-")
        typeCoup = action["Type Coup TK"].strip().replace(" ", "-")
        typeService = action["Type de service"].strip().replace(" ", "-")
        zone = action["Zone de jeu"].strip().replace(" ", "-")
        if zone == "":
            zone = "Sortie" if action["Score"] != "" else "Service"
        typeAction = typeService if typeCoup.__len__() == 0 else typeCoup
        lineTab = list()
        if useLateralite:
            lineTab.append(lateralite)
        if useCoup:
            lineTab.append(coup)
        if useZone:
            lineTab.append(zone)
        if useType:
            lineTab.append(typeAction)
        if "" in lineTab:
            continue
        lineStr = "_".join(lineTab)
        (actionsEchangeCourantGagnant if gagnants[action["Nom"]] else actionsEchangeCourantPerdant).append(lineStr)
        if action["Coup"] in {"Serveur Point +", "Serveur Point -"}:
            echangesParPointGagnant.append(actionsEchangeCourantGagnant)
            echangesParPointPerdant.append(actionsEchangeCourantPerdant)
            actionsEchangeCourantGagnant = list()
            actionsEchangeCourantPerdant = list()
    return echangesParPointGagnant, echangesParPointPerdant


def getResultsWith(minlen, k, useLateralite=False, useCoup=False, useZone=False, useType=False):
    echangesParPointGagnant, echangesParPointPerdant = getEchangesParPoint(useLateralite, useCoup, useZone, useType)

    psGagnants = PrefixSpan(echangesParPointGagnant)
    psPerdants = PrefixSpan(echangesParPointPerdant)
    psGagnants.minlen = minlen
    psPerdants.minlen = minlen
    resultsGagnants = psGagnants.topk(k)
    resultsPerdants = psPerdants.topk(k)
    resultsCommuns = [rp for rp in resultsPerdants if rp.__getitem__(1) in [rg.__getitem__(1) for rg in resultsGagnants]]
    resultsToRemove = [rm.__getitem__(1) for rm in resultsCommuns]
    resultsGagnants = [rg for rg in resultsGagnants if rg.__getitem__(1) not in resultsToRemove]
    resultsPerdants = [r for r in resultsPerdants if r.__getitem__(1) not in resultsToRemove]
    return {"gagnant": resultsGagnants, "perdant": resultsPerdants, "commun": resultsToRemove}


CSV_DICT_LINES = None


def loadFileCsv(file):
    global CSV_DICT_LINES
    if CSV_DICT_LINES is None:
        CSV_DICT_LINES = list()
        csvFile = open(file, "r", newline="", encoding="utf-8-sig")
        CSV_DICT_LINES = list()
        csvDictReader = csv.DictReader(csvFile, delimiter=";")
        for csvDictLine in csvDictReader:
            CSV_DICT_LINES.append(csvDictLine)
    return CSV_DICT_LINES


def getDistinctColumnValues():
    distinctValues = dict()
    for key in CSV_DICT_LINES[0].keys():
        values = [line[key] for line in CSV_DICT_LINES]
        distinctValues[key] = {value: values.count(value) for value in values}
    return distinctValues


def main(file, minlen, k, useLateralite, useCoup, useZone, useType):
    loadFileCsv(file)

    # Données de test à regarder avec le débugger
    distinctColumnValues = getDistinctColumnValues()
    test = getResultsWith(minlen=2, k=10, useLateralite=True, useCoup=True, useZone=False, useType=False)
    test2 = getResultsWith(minlen=3, k=10, useLateralite=True, useCoup=True, useZone=False)
    test3 = getResultsWith(minlen=3, k=10, useLateralite=False, useCoup=True, useZone=False)

    result = getResultsWith(minlen, k, useLateralite, useCoup, useZone, useType)
    print(json.dumps(result))


'''
Notre programme permet de poser les questions suivantes :

- Quels sont les patterns présents chez les joueurs qui gagnent mais qui ne sont pas présents chez les joueurs qui perdent ?
- Quels sont les patterns présents chez les joueurs qui perdent mais qui ne sont pas présents chez les joueurs qui gagnent ?
- Quels sont les patterns présents à la fois chez les joueurs qui gagnent et chez ceux qui perdent ?

Autrement dit si on réécrit ces question avec un langage plus humain :

- Quelles sont les stratégies gagnantes ?
  Celles qu'il faut privilégier.
- Quelles sont les stratégies perdantes ?
  Celle qu'il faut éviter.
- Quels sont les stratégies à la fois gangantes et perdantes ?
  Celles qu'il faut privilégier si on hésite avec un coup perdant,
  mais à ne pas privilégier si on hésite avec un coup gagnant.
'''

if __name__ == "__main__":
    if sys.argv.__len__() < 7:
        print("Usage:\n> python3 main.py file, minlen, k, useLaterabilite (True/False), useCoup, useZone, useType")
        exit()
    file = sys.argv[1]
    minlen = int(sys.argv[2])
    k = int(sys.argv[3])
    useLaterabilite = bool(sys.argv[4])
    useCoup = bool(sys.argv[5])
    useZone = bool(sys.argv[6])
    useType = bool(sys.argv[7])
    main(file, minlen, k, useLaterabilite, useCoup, useZone, useType)

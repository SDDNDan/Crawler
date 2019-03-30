import pandas as pd
import matplotlib.pyplot as plt
from Shared.NewsType import newsType

NewsSite = ['StireaZilei', 'StiriPeSurse', 'B1', 'MediaFax', 'ProTV', 'Tvr1']

news = ['economic', 'economic', 'politica', 'sport', 'accidente', 'infractiuni', 'meteo', 'cultura', 'horoscop', 'IT&C',
        'Auto', 'Monden', 'rezultate meritorii', 'sanatate si fitness', 'educatie', 'divertisment',
        'religie', 'rutier', 'medical']
newsDictionary = dict()
newsDictionary['economic'] = 0
newsDictionary['politica'] = 0
newsDictionary['sport'] = 0
newsDictionary['accidente'] = 0
newsDictionary['infractiuni'] = 0
newsDictionary['meteo'] = 0
newsDictionary['cultura'] = 0
newsDictionary['horoscop'] = 0
newsDictionary['IT&C'] = 0
newsDictionary['Auto'] = 0
newsDictionary['Monden'] = 0
newsDictionary['rezultate meritorii'] = 0
newsDictionary['sanatate si fitness'] = 0
newsDictionary['educatie'] = 0
newsDictionary['divertisment'] = 0
newsDictionary['religie'] = 0
newsDictionary['rutier'] = 0
newsDictionary['medical'] = 0


def readNewsByNews(newsSite):
    with open(newsSite + "/queue.txt", "r") as ins:
        for line in ins:
            findTypeOfNews(line)
            if limitIsOut():
                break


def findTypeOfNews(new):
    for typeOfNew, words in newsType.items():
        for word in words:
            if word in new:
                newsDictionary[typeOfNew] += 1
                if typeOfNew == 'sport' and newsDictionary['sport'] > 150:
                    newsDictionary['sport'] -= 1
                break
    return 'NotFound'


def limitIsOut():
    suma = 0
    for k, v in newsDictionary.items():
        suma += v
    if suma >= 500:
        return True
    return False


def resetDictionary():
    for k, v in newsDictionary.items():
        newsDictionary[k] = 0


def start():
    for new in NewsSite:
        resetDictionary()
        readNewsByNews(new)
        makePieChar(new)


def createPieChartForAllType():
    for typeOfNew in news:
        siteValues = []
        for site in NewsSite:
            siteValues.append(createForType(site,typeOfNew))
        explode = []
        for k in siteValues:
            explode.append(0.5 / (k + 1))
        print(explode)
        df = pd.DataFrame({typeOfNew: siteValues}, index=NewsSite)

        df.plot(kind='pie', explode=tuple(explode), subplots=True, figsize=(16, 16), autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.savefig('Charts/TipulDeStire/' + typeOfNew)


def createForType(site, typeOfNews):
    resetDictionary()
    readNewsByNews(site)
    return newsDictionary[typeOfNews]


def makePieChar(new):
    labels = []
    values = []
    explode = []
    for k, v in newsDictionary.items():
        labels.append(k)
        values.append(v)
        explode.append(0.5 / (v + 1))
    df = pd.DataFrame({'News Types': values}, index=labels)

    df.plot(kind='pie', explode=tuple(explode), subplots=True, figsize=(16, 16), autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.savefig('Charts/Site/' + new)


start()
createPieChartForAllType()

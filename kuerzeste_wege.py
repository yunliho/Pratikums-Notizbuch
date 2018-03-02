#!/usr/bin/python3

import sys

# Repräsentation der Zahl "unendlich"
UNENDLICH = float('inf')
# Repräsentation von "nicht spezifiziert" oder "keine Information"
NICHTS = -1

'''
Vervollständige die folgenden Funktionen in der Reihenfolge, in denen du sie unten findest ihrer Beschreibung entsprechend.
Ersetze dazu 'pass' durch deinen Programmcode.

Du kannst testen, ob dein Code in Funktion 'funktion' richtig funktioniert, indem du in einer Konsole
    python3.5 -m unittest tests.TestKuerzesteWege.test_funktion
aufrufst.




Tip: Oft kannst und solltest du Funktionen verwenden, die du vorher geschrieben hast.

'UNENDLICH' und 'NICHTS' sind definiert und du kannst sie wie normale Zahlen benutzen,
zum Beispiel wird der folgende Code "3 ist kleiner als unendlich" ausgeben:

    zahl1 = UNENDLICH
    zahl2 = 3
    if zahl2 < zahl1:
        print(str(zahl2) + " ist kleiner als unendlich")

Ein Pythonprogramm wird mit 'exit(0)' beendet.

Mengen werden mit 'set()' initialisiert.
- Du kannst einer Menge 's' ein Element 'e' hinzufügen, indem du 's.add(e)' aufrufst.
- Du kannst ein Element 'e' aus einer Menge 's' löschen, indem du 's.remove(e)' aufrufst.
- Mit 'len(s)' findest du die Anzahl der Elemente einer Menge heraus.

Dictionaries werden mit '{}' initialisiert.
- Du speicherst ein Element 'e' in einem Dictionary 'd' unter dem Key 'k', indem du 'd[k] = e' aufrufst.
- Die Keys eines Dictionaries 'd' bekommst du mit 'd.keys()'
'''

def beende_programm(nachricht):
    '''
    Gib die Nachricht aus und beende das Programm.

    Parameters
    ==========
    nachricht : str
        Nachricht, die vor dem Beenden ausgegeben wird.
    '''
    print(nachricht)    
    exit(0)


def graph_abstand(graph, knoten1, knoten2):
    '''
    Gib den Abstand zweier Knoten in einem Graphen zurück.

    Wenn die Kante (knoten1, knoten2) nicht im Graphen ist,
    beende das Programm mit der Fehlermeldung:
        "Kann gesuchte Kante im Graphen nicht finden."

    Wenn die Kante (knoten1, knoten2) einen Wert null oder kleiner hat,
    beende das Programm mit der Fehlermeldung:
        "Nichtpositive Kantengewichte sind verboten."

    Parameters
    ==========
    graph : dict
        graph[(i,j)] : int
            ist der Abstand von i und j oder UNENDLICH, falls i und j nicht verbunden sind.
            Dabei ist i stets kleiner oder gleich j.
        graph['alleknoten'] : set
            enthält die Menge der Knoten.
    knoten1 : int
        Knoten im Graph.
    knoten2 : int
        Knoten im Graph.

    Returns
    =======
    int
        Der Abstand zwischen knoten1 und knoten2.
    '''
    if knoten1>knoten2:
       # n=knoten1
       # knoten1=knoten2
       # knoten2=n
       knoten1, knoten2 = tausche(knoten1, knoten2)
    if (knoten1, knoten2) not in graph.keys():
       beende_programm("Kann gesuchte Kante im Graphen nicht finden.")
    elif graph[(knoten1, knoten2)]<=0:
       beende_programm("Nichtpositive Kantengewichte sind verboten.")
    elif graph[(knoten1, knoten2)]>0:
       return graph[(knoten1, knoten2)]


def sind_nachbarn(graph, knoten1, knoten2):
    '''
    Entscheide, ob 'knoten1' und 'knoten2' Nachbarn sind.

    Zwei Knoten heißen Nachbarn, wenn sie verbunden sind, also ihr Abstand kleiner als UNENDLICH ist.

    Parameters
    ==========
    graph : dict
        graph[(i,j)] : int
            ist der Abstand von i und j oder UNENDLICH, falls i und j nicht verbunden sind.
            Dabei ist i stets kleiner oder gleich j.
    knoten1 : int
        Knoten im Graph.
    knoten2 : int
        Knoten im Graph.

    Returns
    =======
    bool
        'True', wenn 'knoten1' und 'knoten2' verbunden sind, ansonsten 'False'.
    '''
    if knoten1>knoten2:
       # n=knoten1
       # knoten1=knoten2
       # knoten2=n
       knoten1, knoten2 = tausche(knoten1, knoten2)
    if graph[(knoten1, knoten2)]<UNENDLICH:
       return True
    else:
       return False 	 		
   
    
def tausche(k1, k2):
    '''
    Gib k1 und k2 in der umgekehrten Reihenfolge zurück.
    '''
    return k2, k1


def alle_nachbarknoten(graph, knoten):
    '''
    Erstelle eine Menge von Knoten die Nachbarn von 'knoten' sind.

    Parameters
    ==========
    graph : dict
        graph[(i,j)] : int
            ist der Abstand von i und j oder UNENDLICH, falls i und j nicht verbunden sind.
            Dabei ist i stets kleiner oder gleich j.
        graph['alleknoten'] : set
            enthält die Menge der Knoten.
    knoten : int
        Knoten im Graph.

    Returns
    =======
    set
        Die Menge aller Nachbarn von 'knoten'.
    '''
    nachbarn = set()
    for knoten2 in graph['alleknoten']:
        if sind_nachbarn(graph, knoten, knoten2):
           nachbarn.add(knoten2)
    return nachbarn   


def naechster_knoten(knotenmenge, abstaende):
    '''
    Gegeben eine Menge von Knoten und Abständen, finde den Knoten, der den geringsten Abstand hat.

    Wenn 'knotenmenge' leer ist, beende das Programm mit der Fehlermeldung:
        "Knotenmenge darf nicht leer sein."

    Parameters
    ==========
    knotenmenge : set(int)
        Menge von Knoten.
    abstaende : dict(int -> int)
        Für jeden Knoten i gibt abstand[i] die Länge des kürzesten Wegs zwischen start und i an.
        Achtung: UNENDLICH ist ein gültiger Abstand.

    Returns
    =======
    int
        Der Knoten mit dem kleinsten Abstand.
    '''
    if len(knotenmenge) == 0 :
       beende_programm("Knotenmenge darf nicht leer sein.")
        
    x=set()
    # finde den minimalen abstand
    for k in knotenmenge:
       y=abstaende[k]
       x.add(y)
       ka=min(x) 

    # gib einen knoten zurück, der minimalen Abstand hat
    for k in knotenmenge:       
        if ka == abstaende[k]:
           return k

    # alternativ
    #minimum = UNENDLICH
    #mini_knoten = knotenmenge[0]
    #for knoten in knotenmenge:
    #    if abstaende[knoten] < minimum:
    #         minimum = abstaende[knoten]
    #         mini_knoten = knoten
    #return mini_knoten


def berechne_kuerzeste_wege_von(graph, start):
    '''
    Berechne kürzeste Wege vom Knoten 'start' zu jedem Knoten im Graphen.

    Benutze den Dijkstra-Algorithmus.

    Parameters
    ==========
    graph : dict
        graph[(i,j)] : int
            ist der Abstand von i und j oder UNENDLICH, falls i und j nicht verbunden sind.
            Dabei ist i stets kleiner oder gleich j.
        graph['alleknoten'] : set
            enthält die Menge der Knoten.
    start : int
        Der Knoten, von dem aus alle kürzesten Wege gesucht werden.

    Returns
    =======
    abstaende : dict(int -> int)
        Für jeden Knoten i gibt abstand[i] die Länge des kürzesten Wegs zwischen start und i an.
        Achtung: UNENDLICH ist ein gültiger Abstand.
    vorgaenger : dict(int -> int)
        Für jeden Knoten i gibt vorgaenger[i] den Vorgängerknoten im kürzesten Weg an.
    '''
    # bereite variablen vor: initialisierung 
    Q=set()
    abstaende={}
    vorgaenger={}
    for v in graph['alleknoten']:
        abstaende[v]=UNENDLICH
        vorgaenger[v]=NICHTS
        Q.add(v)

    # dijkstra algorithmus
    abstaende[start]=0
    while len(Q) != 0:
          u= naechster_knoten(Q,abstaende)
          Q.remove(u)
          for v in alle_nachbarknoten(graph, u) :
              alt=abstaende[u]+ graph_abstand(graph ,u , v)
              if alt < abstaende[v]:
                 abstaende[v]=alt
                 vorgaenger[v]=u
    return abstaende, vorgaenger


def schreibe_weg(start, ziel, abstaende, vorgaenger):
    '''
    Gib eine lesbare Repräsentation des Wegs zwischen Start und Ziel zurück.

    Konstruiere einen String, der die folgende Form hat:
        Länge des kürzesten Wegs: 5.
        Stationen: 1 - 2 - 3.
    (Dies ist ein Beispiel für folgende Belegung:
        start = 1
        ziel = 3
        vorgaenger[3] = 2
        vorgaenger[2] = 1
        abstaende[3] = 5.)
    Beachte den Zeilenumbruch.

    Wenn der Weg langer ist als die Anzahl der Knoten im Graph,
    beende das Programm mit der Fehlermeldung:
        "Wir haben uns verlaufen und sind in einem Kreis gefangen."

    Wenn der Weg ins NICHTS führt,
    beende das Programm mit der Fehlermeldung:
        "Wir sind ins Nichts gelaufen."

    Parameters
    ==========
    start : int
        Der Start-Knoten
    ziel : int
        Der Ziel-Knoten
    abstaende : dict(int -> int)
        Für jeden Knoten i gibt abstand[i] die Länge des kürzesten Wegs zwischen start und i an.
        Achtung: UNENDLICH ist ein gültiger Abstand.
    vorgaenger : dict(int -> int)
        Für jeden Knoten i gibt vorgaenger[i] den Vorgängerknoten im kürzesten Weg an.

    Returns
    =======
    string
        Die Repräsentation des Wegs.
    '''
    if ziel == NICHTS:
       beende_programm("Wir sind ins Nichts gelaufen.")
    wege = str(ziel)
    pos = ziel
    schritte=0
    while vorgaenger[pos] != NICHTS:
       wege =str(vorgaenger[pos]) +' - '+ wege
       pos = vorgaenger[pos]
       schritte=schritte+1
       if schritte > len(abstaende) :
          beende_programm("Wir haben uns verlaufen und sind in einem Kreis gefangen.")
    else:
       if pos!=start:
          beende_programm("Wir sind ins Nichts gelaufen.")
    l= 'Länge des kürzesten Wegs: '+str(abstaende[ziel])+'.'
    s= 'Stationen: '+wege+'.'
    output = l + "\n" + s
    return output


def konstruiere_leeren_graphen(knotenanzahl):
    '''
    Konstruiere einen leeren Graphen mit Knoten 0 bis ('knotenanzahl' - 1)

    Wenn 'knotenanzahl' keine ganze Zahl ist oder nicht positiv,
    beende das Programm mit der Fehlermeldung:
        "Knotenanzahl muss eine positive ganze Zahl sein"

    Parameters
    ==========
    knotenanzahl : int
        Anzahl der Knoten im Graph.

    Returns
    =======
    dict
        Ein Dictionary, das einen Graphen repräsentiert.
        graph['alleknoten'] : set
            enthält die Menge aller Knoten.
        graph[(i,j)] : int
            ist UNENDLICH, dabei sind i und j beliebige Knoten und i ist stets kleiner oder gleich j.
    '''  
    if type(knotenanzahl)!= int or knotenanzahl<=0:
       beende_programm("Knotenanzahl muss eine positive ganze Zahl sein.")
    graph={}
    graph['alleknoten'] = set()
    for k in range(0, knotenanzahl):
        graph['alleknoten'].add(k)
    for i in range (0, knotenanzahl):
        for j in range (0, knotenanzahl):
            if i > j :
               graph[(j, i)] = UNENDLICH
            else:
               graph[(i,j)] = UNENDLICH
        #for j in range (i, knotenanzahl):
        #    graph[(i,j)] = UNENDLICH
    return graph 



if __name__ == '__main__':
    '''
    Diese Funktion wird aufgerufen, wenn man das Programm mit
        python kuerzeste_wege.py
    von der Kommandozeile aufruft.

    Hier werden der Graph konstruiert und initialisiert
    sowie die Funktionen zum Berechnen kürzester Wege aufgerufen.
    '''
    # Konstruiere den Graphen als Dictionary.
    knotenanzahl = 6
    # sobald du die methode implementiert hast, kannst du die folgende Zeile aktivieren.
    graph = konstruiere_leeren_graphen(knotenanzahl)

    # Initialisiere alle Kanten fuer unser Problem.
    graph[(0,1)]=10
    graph[(1,2)]=1
    graph[(2,3)]=5
    graph[(3,4)]=7
    graph[(4,5)]=4
    graph[(0,5)]=2
    graph[(0,2)]=4
    graph[(3,5)]=2

    # Finde den kuerzesten Weg zwischen Start und Ziel.
    start = int(sys.argv[1])
    ziel = int(sys.argv[2])
    if start > 5 or ziel > 5 :
       beende_programm('Knoten ist nicht im Graphen')
    if start < 0 or ziel < 0:
       beende_programm('Knoten muss positiv sein')
    abstaende, vorgaenger=berechne_kuerzeste_wege_von(graph, start)
    print(schreibe_weg(start, ziel, abstaende, vorgaenger))
    # ...... dein code .......
    # überprüfe, dass start und ziel nicht identisch sind
    # berechne einen kürzesten Weg von 'start' nach 'ziel' und gib ihn aus.
    # ...... dein code .......









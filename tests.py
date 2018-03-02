# run with: python3.6 -m unittest tests.py

from kuerzeste_wege import *
import sys
import unittest
from contextlib import contextmanager
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

@contextmanager
def captured_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

def init_graph(length=6):
    graph = {}
    # Initialisiere alle Kanten fuer unser Problem.
    graph['alleknoten'] = set()
    for k in range(0, length):
        graph["alleknoten"].add(k)
        for l in range(k, length):
            graph[(k,l)] = UNENDLICH

    if length == 6:
        graph[(0,1)]=10
        graph[(1,2)]=1
        graph[(2,3)]=5
        graph[(3,4)]=7
        graph[(4,5)]=4
        graph[(0,5)]=2
        graph[(0,2)]=4
        graph[(3,5)]=2
    elif length == 4:
        graph[(0,1)]=2
        graph[(0,2)]=2
        graph[(0,3)]=2
        graph[(1,2)]=3
        graph[(1,3)]=3
        graph[(2,3)]=3
    return graph


class TestKuerzesteWege(unittest.TestCase):


    def test_beende_programm(self):
        print("\n==> Teste Methode 'beende_programm(...)'")
        teststring = ("Test1")
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                beende_programm(teststring)
            self.assertEqual(mystdout.getvalue().strip(),teststring)
        teststring = ("Test2")
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                beende_programm(teststring)
            self.assertEqual(mystdout.getvalue().strip(),teststring)
        teststring = ("Test3")
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                beende_programm(teststring)
            self.assertEqual(mystdout.getvalue().strip(),teststring)
        print("===> Methode 'beende_programm(...)' hat den Test bestanden.")


    def test_graph_abstand(self):
        print("\n==> Teste Methode 'graph_abstand(...)'.")
        graph = init_graph()
        testres = [[0,1,10], [1,2,1], [2,3,5], [3,4,7], [4,5,4], [0,5,2], [0,2,4], [3,5,2]]
        for i, j, k in testres:
            self.assertEqual(graph_abstand(graph, i, j), k)
            self.assertEqual(graph_abstand(graph, j, i), k)
        graph.pop((1,4))
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                graph_abstand(graph, 1, 4)
            self.assertEqual(mystdout.getvalue().strip(),"Kann gesuchte Kante im Graphen nicht finden.")
        graph[(2,4)] = 0
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                graph_abstand(graph, 2, 4)
            self.assertEqual(mystdout.getvalue().strip(),"Nichtpositive Kantengewichte sind verboten.")
        graph[(3,4)] = -1
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                graph_abstand(graph, 3, 4)
            self.assertEqual(mystdout.getvalue().strip(),"Nichtpositive Kantengewichte sind verboten.")
        print("===> Methode 'graph_abstand(...) hat den Test bestanden.")


    def test_sind_nachbarn(self):
        print("\n==> Teste Methode 'sind_nachbarn(...)'.")
        graph = init_graph()
        testres = [[0,1], [1,2], [2,3], [3,4], [4,5], [0,5], [0,2], [3,5]]
        for i in range(0, 6):
            for j in range(i, 6):
                if [i,j] in testres:
                    self.assertEqual(sind_nachbarn(graph, i, j), True)
                    self.assertEqual(sind_nachbarn(graph, j, i), True)
                else:
                    self.assertEqual(sind_nachbarn(graph, i, j), False)
                    self.assertEqual(sind_nachbarn(graph, j, i), False)
        print("===> Methode 'sind_nachbarn(...)' hat den Test bestanden.")


    def test_alle_nachbarknoten(self):
        print("\n==> Teste Methode 'alle_nachbarnknoten(...)'")
        graph = init_graph()
        testres = [3, 2, 3, 3, 2, 3]
        for i in range(0, 6):
            nachbarn = alle_nachbarknoten(graph, i)
            self.assertEqual(len(nachbarn), testres[i])
        graph[(1,4)] = 2
        for i in range(0, 6):
            nachbarn = alle_nachbarknoten(graph, i)
            self.assertEqual(len(nachbarn), 3)
        graph[(0,2)] = UNENDLICH
        graph[(1,4)] = UNENDLICH
        graph[(3,5)] = UNENDLICH
        for i in range(0, 6):
            nachbarn = alle_nachbarknoten(graph, i)
            self.assertEqual(len(nachbarn), 2)
        print("===> Methode 'alle_nachbarknoten(...)' hat den Test bestanden.")


    def test_naechster_knoten(self):
        print("\n==> Teste Methode 'naechster_knoten(...)'")
        abstaende = {0: 2, 1: 5, 2: 1, 3: 4, 4: float('inf'), 5: float('inf'), 6: 3 }
        testcases = [ [{ 0, 1, 2, 6 }, 2], [{1}, 1], [{4}, 4], [{2, 5, 6}, 2], [{0, 3, 6}, 0],
                [{1, 4, 6}, 6], [{0, 1, 2, 3, 4, 5, 6}, 2]]
        for i,j in testcases:
            self.assertEqual(naechster_knoten(i,abstaende), j)
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                naechster_knoten({},abstaende)
            self.assertEqual(mystdout.getvalue().strip(),"Knotenmenge darf nicht leer sein.")
        print("===> Methode 'sind_nachbarn(...)' hat den Test bestanden.")


    def test_berechne_kuerzeste_wege_von(self):
        print("\n==> Teste Methode 'berechne_kuerzeste_wege_von(...)'")
        graph = init_graph()
        testres = [[0, [0, 5, 4,4, 6,2], [NICHTS,2,0,5,5,0]],
                   [1, [5, 0, 1,6,11,7], [2,NICHTS,1,2,5,0]],
                   [2, [4, 1, 0,5,10,6], [2,2,NICHTS,2,5,0]],
                   [3, [4, 6, 5,0, 6,2], [5,2,3,NICHTS,5,3]],
                   [4, [6,11,10,6, 0,4], [5,2,0,5,NICHTS,4]],
                   [5, [2, 7, 6,2, 4,0], [5,2,0,5,5,NICHTS]]]
        for i,abst,vorg in testres:
            abstaende, vorgaenger = berechne_kuerzeste_wege_von(graph, i)
            for j in range(len(abst)):
                self.assertEqual(abst[j], abstaende[j])
            for j in range(len(vorg)):
                self.assertEqual(vorg[j], vorgaenger[j])

        graph = init_graph(length=4)
        testres = [[0, [0,2,2,2], [NICHTS,0,0,0]],
                   [1, [2,0,3,3], [1,NICHTS,1,1]],
                   [2, [2,3,0,3], [2,2,NICHTS,2]],
                   [3, [2,3,3,0], [3,3,3,NICHTS]]]
        for i,abst,vorg in testres:
            abstaende, vorgaenger = berechne_kuerzeste_wege_von(graph, i)
            for j in range(len(abst)):
                self.assertEqual(abst[j], abstaende[j])
            for j in range(len(vorg)):
                self.assertEqual(vorg[j], vorgaenger[j])
        print("===> Methode 'berechne_kuerzeste_wege_von(...)' hat den Test bestanden.")


    def test_schreibe_weg(self):
        print("\n==> Teste Methode 'schreibe_weg(...)'")
        abstaende = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6 }
        vorgaenger = {0:NICHTS, 1:0, 2:1, 3:2, 4:3, 5:4, 6:5}
        for i in range(1, 7):
            out = schreibe_weg(0, i, abstaende, vorgaenger)
            vergleich = "Länge des kürzesten Wegs: {}.\nStationen: {}.".format(
                    abstaende[i], " - ".join([str(i) for i in range(0, i+1)]))
            self.assertEqual(out, vergleich)

        abstaende = {0:3, 1:4, 2:5, 3:6, 4:4, 5:0}
        vorgaenger = {0:5, 1:0, 2:0, 3:2, 4:5, 5:NICHTS}
        results = [[0, [5,0]], [1, [5,0,1]], [2, [5,0,2]], [3, [5,0,2,3]], [4, [5,4]] ]
        for i,j in results:
            out = schreibe_weg(5, i, abstaende, vorgaenger)
            vergleich = "Länge des kürzesten Wegs: {}.\nStationen: {}.".format(
                    abstaende[i], " - ".join([str(i) for i in j]))
            self.assertEqual(out, vergleich)

        vorgaenger = {0:NICHTS, 1:0, 2:3, 3:2, 4:3, 5:4, 6:5}
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                schreibe_weg(0, 5, abstaende, vorgaenger)
            self.assertEqual(mystdout.getvalue().strip(),"Wir haben uns verlaufen und sind in einem Kreis gefangen.")
        vorgaenger = {0:NICHTS, 1:0, 2:1, 3:2, 4:3, 5:4, 6:5}
        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                schreibe_weg(3, 1, abstaende, vorgaenger)
            self.assertEqual(mystdout.getvalue().strip(),"Wir sind ins Nichts gelaufen.")

        print("===> Methode 'schreibe_weg(...)' hat den Test bestanden.")


    def test_konstruiere_leeren_graphen(self):
        print("\n==> Teste Methode 'konstruiere_leeren_graphen(...)'")
        for i in range(1, 5):
            graph = konstruiere_leeren_graphen(i)
            self.assertEqual(len(graph), (i*(i+1.0)/2 + 1))
            alleknoten = graph['alleknoten']
            for j in range(0, i):
                self.assertIn(j, alleknoten)
                for k in range(j, i):
                    self.assertEqual(graph[(j,k)], UNENDLICH)
                    if j != k:
                        self.assertNotIn((k,j), graph.keys() )

        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                konstruiere_leeren_graphen(0)
            self.assertEqual(mystdout.getvalue().strip(),"Knotenanzahl muss eine positive ganze Zahl sein.")

        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                konstruiere_leeren_graphen(-2)
            self.assertEqual(mystdout.getvalue().strip(),"Knotenanzahl muss eine positive ganze Zahl sein.")

        with captured_output() as mystdout:
            with self.assertRaises(SystemExit):
                konstruiere_leeren_graphen(0.5)
            self.assertEqual(mystdout.getvalue().strip(),"Knotenanzahl muss eine positive ganze Zahl sein.")

        print("===> Methode 'konstruiere_leeren_graphen(...)' hat den Test bestanden.")


if __name__ == '__main__':
    unittest.main()

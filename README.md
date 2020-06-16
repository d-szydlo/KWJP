# KWJP
Zadania wykonane na kursie Kurs Wybranego Języka Programowania (Python)

## Lista 1
Pobierz Jupyter notebook z zadaniami: Lista 1. Wszystkie rozwiązania wpisz do tego notatnika.

## Lista 2
1. Napisz program, który dla danego pliku tekstowego wróci następujące informacje: liczba bajtów, liczbę słów, liczbę linii oraz maksymalną długość linii.
```
    $ python wordcount.py tekst.txt
    liczba bajtów: 4956
    liczba słów: 1018
    liczba linii: 528
    maksymalna długość linii: 67
```
2. Napisz program, który koduje oraz dekoduje dowolny plik binarny w kodzie Base64. Kod Base64 koduje w taki sposób, że każde kolejne 6 bitów z pliku kodowane jest znakiem ASCII przedstawionych w poniższej tabeli:
```
    tablica = 'ABCD​EFGH​IJKL​MNOP​QRST​UVWX​YZab​cdef​ghij​klmn​opqr​stuv​wxyz​0123​4567​89+/'
```
Na przykład: słowo "Python" kodujemy jako "UHl0aG9u" \
    Kodowanie:
    ```
      $ python base64.py --encode plik.bin plik-enc.txt
    ```\
    Dekodowanie:
    ```
      $ python base64.py --decode plik-enc.txt plik.bin
    ```\
Uwaga: Proszę napisać podstawowe funkcje kodujące i dekodujące bez korzystania np. z biblioteki base64 (lub innych realizujących to zadanie).

3. Napisz program, który zamienia wszystkie nazwy w danym katalogu oraz wszystkich podkatalogach na małe litery. Jako parametr podajemy katalog (zobacz moduł os).
```
    $ python tolower.py ./
```
4. Napisz program, który w danym katalogu znajdzie wszystkie pliki, które powtarzają się więcej niż raz (zobacz os, help(os.walk)). Weź pod uwagę, że pliki mogą mieć różne nazwy, ale tą samą zawartość, dlatego przyjmujemy, że dwa pliki są takie same, jeśli mają taką samą wielkość oraz taką samą wartość funkcji haszującej. Przykład użycia funkcji haszujących:
```
$ python 
>>>>import hashlib
>>>>hashlib.md5('python'​.encode())​.hexdigest()
'23eeeb4347bdd26bfc6b7ee9a3b755dd'\
>>>>hashlib.sha512('python'.encode()).hexdigest()
'ecc579811​643b170​cbd88fd0d0e3​23d1e1ac​c7cef8f73​483a70abea01a89 ...
```
Na wyjściu program wyświetla listę wszystkich plików, które się powtarzają (nazwy plików wraz ze ścieżką)
```
$ python repchecker.py ./
---------------------------------
./plik1.txt
./katalog1/plik5.txt
./katalog3/plik1.dat
---------------------------------
./plik3.txt
./katalog2/plik2.txt
---------------------------------
```

## Lista 3
1. Załóżmy, że reprezentujemy macierze kwadratowe w Pythonie następująco (dla rozmiaru macierzy n=3):
```
m = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
```
Napisz funkcję wykorzystując tylko listy składane, która dokonuje transpozycji takich macierzy (dowolnych rozmiarów) oraz zwraca wynik w tej samej postaci (można to zrobić w jednej linii kodu!).

2. Napisz generator o nazwie "flatten", który przechodzi dowolną listę (również zagnieżdżoną) i podaje po kolei jej elementy. Na przykład dla listy
```
l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
```
Po wywołaniu: ```print(list(flatten(l)))```, otrzymujemy:
```
[1, 2, 'a', 4, 'b', 5, 5, 5, 4, 5, 6, 7, 9, 123, 123, 10]
```
3. Wykorzystując, tylko listy składane (jako generatory) napisz program, który odczytuje plik tekstowy następnie pobiera ostatnią kolumnę, która zawiera informację o wielkości pliku, sumuje i wynik wyświetla na ekranie. Przykład pliku:
```
      127.0.0.1 -  - "GET /ply/  HTTP/1.1" 200 7587
      127.0.0.1 -  - "GET /favicon.ico HTTP/1.1" 404 133
      127.0.0.1 -  - "GET /ply/bookplug.gif" 200 23903
      127.0.0.1 -  - "GET /ply/ply.html HTTP/1.1" 200 97238
      127.0.0.1 -  - "GET /ply/example.html HTTP/1.1" 200 2359
      127.0.0.1 -  - "GET /index.html" 200 4447
```
Dostajemy wynik:
```
Całkowita liczba bajtów: 135667
```

4. Rozważmy algorytm QuickSort napisany w języku Haskell:
```
     qsort [] = []
     qsort (x:xs) = qsort elts_lt_x ++ [x] ++ qsort elts_greq_x\]
                     where
                       elts_lt_x = [y | y <- xs, y < x]
                       elts_greq_x = [y | y <- xs, y >= x]
```
Napisz podobny program w języku Python wykorzystując:
    
- składnie funkcjonalną (filter)
- operacje na listach składanych
5. Poniżej w języku OCAML napisany jest program, który generuje wszystkie podzbiory
```
      let rec allsubsets s =
        match s with
          [] -> [[]]
        | (a::t) -> let res = allsubsets t in
                      map (fun b -> a::b) res @ res;;
       # allsubsets [1;2;3];;
       -: int list list = [[1; 2; 3]; [1; 2]; [1; 3]; [1]; [2; 3]; [2]; [3]; []]
```       
Napisz podobny program w języku Python wykorzystując:
    
- składnie funkcjonalną (map, lambda)
- operacje na listach składanych.

## Lista 4
1. Napisz dekorator, mający za zadanie drukować informacje o czasie wykonywania funkcji.
2. Załóżmy, że mamy drzewo i reprezentujemy je na liście np. drzewo tree\
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)\
reprezentujemy jako ```["1", ["2", ["4", ["8", None, None], ["9",None,None]], ["5",None,None]], ["3", ["6", None, None], ["7", None, None]]]```
Napisz funkcję która generuje w sposób losowy drzewo podanej wysokości oraz generator który przechodzi drzewo w porządku DFS i BFS.
3. Napisz klasę class Node(object) do reprezentacji pojedynczego węzła drzewa z dowolną liczbą potomków. Podobnie jak w zadaniu poprzednim napisz funkcję która generuje losowo drzewo o danej wysokości i generator który przechodzi drzewo w porządku DFS i BFS.
5. Przeciążenie funkcji (function overloading) daje możliwość wykorzystania tej samej nazwy funkcji, ale z różnymi parametrami. Na przykład w innych językach możemy napisać:
```
  float norm(float x, float y) {            // norma Euklidesowa
    return sqrt(x*x + y*y)\
  }\
  float norm(float x, float y, float z) {   // norma taksówkowa
    return abs(x) + abs(y) + abs(z)\
  }
 ```
W języku Python nie ma przeciążenia funkcji, po prostu następna definicja nadpisuje poprzednią. Napisz dekorator nazwijmy go @overload, który pozwala na taką własność. Przykładowy program powinien wyglądać tak:
  ```
  @overload
  def norm(x,y):
    return math.sqrt(x*x + y*y)
  @overload
  def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)
  print(f"norm(2,4) = {norm(2,4)}")
  print(f"norm(2,3,4) = {norm(2,3,4)}")
```
Otrzymujemy:
```
  norm(2,4) = 4.47213595499958
  norm(2,3,4) = 9
```
Wskazówka: Napisz dekorator, który wraca klasę z odpowiednio przeciążonym operatorem __call__, która przechowuje nazwy funkcji z parametrami. Do odróżnienia funkcji można wykorzystać np. getfullargspec(f).args z modułu inspect (from inspect import getfullargspec). 


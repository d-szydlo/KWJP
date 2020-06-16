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
![tree](https://github.com/d-szydlo/KWJP/blob/master/Lista4/l4tree.png)\
reprezentujemy jako ```["1", ["2", ["4", ["8", None, None], ["9",None,None]], ["5",None,None]], ["3", ["6", None, None], ["7", None, None]]]```
Napisz funkcję która generuje w sposób losowy drzewo podanej wysokości oraz generator który przechodzi drzewo w porządku DFS i BFS.
3. Napisz klasę class Node(object) do reprezentacji pojedynczego węzła drzewa z dowolną liczbą potomków. Podobnie jak w zadaniu poprzednim napisz funkcję która generuje losowo drzewo o danej wysokości i generator który przechodzi drzewo w porządku DFS i BFS.
5. Przeciążenie funkcji (function overloading) daje możliwość wykorzystania tej samej nazwy funkcji, ale z różnymi parametrami. Na przykład w innych językach możemy napisać:
```
  float norm(float x, float y) {            // norma Euklidesowa
    return sqrt(x*x + y*y)
  }
  float norm(float x, float y, float z) {   // norma taksówkowa
    return abs(x) + abs(y) + abs(z)
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

## Lista 5
1. Napisz wykorzystując regresję liniową program, który na podstawie oceny filmów przez użytkowników będzie starał się przewidzieć ocenę innych użytkowników. Jako dane wykorzystamy zbiór MovieLens Latest Datasets. Dokładnie wybierzemy mniejszy zbiór, pobierz plik ml-latest-small.zip. Zadanie polega na wybraniu z pliku ratings.csv tych użytkowników (userId), którzy ocenili film 'Toy Story (1995)', który w tym pliku ma identyfikator '1' (patrz movies.csv). W tym pliku osób takich jest 215. Wtedy zgodnie z zapisem z wykładu x<su>ij</sub> będzie oceną i-tego użytkownika dla i = 0,1, ..., 214, bo taki jest nasz zbiór osób, które oceniły 'Toy Story' oraz j będzie oceną j-tego filmu dla j = 0, ..., m. Jako j
 można wybrać movieId filmu, czyli np. film o movieId = 42 oceniony przez użytkownika 5 (nie jest to userId, tylko piąta osoba ze zbioru 215 osób), który ocenił film jako np. 3.5 wpisujemy x[5,42] = 3.5. Natomiast y<sub>i</sub> to ocena 'Toy Story' przez i-tego użytkownika. Zatem tworzymy macierz X = [x<su>ij</sub>] oraz wektor y<su>i</sub> gdzie i = 0, ...,215 oraz j=0, ...,m. Dla tak przygotowanych danych wykonujemy:
* regresje liniową na całym zbiorze użytkowników dla m =10, 1000, 10000, czyli np. dla m = 10 ignorujemy filmy o movieId > 10 i robimy regresje dla tak okrojonego zbioru ocen. Jakie dostajemy błędy. Pokaż na wykresie.
* podziel zbiór osób na tzw. zbiór treningowy oraz zbiór testowy np. weźmy i = 0, ..., 200 to będzie zbiór treningowy i na takim zbiorze osób wykonajmy regresje natomiast później sprawdzamy już dla całości (215). Zatem ostatnie 15 ocen będziemy chcieli przewidzieć (zbiór testowy). Zrób przewidywanie dla m = 10, 100, 200, 500, 1000, 10000. Wyświetl wynik predykcji i wynik prawidłowy dla tych 15 osób.

Przykład danych do regresji jakie otrzymujemy dla m = 10 i n = 215:
```
X = [[0.  4.  0.  0.  4.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
     [3.  0.  0.  0.  4.  0.  0.  0.  0.  0. ]
     [3.  3.  0.  0.  0.  2.  0.  0.  2.  0. ]
     [3.5 0.  0.  0.  0.  0.  0.  0.  5.  0. ]
     ...
y = [[4. ]
     [4. ]
     [4.5]
     [2.5]
     [4.5]
     [3.5]
     [4. ]
     [3.5]
     ...
```

2. Napisz system rekomendacji filmów. Systemy takie są wykorzystywane przez różne firmy np. Netflix organizował konkurs na opracowanie algorytmu, który będzie przewidywał ocenę użytkownika (Netflix Prize). W zadaniu tym zaimplementujemy podobny system, który jednak zamiast przewidywania będzie na podstawie preferencji użytkownika rekomendował filmy, które najprawdopodobniej mu się spodobają. Istnieje wiele sposobów, aby taki system napisać, dla zainteresowanych bardziej tematem proponuje zobaczyć np. Recommendation Systems. W tym zadaniu wybierzemy w miarę prosty i łatwy do implementacji system rekomendacji. Sformalizujmy problem. Załóżmy, że mamy macierz oceny, gdzie wiersze będą reprezentować użytkowników a kolumny filmy np.

użytkownik | Matrix | Star Wars IV
------------ | ------------- | -------------
Alice | 5 | 4
Bob | 0 | 1
John | 2 | 2
Ada | 5 | 5

Patrząc na powyższą macierz widać, że kolumny pierwsza i druga mają podobne oceny stąd można wywnioskować, że filmy Matrix i Star Wars IV są (według użytkowników) podobne do siebie, czyli jeśli komuś podobał się Matrix to jest duża szansa, że będzie podobał mu się Star Wars i odwrotnie. Dlatego "podobieństwo" sformalizujemy przez wykorzystanie podobieństwa cosinusowego.
```
>>> x = np.array([[5,0,2,5], [4,1,2,5]]).T
>>> x
array([[5, 4],
       [0, 1],
       [2, 2],
       [5, 5]])

# obliczamy normę wektorów kolumnowych
>>> np.linalg.norm(x, axis=0)
array([7.34846923, 6.78232998])

# obliczamy znormalizowaną macierz
>>> x/np.linalg.norm(x, axis=0)
array([[0.68041382, 0.58976782],
       [0.        , 0.14744196],
       [0.27216553, 0.29488391],
       [0.68041382, 0.73720978]])

# teraz weźmy własną ocenę filmów Matrix - 4, Star Wars IV - 3
# dla wygody zapisujemy jako wektor kolumnowy
>>> y = [[4],[3]]

# obliczamy podobieństwo cosinusowe z każdym użytkownikiem (skorzystamy z mnożenia macierzowego)
>>> z=np.dot(x/np.linalg.norm(x, axis=0), np.array(y)/np.linalg.norm(y))
>>> z
array([[0.89819175],
       [0.08846517],
       [0.39466277],
       [0.98665692]])

# normalizujemy otrzymany wektor (będzie on reprezentował nasz profil filmowy)
>>> z/np.linalg.norm(z)
array([[0.64422929],
       [0.06345177],
       [0.28307243],
       [0.70768107]])
```
Teraz musimy obliczyć podobieństwo cosinusowe między naszym profilem a każdą kolumną macierzy, aby znaleźć takie filmy, które są podobne do naszego profilu. Sortujemy po otrzymanym podobieństwu i dostajemy rekomendacje. Wykorzystując nasz przykład, otrzymujemy
```
>>> X = x/np.linalg.norm(x, axis=0)
>>> Z = z/np.linalg.norm(z)
>>> np.dot(X.T, Z)
array([[0.99690104],
        [0.99448407]])
```
Stąd dostaliśmy większą rekomendacje dla filmu Matrix (0.996) niż Star Wars IV (0.994). Co było oczywiście oczekiwane skoro nasza ocena była Matrix - 4, a Star Wars IV - 3. Możemy, teraz przejść do właściwej części zadania. Napisz system rekomendacji filmów który będzie wykorzystywał dane MovieLens Latest Datasets. Dokładnie mniejszy zbiór (który dodatkowo trochę jeszcze zmniejszymy). Pobierz plik ml-latest-small.zip. Interesować, będą nas głównie dwa pliki movies.csv oraz ratings.csv. W pliku ratings.csv mamy właściwie wszystkie dane, które będą nam potrzebne aby stworzyć macierz oceny. Ponieważ nawet w tym przypadku otrzymana macierz będzie dość duża dlatego w trakcie wczytywania danych z pliku proszę wziąć pod uwagę tylko te wiersze (z pliku ratings.csv) w których movie_id (druga kolumna) jest mniejsze od 10000 (resztę ignorujemy). Dla aktualnych danych ze strony otrzymamy, wtedy macierz mniej więcej 611x9019. Przykładowy wynik dla wybranego profilu filmowego:
```
# wektor my_ratings odpowiada wektorowi y z przykładu wyżej
my_ratings = np.zeros((9019,1))
my_ratings[2571] = 5      # patrz movies.csv  2571 - Matrix
my_ratings[32] = 4        # 32 - Twelve Monkeys
my_ratings[260] = 5       # 260 - Star Wars IV
my_ratings[1097] = 4
my_ratings_norm = my_ratings/np.linalg.norm(my_ratings)

...

# otrzymujemy wynik rekomendacji po posortowaniu
# (cos(θ), movies_id)
(0.8675507828468105, 260)
(0.8362098349303669, 2571)
(0.8227451213877744, 1196)
(0.8002349214247857, 1210)
(0.7458504689612442, 1097)
(0.7286029159733108, 32)
(0.7265369898748615, 1198)
(0.7095672455110477, 1240)
(0.7029872178855614, 1270)
```
Otrzymane reprezentacje wyświetl w postaci nazw filmów, korzystając z movies.csv. Uwaga: w rzeczywistych danych otrzymamy dużą liczbę zer, nawet całe kolumny, wtedy dostaniemy wartości NaN przy dzieleniu! Rozwiąż ten problem wykorzystując np.nan_to_num(...).

3. Napisz rekomendacje dla pełnego zbioru danych ml-latest.zip. Wykorzystaj do tego macierze rzadkie (sparse matrix) np. z pakietu scipy (lub inny sposób, który pozwala na obróbkę tak dużej ilości danych).

## Lista 6
1. Zaimplementuj algorytm propagacji wstecznej przedstawiony na wykładzie 9 dla sieci neuronowej 3-4-1 (3-wejścia, 4-warstwa ukryta, 1-wyjście). Rozwiąż pokazany problem XOR. Następnie:
- zamiast funkcji sigmoidalnej wykorzystaj funkcje aktywacji ReLU,
- wykorzystaj kombinacje funkcji sigmoidalnej σ z ReLU np. warstwa ukryta ma σ a warstwa wyjściowa jest ReLU lub inne kombinacje. Poeksperymentuj!

Które rozwiązanie daje lepszą dokładność? Odpowiedź na to pytanie pisząc program testowy, który to pokazuje (np. po uruchomieniu w terminalu dostajemy wyniki dla różnych kombinacji z opisem). Rozwiąż ten problem również dla innych funkcji logicznych AND i OR. Dlaczego w danych wejściowych z przykładu z wykładu mamy ostatnią kolumnę z samymi jedynkami. Na to pytanie odpowiedź w komentarzu kodu źródłowego programu.

2. Zaprojektuj sieć neuronową dwuwarstwową do aproksymacji funkcji np. sieć 1-5-1 lub 1-10-1 itp. i naucz ją funkcji (jedna funkcja dla jednej sieci)
- Weźmy dane wejściowe, jako próbkowana funkcja paraboliczna
```
>>> x=np.linspace(-50,50,26)
>>> y=x**2
>>> plt.scatter(x,y)
```
Sieć testuj dla wektora wejściowego
```
>>> x=np.linspace(-50,50,101)
>>> y - wynik sieci dla wejścia x
>>> plt.scatter(x,y)
```
- Weźmy dane wejściowe, jako próbkowana funkcja sinus
```
>>> x = np.linspace(0,2,21)
>>> y = np.sin((3*np.pi/2) * x)
>>> plt.scatter(x,y)
```
Sieć testuj dla wektora wejściowego
```
>>> x = np.linspace(0,2,161)
>>> y = wynik sieci dla wejścia x
>>> plt.scatter(x,y)
```
Dobierz też odpowiednie dla problemu funkcje aktywacji! Dokładnie σ, ReLU lub tanh. W czasie uczenia pokazuj aproksymacje funkcji co np. 100 krok, czyli co 100 krok np. dla funkcji parabolicznej dla wektora x = np.linspace(-50,50,101) pokaż wynik działania sieci wykorzystując matplotlib. Dostaniemy animacje procesu uczenia sieci. Wyświetlaj jeszcze aktualny krok uczenia oraz błąd średnio-kwadratowy. Animacje procesu uczenia wykonaj dla dwóch powyższych zbiorów danych (parabola i sinus).

3. Wykonaj zadanie drugie dla sieci o trzech warstwach np. 1-10-10-1. Sam napisz algorytm propagacji wstecznej dla sieci trójwarstwowej. Jakie wyniki aproksymacji dostaniemy dla tej ,,głębszej'' sieci?

## Lista 7
1. Wykonaj zadanie 2 z listy 6 z wykorzystaniem Kerasa i Tensorflow. Wykonaj testy dla kilku funkcji aktywacji oraz dla wielu warstw sieci. Poeksperymentuj!
2. Wykorzystując architekturę sieci neuronowych RetinaNet Focal Loss for Dense Object Detection zaprogramuj wykrywanie obiektów. Możesz np. skorzystać z implementacji sieci w Kerasie razem z modelem uczonym na danych COCO object detection dataset. Pobierz nauczoną sieć w kerasie resnet50_coco_best_v2.1.0.h5 i przeprowadź wykrywanie obiektów dla COCO dataset.

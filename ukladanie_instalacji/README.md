Projekt zawiera realizację problemu poszukiwania optymalnego ułożenia sieci wodociągowej za pomocą algorytmu genetycznego i symulowanego wyżarzania. Szczegóły projektu opisane są w pliku Dokumentacja.pdf.

Projekt realizowany w grupie trzyosobowej, napisany w języku Python.

# Projekt zawiera następujące pliki:

Kod programu:
-algorytm_genetyczny.py - implementacja algorytmu genetycznego
-algorytm_konstrukcyjny.py - implementacja algorytmów generujących rozwiązania początkowe
-implementacja_problemu.py - implementacja struktur i klas służących do opisu problemu
-main.py - implementacja GUI, plik do uruchomienia programu
-SA.py - implementacja algorytmu symulowanego wyżarzania i mutacji z algorytmu genetycznego
-testy.py - testy różnych funkcji i algorytmów, kody generujące testy algorytmów SA i genetycznego i zapisujące wyniki do pliku
-wczytywanie_danych.py - algorytm służący do wczytania danych z pliku
-wyrysowywanie_rozwiązania.py - kod służący do wizualizacji rozwiązania

Dane do projektu:
-DANE.xlsx - plik z danymi, na których pracowaliśmy. W celu przetestowania algorytmów dla innych danych należy zmienić dane w tym pliku

Wyniki testów:
-folder EA_tests - wyniki testów algorytmu genetycznego

Opracowanie wyników:
-Dokumentacja.pdf

# Uruchomienie projektu:
Pakiety potrzebne do uruchomienia kodu to PySimpleGUI, numpy i pandas.
Aby uruchomić program zawierający algorytmy, należy otworzyć plik main.py i uruchomić kod. Po uruchomieniu zostanie wyświetlone główne menu programu, w którym można zmienić parametry funkcji celu oraz wybrać algorytm. W przypadku algorytmu genetycznego dotkliwość kary za niezaspokojenie punktów poboru powinna być 100 razy większa niż pozostałe wagi, by algorytm działał prawidłowo.
Po wybraniu algorytmu, otwarte zostanie okno, w którym można wybrać parametry odpowiedniego algorytmu. Po wciśnięciu przycisku Start algorytm zacznie pracę, po czym wyświetli rezultaty w polu tekstowym poniżej. Istnieje też możliwość powrotu do głównego menu, dzięki czemu można sprawnie testować oba algorytmy bez konieczności uruchamiania od nowa kodu programu.



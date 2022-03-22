Projekt realizujący system służący do modelowania i symulacji działania sieci na przykładzie linii produkcyjnej w fabryce. Realizowany w grupie trzyosobowej. Wykorzystano w nim programowanie obiektowe w języku C++. Projekt został napisany w środowisku CLion.

# Opis problemu:
Linia produkcyjna składa się z węzłów połączonych w spójną całość:
- rampy rozładunkowe
- robotnicy
- magazyny.
W ramach procesu technologicznego dopuszczalne są następujące połączenia:
- rampa rozładunkowa -> robotnik
- robotnik -> robotnik
- robotnik -> magazyn.

Należało zaprojektować i zasymulować działanie takiej sieci od dostarczenia półproduktu na rampę do zmagazynowania gotowego wyrobu.

# Foldery w projekcie:
- diagram-UML zawierający diagramy UML do niektórych etapów projektu
- include zawierający pliki nagłówkowe projektu
- src zawierający pliki źródłowe projektu
- test zwierający testy jednostkowe
- mocks - folder pomocniczy, potrzebny do prawidłowego działania testów
- folder googletest-master(należy go pobrać wcześniej) i plik CMakeLists niezbędne do prawidłowego uruchomienia i działania projektu w środowisku CLion

# Uruchomienie projektu:
W celu poprawnego uruchomienia projektu należy najperw w folderze z projektem (folder bieżący) utworzyć folder googletest-master i pobrać do niego pliki z poniższego repozytorium:

https://github.com/google/googletest


# Rozszerzenie programu do zarządzania plikami csv

# Napisz program oparty na klasach i dziedziczeniu, który odczyta wejściowy plik, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.
#
# Uruchomienie programu przez terminal:
# python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>
#
#  <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv, in.json lub in.txt
#  <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv, out.json, out.txt lub out.pickle
#  <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.
#
# Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.json”.
#
# Przykład działania:
# python reader.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# Z pliku in.json ma wyjść plik out.csv:
# gitara,3,7,0
# kanapka,12,5,kubek
# pedzel,17,34,5
# plakat,czerwony,8,0
# Wymagane formaty:
#
# .csv
# .json
# .txt
# .pickle

import sys

from obsluga_plikow import ObslugaCSV, ObslugaTXT, ObslugaPKL, ObslugaJSON
from utils import sprawdz_argumenty, sprawdz_indexy

# sprawdzam czy użytkownik wpisał odpowidnią liczbę argumentów i czy plik wejściowy istnieje
if sprawdz_argumenty(sys.argv):

    argumenty = sys.argv
    sciezka_in = argumenty[1]
    sciezka_out = argumenty[2]
    modyfikacje = argumenty[3:]

    # tworzymy obiekt plik_wejsciowy w zależności od podanego rozszerzenia
    if sciezka_in.endswith(".csv"):
        plik_wejsciowy = ObslugaCSV(sciezka_in, sciezka_out, modyfikacje)
    elif sciezka_in.endswith(".txt"):
        plik_wejsciowy = ObslugaTXT(sciezka_in, sciezka_out, modyfikacje)
    elif sciezka_in.endswith(".pkl"):
        plik_wejsciowy = ObslugaPKL(sciezka_in, sciezka_out, modyfikacje)
    elif sciezka_in.endswith(".json"):
        plik_wejsciowy = ObslugaJSON(sciezka_in, sciezka_out, modyfikacje)

    # tworzymy obiekt plik_wyjsciowy w zależności od podanego rozszerzenia
    if sciezka_out.endswith(".csv"):
        plik_wyjsciowy = ObslugaCSV(sciezka_in, sciezka_out, modyfikacje)
    elif sciezka_out.endswith(".txt"):
        plik_wyjsciowy = ObslugaTXT(sciezka_in, sciezka_out, modyfikacje)
    elif sciezka_out.endswith(".pkl"):
        plik_wyjsciowy = ObslugaPKL(sciezka_in, sciezka_out, modyfikacje)
    elif sciezka_out.endswith(".json"):
        plik_wyjsciowy = ObslugaJSON(sciezka_in, sciezka_out, modyfikacje)

    # wczytujemy dane
    dane = plik_wejsciowy.wczytaj_dane()

    # sprawdzam czy użytkownik wpisał prawidłowe numery kolumn i wierszy
    if sprawdz_indexy(sys.argv, dane):
        print("Dane przed modyfikacją:")
        plik_wejsciowy.wyswietl_dane()

        # modyfikujemy dane
        plik_wejsciowy.modyfikuj_dane()
        plik_wyjsciowy.dane = plik_wejsciowy.dane

        print("\nDane po modyfikacji")
        plik_wyjsciowy.wyswietl_dane()

        # zapisujemy dane do wskazanego pliku out
        plik_wyjsciowy.zapisz_dane()



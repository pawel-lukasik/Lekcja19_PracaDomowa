import os

def sprawdz_argumenty(argumenty):
    """
    sprawdza czy użytkownik wpisał odpowidnią liczbę argumentów i czy plik wejściowy istnieje
    """
    if  len(argumenty) < 6 or (len(argumenty) - 3) % 3 != 0: # co najmniej 6 arg. Po odjęciu 3 pierwszych liczba pozostałych powinna być podzielna przez 3
        print("""
        Wpisałeś błędną liczbę argumentów!
        Prawidłowe użycie: 'python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ...'
        <zmiana_x> - zmiana w postaci 'x y wartość', x to nr kolumny, y to nr wiersza, wartość to nowa wartość dla wskazanej komórki.
        Program obsługuje formaty: .csv, .txt, .json, .pkl
        """)
        return False

    # sprawdzam czy podany plik wejściowy istnieje
    elif not os.path.exists(argumenty[1]):
         print(f"\nPodany plik wejściowy: '{argumenty[1]}' nie istnieje!\n")
         return False

    # sprawdzam czy podany plik wejściowy ma zawartość
    elif os.path.getsize(argumenty[1]) == 0:
        print(f"\nPodany plik wejściowy: '{argumenty[1]}' jest pusty!\n")
        return False

    # sprawdzamy rozszerzenie pliku wejściowego
    elif not argumenty[1].lower().endswith((".csv", ".txt", ".pkl", ".json")):
        print(f"\nBłędny format pliku wejściowego: '{argumenty[1]}'. Obsługiwane formaty: .csv, .txt, .json, .pkl\n")
        return False

    # sprawdzamy rozszerzenie pliku wyjściowego
    elif not argumenty[2].lower().endswith((".csv", ".txt", ".pkl", ".json")):
        print(f"\nBłędny format pliku wyjściowego: '{argumenty[2]}'. Obsługiwane formaty: .csv, .txt, .json, .pkl\n")
        return False

    # kiedy wpisane argumenty są prawidłowe
    else:
        print(f"""
Wprowadzone argumenty:
- plik wejściowy: '{argumenty[1]}',
- plik wyjściowy: '{argumenty[2]}',
- modyfikacje: {argumenty[3:]}
        """)
        return True

def sprawdz_indexy(argumenty, dane):
    """
    Sprawdza czy numery kolumn i wierszy są prawidłowe
    """
    czy_ok = False
    for i in range(3, len(argumenty), 3):       # zaczynam od 3 argumentu i iteruję co 3
        x = int(argumenty[i])
        y = int(argumenty[i + 1])

        # sprawdzam x czyli nr kolumny
        if x < 0 or x >= len(dane[0]):
            print(f"Podałeś błędny nr kolumny '{x}'. Dostępne kolumny od 0 do {len(dane[0])-1}")
            print("Zmiany nie zostały wprowadzone.\n")
            czy_ok = False

        # sprawdzam y czyli nr wiersza
        elif y < 0 or y >= len(dane):
            print(f"Podałeś błędny nr wiersza '{y}'. Prawidłowy index od 0 do {len(dane)-1}")
            print("Zmiany nie zostały wprowadzone.\n")
            czy_ok = False

        # jesli numery kolumn i wierszy są prawidłowe
        else:
            czy_ok = True

    if czy_ok:
        return True
    else:
        return False


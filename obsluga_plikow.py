import pickle
import csv
import json
from abc import ABC, abstractmethod


class ObslugaPlikow(ABC):
    def __init__(self, plik_wejsciowy, plik_wyjsciowy, modyfikacje):
        self.plik_wejsciowy = plik_wejsciowy
        self.plik_wyjsciowy = plik_wyjsciowy
        self.modyfikacje = modyfikacje
        self.dane = None

    @abstractmethod
    def wczytaj_dane(self):
        pass

    @abstractmethod
    def zapisz_dane(self):
        pass

    def wyswietl_dane(self):
        for wiersz in self.dane:
            text = ""
            for komorka in wiersz:
                text += komorka.ljust(15)
            print(text)

    def modyfikuj_dane(self):
        for i in range(0, len(self.modyfikacje), 3):       # iteruję od 0 i co 3 elementy
            x = int(self.modyfikacje[i])
            y = int(self.modyfikacje[i+1])
            wartosc = self.modyfikacje[i+2]
            self.dane[y][x] = wartosc
        return self.dane

class ObslugaCSV(ObslugaPlikow):
    def wczytaj_dane(self):
        with open(self.plik_wejsciowy, "r", encoding="utf-8") as plik:
            dane_csv = csv.reader(plik)
            self.dane = list(dane_csv)
        return self.dane

    def zapisz_dane(self):
        with open(self.plik_wyjsciowy, "w", newline="",
                  encoding="utf-8") as plik:  # newline="" usuwa problem pustych wierszy w pliku csv (dotyczy windows)
            writer = csv.writer(plik)
            writer.writerows(self.dane)
        print(f"\nZmiany zapisano do pliku '{self.plik_wyjsciowy}'\n")

class ObslugaTXT(ObslugaPlikow):
    def wczytaj_dane(self):
        data = []
        with open(self.plik_wejsciowy, "r", encoding="utf-8") as plik:
            for linia in plik:
                wiersz = linia.strip().split(",") # strip usuwa białe znaki, split dzieli strin na listę po przecinkach
                data.append(wiersz)
                self.dane = data
        return self.dane

    def zapisz_dane(self):
        with open(self.plik_wyjsciowy, "w", encoding="utf-8") as plik:
            for row in self.dane:
                plik.write(",".join(row) + "\n")
        print(f"\nZmiany zapisano do pliku '{self.plik_wyjsciowy}'\n")

class ObslugaPKL(ObslugaPlikow):
    def wczytaj_dane(self):
        with open(self.plik_wejsciowy, mode="rb") as plik:
            self.dane =  pickle.load(plik)
        return self.dane

    def zapisz_dane(self):
        with open(self.plik_wyjsciowy, mode="wb") as plik:
            plik.write(pickle.dumps(self.dane))
        print(f"\nZmiany zapisano do pliku '{self.plik_wyjsciowy}'\n")

class ObslugaJSON(ObslugaPlikow):
    def wczytaj_dane(self):
        with open(self.plik_wejsciowy, mode="r", encoding="utf-8") as plik:
            self.dane = json.load(plik)
        return self.dane

    def zapisz_dane(self):
        with open(self.plik_wyjsciowy, mode="w", encoding="utf-8") as plik:
            json.dump(self.dane, plik, ensure_ascii=False, indent=4)
            #  ensure_ascii=False polskie znaki nie zamienią się na krzaki, indent=4 zapis do pliku z wcięciami

        print(f"\nZmiany zapisano do pliku '{self.plik_wyjsciowy}'\n")
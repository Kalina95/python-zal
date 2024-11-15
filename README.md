# Algorytmy i struktury danych w języku python
## Projekt Zaliczeniowy - Aplikacja do pobierania i wizualizacji cen złota i walut

### Technologie:
- Python
- Pandas
- Matplotlib
- Tkinter

### Opis Aplikacji:
Aplikacja jest narzędziem do pobierania oraz wizualizacji cen złota i dolara. Działa w oparciu o dane z API Narodowego Banku Polskiego (link do dokumentacji: https://api.nbp.pl/) i zapisuje je w plikach lokalnych. 

Logika aplikacji została podzielona na pakiety:
- model - model zbieranych danych.
- service - warstwa obróbki zebranych danych oraz integracaę z NBP API.
- view - warstwa widoku. Pokazanie graficznego interfejsu użytkownika oraz danych w formie logów lub wykresu.
 
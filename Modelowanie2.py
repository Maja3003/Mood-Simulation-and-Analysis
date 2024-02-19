import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def generuj_nastroj():
    # Czy były zajęcia
    byly_zajecia = random.uniform(-8, 8)

    # Ile czasu wolnego
    czas_wolny = random.choice([-12, 5, 12])

    # Czy widziałeś się ze znajomymi
    spotkanie_ze_znajomymi = random.uniform(-12, 12)

    # Czy wyspałeś się w nocy
    dobrze_wyspany = random.uniform(-10, 10)

    # Jaka jest pogoda na zewnątrz
    pogoda = random.choice([-15, 5, 15])

    # Nastroj na koniec dnia
    nastroj_poczatkowy = random.gauss(50,2)
    nastroj = nastroj_poczatkowy + (byly_zajecia + czas_wolny + spotkanie_ze_znajomymi + dobrze_wyspany + pogoda) 

    if nastroj > 100:
      nastroj = 100
    if nastroj < 0:
      nastroj = 0

    return nastroj

# Generowanie danych do histogramu
liczba_prob = 6000
nastroje = [generuj_nastroj() for _ in range(liczba_prob)]

# Zapis wyników do pliku
with open('wyniki_symulacji.txt', 'w') as file:
    for nastroj in nastroje:
        file.write(f'{nastroj}\n')

# Tworzenie histogramu
plt.hist(nastroje, bins=30, color='darkviolet', edgecolor='black', alpha=0.7, density=True)
plt.title('Histogram Nastroju na Koniec Dnia')
plt.xlabel('Nastroj')
plt.ylabel('Liczba przypadków')
plt.xlim(0, 100)

# Obliczenie parametrów rozkładu normalnego
mu, std = norm.fit(nastroje)

# Wygenerowanie danych do krzywej
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

# Wykreślenie krzywej dopasowania
plt.plot(x, p, 'k', linewidth=2, label='Dopasowany rozkład normalny')

plt.xlabel("Wartości: \n Średnia (mu): {} \n Odchylenie standardowe (std): {}".format(mu, std))
plt.legend()
plt.legend()
plt.savefig('wykres_histogram.jpeg')
plt.tight_layout() 

plt.show()
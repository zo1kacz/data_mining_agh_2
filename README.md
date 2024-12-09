Testy:

Skupiłyśmy się na doborze wybranych hiperparametrach i optymalizatorach:
- Hiperparametry treningu:
Liczba epok (domyślnie 3)
Rozmiar batcha (domyślnie 64)
Learning Rate (domyślnie 0.01)
- Optymalizator:
Zamiana SGD na Adam

Wnioski: 
- Maksymalna Dokładność: Osiągnięta przy średniej wielkości batcha (32) oraz optymalizatorze SGD, co wskazuje na wysoką skuteczność w tym przypadku.
- Minimalna Dokładność i Najmniejsza Stabilność: Duży batch (256) powoduje niższą i bardzo zmienną dokładność, co może wskazywać, że nie jest to optymalne ustawienie.
- Największa Stabilność: Mały batch (16) zapewnia wysoką i przewidywalną dokładność, co sugeruje lepsze generalizowanie modelu.


Dokładne wyniki testów:
1. Konfiguracja z Maksymalną Dokładnością:
Średnia Dokładność: 97,26%
Odchylenie Standardowe: 0,56 
Szczegóły Konfiguracji: {'optimizer': 'SGD', 'epochs': 6, 'batch_size': 32, 'lr': 0.01}

2. Konfiguracja z Minimalną Dokładnością:
Średnia Dokładność: 95,36%
Odchylenie Standardowe: 1,75 (najmniej stabilna)
Szczegóły Konfiguracji: {'optimizer': 'SGD', 'epochs': 6, 'batch_size': 256, 'lr': 0.01}

3. Najmniej Stabilna Konfiguracja:
Średnia Dokładność: 95,36%
Odchylenie Standardowe: 1,75
Szczegóły Konfiguracji: {'optimizer': 'SGD', 'epochs': 6, 'batch_size': 256, 'lr': 0.01}

4. Najbardziej Stabilna Konfiguracja:
Średnia Dokładność: 96,86%
Odchylenie Standardowe: 0,48
Szczegóły Konfiguracji: {'optimizer': 'SGD', 'epochs': 6, 'batch_size': 16, 'lr': 0.01}

Dodatkowo:
- najmniejszą pojedyńczą dokładność uzyskano dla konfiguracji {'optimizer': 'SGD'	 'epochs': 10	 'batch_size': 256	 'lr': 0.01}, 91.87%, epoka nr 1
- największą pojedyńczą dokładność uzyskano dla konfiguracji {'optimizer': 'SGD'	 'epochs': 20	 'batch_size': 256	 'lr': 0.01} 97.94%, epoka nr 19


# Sprint 6 - Avtotesty dlya Яндекс.Самокат

## Obzor proekta
Avtomatizirovannye UI-testy dlya servisa Samokat s ispol'zovaniem Selenium, Pytest, Allure i Page Object Pattern.

## Struktura proekta
Sprint_6/
├── pages/ # Page Object klassy
│ ├── base_page.py # Bazovyy klass s obshchimi metodami i Allure steps
│ ├── main_page.py # Vzaimodeystviya s glavnoy stranitsey
│ └── order_page.py # Vzaimodeystviya s formoy zakaza
├── locators/ # Lokatory dlya stranits
│ ├── main_page_locators.py
│ └── order_page_locators.py
├── tests/ # Testovye sluchai
│ ├── test_faq.py # Testy dlya razdelа FAQ (8 testov)
│ ├── test_logos.py # Testy redirectov logotipov (2 testa)
│ └── test_order_flow.py # Testy protsessa zakaza (2 testa)
├── utilities/
│ └── config.py # Nastrojki konfiguratsii
├── conftest.py # Konfiguratsiya Pytest (fixtures)
├── pytest.ini # Nastrojki Pytest
├── requirements.txt # Zavisimosti
└── README.md # Etot fayl

## Pokrytie testami

### 1. Razdel FAQ (8 testov)
- Testiruyut vse voprosy v razdele "Voprosy o vazhnom"
- Proveryayut, chto pri klikе na vopros poyavlyayetsya pravil'nyy tekst otveta
- Parametrizatsiya dlya vsekh 8 voprosov s proverkoy tochnogo teksta

### 2. Redirecty logotipov (2 testa)
- **Logotip Samokata**: perenapravlyayet na glavnuyu stranitsu
- **Logotip Yandeksa**: otkryvayet Yandeks Dzen v novom okne

### 3. Protsess zakaza (2 testa)
- **Zakaz cherez verkhnyuyu knopku**: Ivan Ivanov, chernyy samokat, arenda na 1 den'
- **Zakaz cherez nizhnyuyu knopku**: Anna Petrova, seryy samokat, arenda na 2 dnya

## Ispol'zuyemyye tekhnologii
- **Python 3.13**
- **Selenium WebDriver**
- **Pytest** + **Allure** otchety
- **Page Object Model** pattern
- **Mozilla Firefox** brauzer

## Klyuchevyye osobennosti
- Polnaya realizatsiya **Page Object Model**
- **Yavnyye ozhidaniya** (WebDriverWait) vmesto time.sleep()
- **Allure steps** vo vsekh metodakh vzaimodeystviya
- **Atomarnyye testy** bez uslovnoy logiki
- **Izolirovannyye lokatory** v otdel'nykh faylakh

## Zavisimosti
```txt
selenium==4.15.0
pytest==7.4.0
allure-pytest==2.15.0
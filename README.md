# Sprint 6 - Avtotesty dlya Яндекс.Самокат

## 📋 Obzor proekta
Avtomatizirovannye UI-testy dlya servisa Samokat s ispol'zovaniem Selenium, Pytest i Page Object Pattern.

## Pokrytie testami

### 1. Razdel FAQ (8 testov)
- Testiruyut vse voprosy v razdele "Voprosy o vazhnom"
- Proveryayut, chto otvety poyavlyayutsya pri klikе na voprosy
- Ispol'zuyetsya parametrizatsiya dlya vsekh 8 voprosov

### 2. Redirecty logotipov (2 testa)
- **Logotip Samokata**: perenapravlyayet na glavnuyu stranitsu
- **Logotip Yandeksa**: otkryvayet Yandeks Dzen v novom okne

### 3. Protsess zakaza (2 testa)
- **Pozitivnye stsenarii** s razlichnymi naborami dannykh
- **Dve tochki vkhoda**: verkhnyaya i nizhnyaya knopki "Zakazat'"
- **Polnyy protsess**: zapolnenie formy → podtverzhdeniye → uspeshnyy modal
- **Testovyye dannyye**:
  - Nabor 1: Ivan Ivanov, chernyy samokat, arenda na 1 den'
  - Nabor 2: Anna Petrova, seryy samokat, arenda na 2 dnya

## Ispol'zuyemyye tekhnologii
- **Python 3.13**
- **Selenium WebDriver**
- **Pytest** + **Allure** otchety
- **Page Object Model** pattern
- **Mozilla Firefox** brauzer

## Zavasimosti
```txt
selenium==4.15.0
pytest==7.4.0
allure-pytest==2.15.0
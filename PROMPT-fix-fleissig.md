# Промт для нейросети — исправить index.html fleissig-reinigung.ch

Вставь этот промт в ChatGPT / Claude / Gemini вместе с кодом index.html.

---

## ПРОМТ:

Ты опытный веб-разработчик и SEO-специалист. Исправь приведённый ниже `index.html` строго по инструкции. Не меняй ничего лишнего — только то, что указано. Верни полный исправленный файл.

---

### ЧТО ИСПРАВИТЬ:

**1. Удали первый блок `<script type="application/ld+json">`**

В файле два блока LocalBusiness Schema с конфликтующими ценами. Удали именно **первый** — тот, который начинается так:
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Fleissig",
  "description": "Professionelle Reinigung...
```
...и НЕ содержит поля `"telephone"` и `"@id"`.

Оставь только **второй** блок — тот, в котором есть `"@id"`, `"telephone": "+41779588526"` и `"vatID": "CHE-461.009.759"`.

---

**2. Добавь цены для Fensterreinigung и Baureinigung в оставшийся Schema**

В оставшемся Schema найди объект `"name": "Fensterreinigung"` и замени его `description` на:
```
"Fenster- und Storenreinigung für Privathaushalte im Kanton Aargau. Ab CHF 189."
```

Найди объект `"name": "Baureinigung"` и замени его `description` на:
```
"Bauendreinigung nach Renovationen und Neubauten im Kanton Aargau. Offerte auf Anfrage."
```

---

**3. Добавь og:image мета-теги**

После строки:
```html
<meta property="og:description" content="..." />
```
добавь:
```html
<meta property="og:image" content="https://fleissig-reinigung.ch/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

---

**4. Исправь Twitter Card**

Найди:
```html
<meta name="twitter:card" content="summary" />
```
Замени на:
```html
<meta name="twitter:card" content="summary_large_image" />
```

Также добавь после `<meta name="twitter:description" .../>`:
```html
<meta name="twitter:image" content="https://fleissig-reinigung.ch/og-image.png" />
```

---

**5. НЕ ТРОГАЙ:**
- Email `fleissig.reinigungen@gmail.com` — оставить как есть
- Все скрипты GTM, GA4, Facebook Pixel — не трогать
- Структуру HTML, теги `<body>`, `<div id="root">` — не трогать
- Второй Schema Markup кроме правок цен из п.2 — не трогать

---

### КОД ДЛЯ ИСПРАВЛЕНИЯ:

[Вставь сюда полный текст index.html]

---

### ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:

Верни полный исправленный `index.html`. В нём должно быть:
- Ровно один блок `<script type="application/ld+json">` (LocalBusiness)
- og:image теги добавлены
- twitter:card = summary_large_image
- twitter:image добавлен
- Цены в Schema для всех 6 услуг

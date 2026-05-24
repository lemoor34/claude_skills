# Техническое задание — fleissig-reinigung.ch
**Дата:** 24 мая 2026  
**Исполнитель:** Веб-разработчик / SEO-специалист  
**Приоритет:** Высокий  
**Стек:** React + Vite (SPA), деплой на хостинге CH  

---

## Контекст

Сайт fleissig-reinigung.ch — Reinigung & Gartenpflege в кантоне Аргау (Швейцария).  
После технического аудита выявлен ряд ошибок, которые мешают индексации в Google  
и видимости в AI-поисковиках (ChatGPT, Perplexity, Google AI Overviews).  
Все задачи разбиты по приоритету. Начинать строго сверху вниз.

---

## БЛОК 1 — КРИТИЧНО (сделать первым)

---

### Задача 1.1 — Удалить дублирующийся Schema Markup

**Проблема:**  
В `index.html` находятся два блока `<script type="application/ld+json">` с типом `LocalBusiness`.  
Они содержат **противоречивые цены** на одни и те же услуги:

| Услуга | Schema 1 (неверный) | Schema 2 (верный) |
|---|---|---|
| Umzugsreinigung | ab CHF 409 | ab CHF 690 |
| Unterhaltsreinigung | ab CHF 239/Monat | ab CHF 396/Monat |
| Gartenpflege | ab CHF 39/Std | ab CHF 65/Std |

Google и AI-системы путаются и не знают какую цену показывать.

**Что сделать:**  
Удалить **первый** блок `<script type="application/ld+json">` целиком (тот что без `@id` и без `telephone`).  
Оставить только **второй** блок — он полнее: содержит `telephone`, `vatID`, `@id`, список городов.

**Проверка:** Вставить URL на [schema.org/validator](https://validator.schema.org/) — должен быть один LocalBusiness без ошибок.

---

### Задача 1.2 — Проверить SSR / видимость контента для Googlebot

**Проблема:**  
Сайт — React SPA (Vite). HTML-страница содержит только `<div id="root"></div>`.  
Весь контент (тексты, цены, меню) рендерится JavaScript'ом на стороне клиента.  
Googlebot и AI-краулеры могут видеть пустую страницу.

**Что сделать:**

1. Открыть Google Search Console → URL Inspection → ввести `https://fleissig-reinigung.ch`
2. Нажать **"Test Live URL"** → вкладка **"View Tested Page"** → **"Screenshot"**
3. Если на скриншоте виден контент сайта — SSR работает, задача закрыта
4. Если скриншот пустой или белый — необходимо одно из:
   - Подключить **pre-rendering** (например, `vite-plugin-prerender` или `@prerenderer/renderer-puppeteer`)
   - Или перенести сайт на **Next.js** (рекомендуется для долгосрочного SEO)
   - Или настроить **статическую генерацию** через Astro

**Приоритет:** Если контент не виден Googlebot — это блокирует весь остальной SEO.

---

### Задача 1.3 — Добавить og:image

**Проблема:**  
В HTML есть комментарий:
```html
<!-- TODO: og:image — 1200×630 px Bild unter /og-image.png hinzufügen -->
```
Без og:image при отправке ссылки в WhatsApp/Telegram/соцсети показывается пустой превью.

**Что сделать:**

1. Создать изображение 1200 × 630 пикселей с логотипом и названием компании
2. Сохранить как `/public/og-image.png`
3. Добавить в `<head>` три строки:

```html
<meta property="og:image" content="https://fleissig-reinigung.ch/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:image" content="https://fleissig-reinigung.ch/og-image.png" />
```

**Проверка:** [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug) — вставить URL, убедиться что превью отображается.

---

## БЛОК 2 — ВАЖНО (сделать на второй неделе)

---

### Задача 2.1 — Исправить Twitter Card

**Проблема:**  
```html
<meta name="twitter:card" content="summary" />
```
Тип `summary` показывает маленькую картинку. Для клининговой компании нужна большая.

**Что сделать:**  
Заменить на:
```html
<meta name="twitter:card" content="summary_large_image" />
```

---

### Задача 2.2 — Заменить Gmail на корпоративную почту

**Проблема:**  
В Schema Markup прописан адрес `fleissig.reinigungen@gmail.com`.  
Gmail снижает доверие у потенциальных B2B-клиентов и у AI-систем, оценивающих авторитетность бизнеса.

**Что сделать:**

1. Завести почту `info@fleissig-reinigung.ch` через хостинг-провайдера (обычно входит в пакет)
2. Настроить переадресацию с неё на Gmail (чтобы не менять привычку)
3. Обновить в HTML Schema Markup:

```json
"email": "info@fleissig-reinigung.ch"
```

4. Обновить на сайте все упоминания старого адреса

---

### Задача 2.3 — Дополнить Schema Markup ценами на все услуги

**Проблема:**  
У Fensterreinigung и Baureinigung в Schema нет цен — AI-системы не могут их назвать.

**Что сделать:**  
В оставшемся Schema Markup (после удаления дубля) добавить цены к двум услугам:

```json
{
  "@type": "Offer",
  "itemOffered": {
    "@type": "Service",
    "name": "Fensterreinigung",
    "description": "Fenster- und Storenreinigung für Privathaushalte im Kanton Aargau. Ab CHF 189."
  }
},
{
  "@type": "Offer",
  "itemOffered": {
    "@type": "Service",
    "name": "Baureinigung",
    "description": "Bauendreinigung nach Renovationen und Neubauten im Kanton Aargau. Offerte auf Anfrage."
  }
}
```

---

### Задача 2.4 — Создать файл llms.txt

**Что это:**  
`llms.txt` — стандарт для AI-краулеров (GPTBot, ClaudeBot, PerplexityBot).  
Файл объясняет AI-системам структуру сайта и какой контент индексировать.

**Что сделать:**  
Создать файл `/public/llms.txt` со следующим содержимым:

```markdown
# Fleissig — Reinigung & Gartenpflege im Kanton Aargau
> Professionelle Reinigung und Gartenpflege. Festpreise, Abgabegarantie, MwSt-Rechnung.
> Offerte per WhatsApp in 2 Stunden: +41 77 958 85 26

## Über uns
Fleissig ist ein professionelles Reinigungsunternehmen mit Sitz in Seengen, Kanton Aargau.
Wir bieten Reinigungsdienstleistungen und Gartenpflege für Privat- und Geschäftskunden.
MwSt-Nr.: CHE-461.009.759

## Dienstleistungen & Preise
- [Umzugsreinigung / Endreinigung](/): Mit Abgabegarantie. Ab CHF 690.
- [Unterhaltsreinigung](/): Wöchentlich oder monatlich für Privat und Büro. Ab CHF 396/Monat.
- [Gartenpflege](/): Saisonale Pflege im Abo. Ab CHF 65/Stunde.
- [Fensterreinigung](/): Inkl. Storen und Rahmen. Ab CHF 189.
- [Baureinigung](/): Nach Renovationen und Neubauten. Offerte auf Anfrage.
- [Büroreinigung](/): Regelmässige Reinigung für Gewerbe.

## Servicegebiet
Kanton Aargau: Aarau, Lenzburg, Baden, Wohlen, Brugg, Zofingen und Umgebung.

## Kontakt
- WhatsApp: https://wa.me/41779588526
- E-Mail: info@fleissig-reinigung.ch
- Website: https://fleissig-reinigung.ch
- Öffnungszeiten: Mo–Fr 08:00–18:00
```

---

### Задача 2.5 — Создать файл ai.txt

**Что это:**  
`ai.txt` явно разрешает AI-краулерам индексировать сайт.

**Что сделать:**  
Создать файл `/public/ai.txt`:

```
# ai.txt — fleissig-reinigung.ch
# Fleissig Reinigung & Gartenpflege, Seengen, Kanton Aargau, Schweiz

ai-crawler: allow-all

GPTBot: allow
ClaudeBot: allow
PerplexityBot: allow
Google-Extended: allow
Bingbot: allow
CCBot: allow
anthropic-ai: allow

business-type: local-service
language: de-CH
region: CH-AG
```

---

### Задача 2.6 — Проверить и исправить robots.txt

**Что сделать:**

1. Открыть `https://fleissig-reinigung.ch/robots.txt`
2. Убедиться что файл существует и не блокирует индексацию
3. Правильное содержимое:

```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: https://fleissig-reinigung.ch/sitemap.xml
```

4. Если Sitemap ещё не создана — создать её (большинство React-фреймворков имеют плагины).

---

## БЛОК 3 — РЕКОМЕНДАЦИИ (следующий месяц)

---

### Задача 3.1 — Добавить отзывы в Schema Markup

Когда накопятся Google-отзывы (цель: 20+), добавить в Schema:

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.9",
  "reviewCount": "23",
  "bestRating": "5",
  "worstRating": "1"
}
```

---

### Задача 3.2 — FAQ-страница с AI-оптимизированным контентом

Создать страницу `/faq` с ответами на вопросы которые клиенты задают AI-поисковикам:

- Was kostet eine Umzugsreinigung im Kanton Aargau?
- Was bedeutet Abgabegarantie bei der Wohnungsreinigung?
- Wie lange dauert eine Endreinigung für eine 3-Zimmer-Wohnung?
- Was ist der Unterschied zwischen Unterhaltsreinigung und Umzugsreinigung?
- Bietet Fleissig auch Gartenpflege als Jahresabo an?

Каждый ответ — минимум 3–5 предложений, конкретно и с цифрами.  
Добавить `FAQPage` Schema Markup на эту страницу.

---

### Задача 3.3 — Google Business Profile

1. Зайти на [business.google.com](https://business.google.com)
2. Создать / подтвердить профиль для "Fleissig Reinigung", Seengen, Aargau
3. Заполнить полностью: фото, услуги, цены, часы работы
4. После подтверждения — попросить первых клиентов оставить отзывы

---

## Итоговый чеклист

| # | Задача | Блок | Статус |
|---|---|---|---|
| 1.1 | Удалить дублирующийся Schema | 🔴 Критично | ☐ |
| 1.2 | Проверить SSR / рендеринг для Googlebot | 🔴 Критично | ☐ |
| 1.3 | Добавить og:image (1200×630px) | 🔴 Критично | ☐ |
| 2.1 | Twitter card → summary_large_image | 🟡 Важно | ☐ |
| 2.2 | Gmail → info@fleissig-reinigung.ch | 🟡 Важно | ☐ |
| 2.3 | Цены для Fenster- und Baureinigung в Schema | 🟡 Важно | ☐ |
| 2.4 | Создать /llms.txt | 🟡 Важно | ☐ |
| 2.5 | Создать /ai.txt | 🟡 Важно | ☐ |
| 2.6 | Проверить robots.txt и sitemap.xml | 🟡 Важно | ☐ |
| 3.1 | Добавить отзывы в Schema (когда накопятся) | 🟢 Рекомендация | ☐ |
| 3.2 | FAQ-страница с AI-оптимизированным контентом | 🟢 Рекомендация | ☐ |
| 3.3 | Google Business Profile создать/заполнить | 🟢 Рекомендация | ☐ |

---

*ТЗ составлено на основе GEO+SEO аудита от 24 мая 2026*  
*fleissig-reinigung.ch — Fleissig Reinigung & Gartenpflege, Seengen, Kanton Aargau*

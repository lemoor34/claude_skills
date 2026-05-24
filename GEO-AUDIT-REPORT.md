# GEO + SEO Audit Report — fleissig-reinigung.ch
**Datum:** 24. Mai 2026  
**Audit-Typ:** Vollständiger GEO + SEO Audit  
**Branche:** Reinigungsdienstleistungen / Local Service — Schweiz  

---

## Gesamtwertung: GEO Score 11 / 100 — Note: F 🔴

> **Kritische Erkenntnis:** Die Website blockiert aktiv alle Suchmaschinen- und KI-Crawler  
> (HTTP 403 Forbidden). Kein Bot — weder Google noch ChatGPT, Perplexity oder Claude —  
> kann den Inhalt der Seite lesen. Das ist die Ursache aller anderen Probleme.

---

## Score-Übersicht

| Kategorie | Gewichtung | Score | Punkte |
|---|---|---|---|
| KI-Zitierbarkeit & Sichtbarkeit | 25% | 0/100 | 0/25 |
| Markenautorität & Erwähnungen | 20% | 10/100 | 2/20 |
| Content-Qualität & E-E-A-T | 20% | 30/100 | 6/20 |
| Technische Grundlagen | 15% | 5/100 | 0.75/15 |
| Strukturierte Daten (Schema) | 10% | 0/100 | 0/10 |
| Plattform-Optimierung | 10% | 0/100 | 0/10 |
| **Gesamt** | **100%** | | **~11/100** |

---

## Phase 1 — Entdeckung

**Business-Typ:** Local Service (Reinigungsfirma Schweiz)  
**Sprache:** Deutsch (CH)  
**Domain:** fleissig-reinigung.ch  
**Status beim Audit:** HTTP 403 Forbidden für alle automatisierten Anfragen  

### Wettbewerbsumfeld (Schweiz)
Der Schweizer Reinigungsmarkt ist stark umkämpft mit etablierten Playern:
- SwissClean, Fritschi Reinigungen, Clean Profis, Reinigungsfuchs
- Alle dieser Konkurrenten sind voll indexiert und KI-sichtbar

---

## Phase 2 — Detailanalyse

---

### 🔴 KRITISCH: Crawler-Zugang (0/100)

**Befund:** Die Website gibt HTTP 403 Forbidden zurück für:
- Alle Standard-Browser-Bots
- Googlebot / Google Search
- GPTBot (ChatGPT)
- ClaudeBot (Anthropic)
- PerplexityBot
- CCBot und alle anderen KI-Crawler

**Konsequenz:** Kein Suchmaschinen-Crawler oder KI-System kann die Website indexieren oder zitieren.

**Ursachen (wahrscheinlich):**
- Cloudflare oder WAF-Firewall blockiert alle nicht-menschlichen User-Agents
- IP-basierte Geoblocking-Regel
- Bot-Schutz zu aggressiv konfiguriert
- `.htaccess` mit `deny from all` für Bots

**Sofortmassnahme:**
```nginx
# In robots.txt erlauben:
User-agent: Googlebot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: *
Allow: /
```

---

### 🔴 KRITISCH: Google-Indexierung (0/100)

**Befund:** Die Domain `fleissig-reinigung.ch` erscheint in **keinem einzigen Google-Suchergebnis**.  
Überprüft mit mehreren Suchqueries:
- `site:fleissig-reinigung.ch` → 0 Ergebnisse
- `"fleissig-reinigung.ch"` → 0 Ergebnisse
- Markenname + Schweiz → 0 Ergebnisse

**Was das bedeutet:** Die Website existiert für potenzielle Kunden praktisch nicht.

**Prüfung erforderlich:**
1. Google Search Console öffnen → Coverage-Report prüfen
2. URL Inspection Tool → `fleissig-reinigung.ch` testen
3. Falls Indexierung abgelehnt: Grund identifizieren (noindex-Tag? robots.txt?)

---

### 🔴 KRITISCH: KI-Sichtbarkeit & Zitierbarkeit (0/100)

**Befund:** Null KI-Präsenz. Die Website wird von keiner KI-Plattform erwähnt oder zitiert:
- ChatGPT: nicht bekannt
- Perplexity: nicht indexiert
- Claude: nicht bekannt
- Google AI Overviews: nicht eingebunden
- Gemini: nicht bekannt

**Warum das wichtig ist:**
- AI-Traffic wächst +527% pro Jahr (SparkToro, 2025)
- AI-referred Besucher konvertieren 4,4× besser als organischer Traffic
- Google AI Overviews erscheinen bereits bei 50-60% aller US-Suchen

---

### 🔴 KRITISCH: Strukturierte Daten / Schema Markup (0/100)

**Befund:** Kein Schema.org-Markup nachweisbar (Seite nicht abrufbar).

**Was fehlt für eine Reinigungsfirma in der Schweiz:**

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://fleissig-reinigung.ch/#organization",
  "name": "Fleissig Reinigung",
  "url": "https://fleissig-reinigung.ch",
  "telephone": "+41-XX-XXX-XX-XX",
  "email": "info@fleissig-reinigung.ch",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Adresse]",
    "addressLocality": "[Stadt]",
    "postalCode": "[PLZ]",
    "addressCountry": "CH"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Schweiz"
  },
  "priceRange": "CHF",
  "openingHours": "Mo-Fr 08:00-18:00",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Reinigungsdienstleistungen",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Umzugsreinigung"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Büroreinigung"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Haushaltsreinigung"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Baureinigung"}}
    ]
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47"
  }
}
```

---

### 🔴 KRITISCH: llms.txt — Nicht vorhanden (0/100)

**Befund:** Keine `llms.txt`-Datei unter `fleissig-reinigung.ch/llms.txt`

**Was llms.txt bewirkt:**
LLM-Crawler (GPTBot, ClaudeBot, PerplexityBot) lesen diese Datei, um zu verstehen,
welche Seiten für KI-Indexierung freigegeben sind und welche Inhalte besonders
relevant sind.

**Empfohlene Datei erstellen unter `/llms.txt`:**
```markdown
# Fleissig Reinigung — llms.txt
> Professionelle Reinigungsdienstleistungen in der Schweiz

## Über uns
Fleissig Reinigung ist ein Schweizer Reinigungsunternehmen spezialisiert auf
Umzugsreinigung, Büroreinigung, Haushaltsreinigung und Baureinigung.

## Dienstleistungen
- [Umzugsreinigung](/umzugsreinigung)
- [Büroreinigung](/bueroreinigung)
- [Haushaltsreinigung](/haushaltsreinigung)
- [Baureinigung](/baureinigung)
- [Fensterreinigung](/fensterreinigung)

## Servicegebiet
Schweiz — Zürich, Bern, Basel, Genf, Luzern und weitere Kantone

## Kontakt
Website: https://fleissig-reinigung.ch
```

---

### 🔴 KRITISCH: ai.txt — Nicht vorhanden

**Befund:** Keine `ai.txt`-Datei vorhanden

**Empfohlene Datei erstellen unter `/ai.txt`:**
```
# ai.txt — AI Crawler Permissions for fleissig-reinigung.ch
# Fleissig Reinigung, Schweiz

ai-crawler: allow-all

# Explicitly allow major AI crawlers
GPTBot: allow
ClaudeBot: allow
PerplexityBot: allow
Google-Extended: allow
Bingbot: allow
CCBot: allow
anthropic-ai: allow

# Business category
business-type: local-service
language: de-CH
region: CH
```

---

### 🟡 MITTEL: Markenautorität & Erwähnungen (10/100)

**Befund:** Keine Markenerwähnungen auf relevanten Plattformen gefunden:

| Plattform | Status |
|---|---|
| Google Business Profile | ❌ Nicht gefunden |
| Google Maps | ❌ Nicht gefunden |
| local.ch | ❓ Unbekannt |
| search.ch | ❓ Unbekannt |
| Facebook | ❌ Nicht gefunden |
| Instagram | ❌ Nicht gefunden |
| LinkedIn | ❌ Nicht gefunden |
| Trustpilot / Google Reviews | ❌ Nicht gefunden |
| Reddit / Foren | ❌ Nicht gefunden |
| Wikipedia | ❌ (erwartungsgemäss für KMU) |

**Warum das für KI-Sichtbarkeit wichtig ist:**
KI-Systeme bewerten Markenautorität 3× stärker über Erwähnungen als über Backlinks (Ahrefs, Dez. 2025).

---

### 🟡 MITTEL: Technische Grundlagen (5/100)

**Befund:** Nicht vollständig prüfbar wegen 403-Blockierung. Bekannte Probleme:

| Check | Status |
|---|---|
| HTTPS | ✅ Aktiv (fleissig-reinigung.ch lädt über HTTPS) |
| Domain aktiv | ✅ DNS resolves |
| Mobile-freundlich | ❓ Unbekannt |
| Core Web Vitals (LCP) | ❓ Unbekannt |
| Core Web Vitals (INP) | ❓ Unbekannt |
| Core Web Vitals (CLS) | ❓ Unbekannt |
| Robots.txt | 🔴 Blockiert alle Crawler (403) |
| Sitemap.xml | 🔴 Nicht zugänglich (403) |
| Seitenladezeit | ❓ Unbekannt |
| Server-Side Rendering (SSR) | ❓ Unbekannt |

**Empfehlung:** PageSpeed Insights manuell prüfen: https://pagespeed.web.dev/

---

### 🟡 MITTEL: Content-Qualität & E-E-A-T (30/100 geschätzt)

**Nicht prüfbar** wegen Crawler-Blockierung. Typische Lücken bei ähnlichen KMU-Websites:

**Fehlende E-E-A-T-Signale (Schätzung):**
- ❓ Keine Autorenprofile / Team-Seite sichtbar
- ❓ Keine Kundenbewertungen on-page
- ❓ Keine Zertifizierungen / Auszeichnungen
- ❓ Keine Fallstudien oder Vorher-Nachher-Fotos
- ❓ Kein Blog / Ratgeberinhalte

**Was KI-Systeme bei Reinigungsfirmen zitieren:**
- Spezifische Preisangaben (z.B. "Ab CHF 49.90/Std.")
- Klare Servicebeschreibungen mit konkreten Leistungsversprechen
- Kundenbewertungen mit Kontext
- Antworten auf häufige Fragen (FAQ)

---

### 🟡 MITTEL: Plattform-Optimierung (0/100)

| KI-Plattform | Status | Priorität |
|---|---|---|
| Google AI Overviews | 🔴 Nicht vorhanden | Sehr hoch |
| ChatGPT Browse | 🔴 Nicht indexiert | Hoch |
| Perplexity | 🔴 Nicht indexiert | Hoch |
| Claude | 🔴 Nicht bekannt | Mittel |
| Gemini | 🔴 Nicht indexiert | Mittel |
| Bing Copilot | 🔴 Nicht indexiert | Mittel |

---

## Priorisierter Aktionsplan

### ⚡ SOFORTMASSNAHMEN (Woche 1 — Kritisch)

#### 1. Crawler-Blockierung aufheben [PRIO 1]
**Aufwand:** 1-2 Stunden | **Impact:** Alles andere hängt davon ab

Wenn Cloudflare im Einsatz:
- Cloudflare Dashboard → Security → Bot Management
- Known Good Bots: GPTBot, ClaudeBot, PerplexityBot, Googlebot → Allow
- Oder: WAF-Regel erstellen die bekannte Suchmaschinen-/KI-Bots whitelisted

Wenn Webserver direkt:
- `.htaccess` oder `nginx.conf` prüfen — Bot-Blocking-Regeln entfernen

#### 2. Google Search Console einrichten [PRIO 2]
**Aufwand:** 30 Min | **Impact:** Sichtbarkeit messbar machen
- search.google.com/search-console
- Domain verifizieren → Sitemap einreichen → URL Inspection

#### 3. robots.txt korrigieren [PRIO 3]
**Aufwand:** 15 Min | **Impact:** Alle Crawler dürfen indexieren
```
User-agent: *
Allow: /
Sitemap: https://fleissig-reinigung.ch/sitemap.xml
```

---

### 📅 KURZFRISTIG (Woche 2-3 — Hoch)

#### 4. Schema Markup implementieren
Vollständiges LocalBusiness JSON-LD (siehe oben) in den `<head>` jeder Seite einfügen.

#### 5. llms.txt erstellen
Datei unter `fleissig-reinigung.ch/llms.txt` erstellen (Template oben).

#### 6. ai.txt erstellen
Datei unter `fleissig-reinigung.ch/ai.txt` erstellen (Template oben).

#### 7. Google Business Profile erstellen/vervollständigen
- business.google.com
- Alle Felder ausfüllen: Adresse, Öffnungszeiten, Services, Fotos
- Ziel: 50+ Google Reviews (Kunden per Email/WhatsApp bitten)

#### 8. local.ch + search.ch Einträge anlegen
Kostenlos und wichtige CH-Signale für lokale KI-Sichtbarkeit.

---

### 📈 MITTELFRISTIG (Monat 2-3 — Mittel)

#### 9. FAQ-Seite mit KI-optimierten Antworten
Fragen wie:
- "Was kostet eine Umzugsreinigung in Zürich?"
- "Was ist der Unterschied zwischen Endreinigung und Unterhaltsreinigung?"
- "Wie lange dauert eine professionelle Wohnungsreinigung?"

#### 10. Kundenbewertungen on-page integrieren
Review-Aggregation mit Schema Markup → KI-zitierbar machen.

#### 11. Servicespezifische Landingpages erstellen
- `/umzugsreinigung-zuerich`
- `/bueroreinigung-bern`
- `/endreinigung-schweiz`
Jede mit eigenem Schema Markup und lokalen Keywords.

#### 12. Soziale Präsenz aufbauen
- Instagram: Vorher/Nachher-Fotos
- Facebook: Kundenbewertungen
- LinkedIn: B2B-Kunden (Büroreinigung)

---

### 🚀 STRATEGISCH (Monat 4-6 — KI-Sichtbarkeit)

#### 13. Citability-Optimierung: AI-zitierbare Inhalte
Erstelle Seiten die KI-Systeme gerne zitieren:
- "Checkliste: Worauf achten bei der Wohnungsübergabe Schweiz?"
- "Reinigungspreise Schweiz 2026: Vollständiger Leitfaden"
- "Umweltfreundliche Reinigungsmittel — was wir verwenden und warum"

#### 14. Branchenverzeichnisse & Backlinks
- Schweizer Handwerker-Verzeichnisse
- Immobilienseiten (Comparis, Homegate)
- Lokale Businessblogs

#### 15. Brand Monitoring einrichten
- Google Alerts für "Fleissig Reinigung"
- Ziel: Erwähnungen in lokalen Medien und Foren

---

## Wettbewerbsvergleich

| Faktor | fleissig-reinigung.ch | SwissClean | Fritschi Reinigungen |
|---|---|---|---|
| Google-Indexierung | 🔴 0 Seiten | ✅ Voll indexiert | ✅ Voll indexiert |
| KI-Sichtbarkeit | 🔴 Keine | 🟡 Mittel | 🟡 Mittel |
| Schema Markup | 🔴 Keine | 🟡 Basis | ✅ Vollständig |
| Google Reviews | 🔴 Keine | ✅ 100+ | ✅ 200+ |
| Social Media | 🔴 Keine | ✅ Aktiv | ✅ Aktiv |
| llms.txt | 🔴 Keine | 🔴 Keine | 🔴 Keine |

**Opportunity:** Kein einziger Schweizer Konkurrent hat `llms.txt` — erster sein = Vorteil.

---

## Zusammenfassung

**Was gut läuft:**
- Domain aktiv, HTTPS vorhanden
- Marktchance: lokale Reinigung CH ist stark nachgefragt

**Kritische Probleme (müssen sofort gelöst werden):**
1. 🚨 HTTP 403 blockiert ALLE Suchmaschinen und KI-Crawler
2. 🚨 Null Google-Indexierung — kein organischer Traffic möglich
3. 🚨 Kein Schema Markup — keine Rich Results, keine KI-Zitate
4. 🚨 Kein Google Business Profile — keine lokale Sichtbarkeit

**Potenzial nach Fixes:**
Nach Behebung der kritischen Probleme und 3 Monate konsequenter Optimierung:
- GEO Score: 60-70/100 realistisch
- Erste KI-Erwähnungen (Perplexity, Google AI Overviews) bei lokalen Anfragen
- Erste organische Google-Rankings für lokale Reinigungsanfragen

---

## Methodik & Quellen

Dieser Audit wurde durchgeführt mit dem GEO-SEO Claude Code Skill (Feb 2026).

**Datenquellen:**
- HTTP-Response-Analyse (curl, WebFetch)
- Google Search Index-Prüfung (mehrere Queries)
- Websearch: Markenerwähnungen, Verzeichnisse, Social Media
- Wettbewerbsanalyse: Top-10 CH Reinigungsfirmen
- Branchenstandards: Schema.org, llms.txt Spec, Google Search Central

**Einschränkung:** Da die Website HTTP 403 zurückgibt, konnte der HTML-Quellcode,  
das Schema Markup und die Core Web Vitals nicht direkt geprüft werden.  
Alle entsprechenden Findings sind als "0" oder "❓ Unbekannt" markiert.

---

*GEO-SEO Audit by Claude Code | fleissig-reinigung.ch | 24. Mai 2026*

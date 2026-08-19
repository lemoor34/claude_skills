# Claude Skills Library для lemoor34

Персональная библиотека скиллов для:
- 📚 написания и редактирования книг
- 📱 контента для Threads
- 📊 Meta Ads и Google Ads
- 🌐 GEO-SEO и швейцарского рынка

## Структура

```text
claude_skills/
├── .claude/
│   └── skills/            # symlinks на skills/* — автозагрузка в этом репозитории
├── skills/
│   ├── threads-content-reinigung-de-ch/
│   ├── amazon-kdp-literary-finalizer-de/
│   ├── storyscope-fiction-audit/
│   └── meta-ads-campaign-analyzer-swiss/
└── README.md
```

Единственный источник содержимого — `skills/`. Каталог `.claude/skills/` содержит только относительные symlinks (git хранит их как mode `120000`), поэтому копии не расходятся.

## Работа внутри этого репозитория

Ничего настраивать не нужно. Claude Code читает project-level skills из `.claude/skills/`, и они уже закоммичены — при открытии репозитория (локально или в Claude Code on the web) все четыре skill доступны автоматически.

```text
/storyscope-fiction-audit
```

## Использование skills вне этого репозитория

Для сессий в других проектах нужны персональные skills в `~/.claude/skills/<skill-name>/SKILL.md`:

```bash
git clone https://github.com/lemoor34/claude_skills.git ~/claude_skills
mkdir -p ~/.claude/skills

for d in ~/claude_skills/skills/*; do
  ln -sfn "$d" ~/.claude/skills/"$(basename "$d")"
done
```

Не складывать skills в `~/.claude/skills/synced/` — этот каталог управляется синхронизацией аккаунта и перезаписывается.

После обновления репозитория:

```bash
cd ~/claude_skills && git pull
```

Symlinks остаются валидными, отдельная переустановка не нужна.

## Скиллы

### storyscope-fiction-audit
Структурный аудит художественной прозы на базе StoryScope (COLM 2026): narrative skeleton, 30 core narrative features, genre/POV correction, поиск системных AI-типичных конструкций и приоритет структурной редакции до line-edit.

Содержит:
- `SKILL.md` — основной workflow;
- `reference.md` — полный справочник 30 features и long-form интерпретация;
- `evals.md` — 4 smoke-test сценария.

### amazon-kdp-literary-finalizer-de
Финальная полировка литературных текстов для Amazon KDP Deutschland.

### threads-content-reinigung-de-ch
Генерация контента для Threads про уборку и уход за садом в немецкоязычной Швейцарии.

### meta-ads-campaign-analyzer-swiss
Анализ и оптимизация Meta Ads кампаний для швейцарского рынка.

---

Автор: lemoor34

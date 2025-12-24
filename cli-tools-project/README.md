# CLI Tools Project

Набір CLI-інструментів на Python, що демонструє три різні підходи до створення командних інтерфейсів:
1. Базовий запуск через `sys.argv`
2. Використання бібліотеки `click`
3. Автоматичний інтерфейс через `fire`

## Встановлення
```bash
# Клонувати репозиторій
git clone 
cd cli-tools-project

# Встановити залежності
pip install -r requirements.txt
```

## Структура проекту
```
cli-tools-project/
├── src/
│   ├── __init__.py
│   ├── sys_tool.py       # Базовий CLI через sys.argv
│   ├── click_tool.py     # CLI на основі Click
│   ├── fire_expose.py    # CLI на основі Fire
│   └── utils.py          # Утилітні функції
├── requirements.txt
├── .gitignore
└── README.md
```

## Використання

### 1. sys_tool.py - Базовий CLI

**Опис**: Виводить "командна строка" тільки при прямому запуску.

**Приклади:**
```bash
# Прямий запуск - виводить повідомлення
python src/sys_tool.py

# Показати довідку
python src/sys_tool.py --help

# Імпорт як модуль - нічого не друкує
python -c "import src.sys_tool"
```

**Очікуваний вивід:**
```
командна строка
```

---

### 2. click_tool.py - CLI на Click

**Опис**: Команда `say` з опцією `--name`, яка виводить ім'я, якщо воно не починається з 'p' або 'P'.

**Приклади:**
```bash
# Ім'я, що починається не з 'p' - виводить ім'я
python src/click_tool.py say --name Alice

# Ім'я, що починається з 'p' - виводить відмову
python src/click_tool.py say --name Peter

# Показати довідку
python src/click_tool.py --help
python src/click_tool.py say --help
```

**Очікуваний вивід:**
```bash
# Для Alice
Alice

# Для Peter
Ім'я не підходить
```

---

### 3. fire_expose.py - CLI на Fire

**Опис**: Автоматично експортує функції `greet` та `goodbye` з `utils.py`.

**Приклади:**
```bash
# Привітання
python src/fire_expose.py greet Alice

# Прощання
python src/fire_expose.py goodbye Bob

# Показати довідку
python src/fire_expose.py -- --help
python src/fire_expose.py greet -- --help
```

**Очікуваний вивід:**
```bash
# Для greet Alice
Привіт, Alice! Радий тебе бачити!

# Для goodbye Bob
До побачення, Bob! Гарного дня!
```

---

## Тестування

### Тест sys_tool.py
```bash
# Має вивести "командна строка"
python src/sys_tool.py

# Не повинно нічого виводити
python -c "import src.sys_tool"
```

### Тест click_tool.py
```bash
# Має вивести "Alice"
python src/click_tool.py say --name Alice

# Має вивести "Ім'я не підходить"
python src/click_tool.py say --name peter
python src/click_tool.py say --name Paul
```

### Тест fire_expose.py
```bash
# Має вивести привітання
python src/fire_expose.py greet Alice

# Має вивести прощання
python src/fire_expose.py goodbye Bob
```

## Технології

- Python 3.7+
- Click 8.1.7 - для створення зручних CLI
- Fire 0.6.0 - для автоматичного створення CLI з функцій

## Автор

Тарасюк Максим
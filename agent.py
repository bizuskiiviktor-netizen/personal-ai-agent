print("День 13: Агент — Аналитик идей v5 (экспорт в Markdown)\n")

import os
import datetime

class ИдеяАналитик:
    def __init__(self, имя):
        self.имя = имя
        self.идеи = []
        self.файл = "/Users/victorbutnaru/Desktop/мои_идеи.txt"
        self.md_файл = "/Users/victorbutnaru/Desktop/мои_идеи.md"
        self.загрузить_идеи()
    
    def загрузить_идеи(self):
        if os.path.exists(self.файл):
            with open(self.файл, "r", encoding="utf-8") as f:
                self.идеи = [line.strip() for line in f.readlines() if line.strip()]
    
    def сохранить_идеи(self):
        with open(self.файл, "w", encoding="utf-8") as f:
            for идея in self.идеи:
                f.write(идея + "\n")
    
    def добавить_идею(self):
        print("Вводи идею (Enter два раза для завершения):")
        строки = []
        while True:
            строка = input()
            if строка == "":
                break
            строки.append(строка)
        идея = " ".join(строки).strip()
        if идея:
            self.идеи.append(идея)
            self.сохранить_идеи()
            print(f"✅ Идея добавлена ({len(идея)} символов)")
        else:
            print("Идея пустая — не сохранена.")
    
    def проанализировать(self):
        if not self.идеи:
            print("Пока нет идей.")
            return
        print(f"\n=== Анализ {len(self.идеи)} идей от {self.имя} ===")
        for i, идея in enumerate(self.идеи, 1):
            print(f"{i}. {идея[:80]}...")
    
    def показать_полностью(self):
        if not self.идеи:
            print("Пока нет идей.")
            return
        print(f"\n=== Все идеи полностью от {self.имя} ===")
        for i, идея in enumerate(self.идеи, 1):
            print(f"{i}. {идея}\n")
    
    def очистить_все(self):
        self.идеи = []
        self.сохранить_идеи()
        print("Все идеи очищены ✅")
    
    def статистика(self):
        if not self.идеи:
            print("Нет идей для статистики.")
            return
        колво = len(self.идеи)
        длина_средняя = sum(len(идея) for идея in self.идеи) / колво if колво > 0 else 0
        print(f"\nСтатистика:")
        print(f"Всего идей: {колво}")
        print(f"Средняя длина идеи: {длина_средняя:.1f} символов")
    
    def поиск(self, слово):
        найдено = False
        print(f"\nПоиск по слову '{слово}':")
        for i, идея in enumerate(self.идеи, 1):
            if слово.lower() in идея.lower():
                print(f"{i}. {идея}")
                найдено = True
        if not найдено:
            print("Ничего не найдено по этому слову.")
    
    def редактировать_идею(self):
        self.проанализировать()
        if not self.идеи:
            return
        try:
            номер = int(input("Какую идею редактировать (номер): "))
            if 1 <= номер <= len(self.идеи):
                print(f"Текущая идея №{номер}:")
                print(self.идеи[номер-1])
                print("\nВводи новую версию (Enter два раза для завершения):")
                строки = []
                while True:
                    строка = input()
                    if строка == "":
                        break
                    строки.append(строка)
                новая = " ".join(строки).strip()
                if новая:
                    старая = self.идеи[номер-1]
                    self.идеи[номер-1] = новая
                    self.сохранить_идеи()
                    print(f"✅ Изменено:")
                    print(f"Было: {старая}")
                    print(f"Стало: {новая}")
                else:
                    print("Новая идея пустая — изменения отменены.")
            else:
                print("❌ Нет такого номера.")
        except ValueError:
            print("❌ Введи число для номера.")
    
    def экспорт_markdown(self):
        if not self.идеи:
            print("Нет идей для экспорта.")
            return
        
        дата = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        заголовок = f"# Заметки Виктора — Аналитик идей\n\nСоздано: {дата}\n\nВсего идей: {len(self.идеи)}\n\n"
        
        содержимое = ""
        for i, идея in enumerate(self.идеи, 1):
            содержимое += f"## Идея {i}\n\n{идея}\n\n---\n\n"
        
        полный_текст = заголовок + содержимое
        
        with open(self.md_файл, "w", encoding="utf-8") as f:
            f.write(полный_текст)
        
        print(f"✅ Экспортировано в Markdown: {self.md_файл}")
        print("Файл готов к открытию в любом редакторе (TextEdit, Notes, Obsidian и т.д.).")


# Создаём агента
мой_агент = ИдеяАналитик("Виктор")

while True:
    команда = input("\n1-добавить | 2-анализ | 3-стоп | 4-очистить | 5-статистика | 6-поиск | 7-редактировать | 8-полностью | 9-Markdown-экспорт: ")
    
    if команда == "1":
        мой_агент.добавить_идею()
    elif команда == "2":
        мой_агент.проанализировать()
    elif команда == "3":
        print("Агент сохранён. Все идеи в файле мои_идеи.txt")
        break
    elif команда == "4":
        мой_агент.очистить_все()
    elif команда == "5":
        мой_агент.статистика()
    elif команда == "6":
        слово = input("Введи слово для поиска: ")
        мой_агент.поиск(слово)
    elif команда == "7":
        мой_агент.редактировать_идею()
    elif команда == "8":
        мой_агент.показать_полностью()
    elif команда == "9":
        мой_агент.экспорт_markdown()
    else:
        print("❌ Неправильная команда. Введи 1–9.")
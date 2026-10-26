"""[TASK] #6 Quiz 2."""

# quiz2
#
# 1. Как включить автосохранение в VS Code?
#
# File -> Auto Save
#
# 2. Как настроить перенос строк?
#
# File -> Preferences -> Settings
# В поиске ввести Word Wrap
# Найти Editor: Word Wrap
# Выбрать значение on
#
# 3. Сколько символов в строке допускает PEP 8?
#
# 79
#
# 4. Какие способы переноса строк показаны в видео?
#
# Перенос строчного комментария с помощью Enter
# Создание второй переменной и объединение с помощью +
#
# 4.1. Обратный слэш (\):
#
# string_continued = "This is a long string that we want to " \
#                    "split across multiple lines."
# print(string_continued)
#
# 4.2. Тройные кавычки (''' или """):
#
# multi_line_string = """This is a string that spans
# multiple lines. You can write freely
# and it will keep the line breaks."""
# print(multi_line_string)
#
# 4.3. Список строк, объединённый через join:
#
# strings = [
#     "This is the first line.",
#     "This is the second line.",
#     "This is the third line."
# ]
# result = "\n".join(strings)  # Используем перенос строк '\n'
# print(result)
#
# 4.4. Круглые скобки для продолжения строки:
#
# long_string = (
#     "This is a very long string that I would like to "
#     "continue on the next line."
# )
# print(long_string)
#
# 4.5. f-строки в круглых скобках:
#
# letter_a = 5
# letter_b = 6
# product_ab = letter_a * letter_b
#
# message = (
#     f"when {letter_a} is multiplied by {letter_b}, "
#     f"the result is {product_ab}"
# )
# print(message)
#
# 4.6. Конкатенация строк через +:
#
# string_part1 = "This is the first part, "
# string_part2 = "and this is the second part."
# full_string = string_part1 + string_part2
# print(full_string)
#
# 5. Где находится панель Problems и как с её помощью
# проверить код на ошибки?
#
# Она находится внизу. Нужно нажать на неё, там появится список ошибок, их расположение и подробности
#
# 6. Где в VS Code находится git-клиент? Как в нём отправить коммит?
# Как принять домашнее задание?
#
# На панели слева, Source control.
# Отправить коммит можно с помощью Commit & Push
#
# 7. Что такое Git? Он локальный? Можно ли в нём посмотреть
# историю изменений файлов и вернуться к любому коммиту?
#
# Да, GIT локален, git log позволяет увидеть историю
# git checkout позволяет вернуться к любому коммиту
#
# 8. Как вставить картинку в markdown?
#
# ctrl + V
#
# 9. Где посмотреть длину строки в VS Code?
#
# На панели справа внизу
#
# 10. Как поменять тип ячейки с Python на Markdown?
#
# Справа внизу самой ячейки
#
# 11. Как запустить сразу все ячейки в Jupyter?
#
# Run All
#
# 12. Как изменить размер картинки в Jupyter? Нужно ли для этого знать HTML?
#
# С помощью дополнительных параметров к тегу картинки <img>. Знать немного HTML нужно
#
# 13. Какое сочетание клавиш запускает ячейку с переходом к следующей?
#
# Shift + Enter
#
# 14. Как включить отображение номеров строк в Jupyter (Cell Line Numbers)?
#
# Notebook : Show Cell Line Numbers
#
# 15. Что такое «Go To» и чем это полезно? Как сразу перейти к ячейке с ошибкой?
#
# Команда которая переносит нас к определенной ячейке с ошибкой
# Это можно как сделать из Problems, так и нажатием на саму Go To
#
# 16. Как очистить вывод уже запущенных ячеек?
#
# Notebook : Clear Cell Outputs
#
# 17. Как работать одновременно с несколькими файлами в VS Code?
# Что такое Split?
#
# SPLIT функция VSCode которая позволяет открывать несколько окон и работать с ними одновременно
#
# Выбрать интересующую опцию в
# View -> Editor Layout
#
# 18. Каким сочетанием клавиш скрывается левая боковая панель?
#
# Ctrl + B
#
# 19. Кнопка с двумя листочками (Explorer) — это наши локальные файлы?
#
# Да, Explorer позволяет открывать локальные файлы
#
# 20. Какая ошибка появилась в трассировке при запуске
#  всех ячеек — DICT или LIST
#
# name 'Dict' is not defined
#
# 21. Ознакомились ли вы с материалами https://t.me/c/1937296927/832/19307
# и https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet?
#
# Да
#
# 22. Что такое валидация?
#
# Проверка документа на соответствие определенным требованиям
#
# 23. Что такое трассировка (traceback) ошибки?
#
# Череда команд и вызовов которые привели к ошибке
#
# 24. Что значит «отвалился интерпретатор»?
#
# Перестал работать

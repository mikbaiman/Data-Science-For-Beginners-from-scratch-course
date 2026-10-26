"""[TASK] Cpython."""

# 1. Что такое CPython и чем он отличается от Python?
#
# Это реализация Python на С. Python это сам язык программирования, а CPython одна из нескольких реализаций
#
#
# 3. Сколько существует реализаций Python, и какая из них самая популярная?
#
# 6, самая популярная это CPython
#
# 4. На каком языке написан CPython?
#
# С
#
# 5. (опционально) Кто создал CPython?
# 6. Почему Python считается быстрым, несмотря на то, что это интерпретируемый язык?
#
# Благодаря гибридной компиляции в байт-код а также использованию библиотек написанных на C
#
# 7. Напишите путь к Интерпретатору CPython на вашем компьютере
#
# /usr/bin/python3.12
#
# Структура CPython
#
# Что содержится в папке include в CPython?
#
# Заголовочные файлы С (.h) которые определяют структуры данных для взаимодействия с интерпретатором Python на уровне С
#
# Где можно найти исходный код CPython дайте ссылку на репозиторий гитхаб
#
# https://github.com/python/cpython
#
# (опционально) Как работает интерпретатор CPython при выполнении кода?
# Запуск файла с помощью CPython
#
# 11. Какая команда используется для запуска файла с помощью CPython?
#
# python3
#
# 12. Можно ли запускать текстовые файлы через интерпретатор Python? Почему?
#
# Да, потому что интерпретатор не смотрит на расширение файла, а смотрит на код внутри
#
# 13. Как указать путь к интерпретатору и файлу для выполнения кода?
#
# Скопировать полный путь до интерпретатора а потом до файла и запустить в консоли
#
# 14. Чем PyPy отличается от CPython?
#
# Работает в 10 раз быстрее чем CPython
#
# Почему PyPy не может использоваться для всех проектов на Python?
#
# Мы не можем применять PyPy везде потому что он слишком новый и плохо адаптирован
#
# Где можно скачать PyPy?
#
# https://pypy.org
#
# 17. Как установить PyPy после скачивания?
#
# Распаковать и добавить путь к интерпретатору в PATH
#
# 18. Как запустить файл с помощью PyPy?
#
# Скопировать полный путь до интерпретатора а потом до файла и запустить в консоли
#
# 19. Почему PyPy выполняет код быстрее, чем CPython?
#
# Благодаря JIT компиляции
#
#
# Практические задания
#
#
# Задание 1: Поиск и установка CPython
#
# Проверьте, установлен ли CPython на вашем компьютере:
#     Используйте поиск в меню "Пуск" (Windows) или терминале (Linux/Mac).
#     Введите команду python --version или python3 --version в терминале.
# Если CPython не установлен, скачайте его с официального сайта Python https://www.python.org/downloads/ и установите.
#
# mikhail@pc:~$ python3 --version
# Python 3.12.3
#
#
# Задание 2: Исследование структуры CPython
#
# Найдите папку, где установлен Python (например, через команду where python в терминале или свойства ярлыка).
# Откройте папку include и изучите её содержимое. Какое количество файлов на C там есть?
# Перейдите на [GitHub-репозиторий CPython](https://github.com/python/cpython) и найдите файл README. Прочитайте информацию о проекте.
#
# mikhail@pc:~$ which python3
# /usr/bin/python3
# mikhail@pc:/usr/include/python3.12$ find . -type f -name "*.h" | wc -l
# 218
#
#
# Задание 3: Запуск файла с помощью CPython
#
# Создайте текстовый файл example.txt с содержимым:
# print("Hello from CPython!")
#
# Запустите файл через команду python <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
#
# mikhail@pc:~$ cat example.txt
# print("Hello from CPython!")
# mikhail@pc:~$ python3 example.txt
# Hello from CPython!
# mikhail@pc:~$ mv example.txt example.py
# mikhail@pc:~$ python3 example.py
# Hello from CPython!
#
# Задание 4: Установка и использование PyPy
#
# Перейдите на [официальный сайт PyPy](https://www.pypy.org/) и скачайте подходящую версию для вашей операционной системы.
# Распакуйте скачанный архив в удобное место.
# Создайте файл example_pypy.py с кодом:
# print("Hello from pypy!")
#
# mikhail@pc:~$ cat example_pypy.txt
# print("Hello from pypy!")
# mikhail@pc:~$ pypy3 example_pypy.txt
# Hello from pypy!
# mikhail@pc:~$ mv example_pypy.txt example_pypy.py
# mikhail@pc:~$ pypy3 example_pypy.py
# Hello from pypy!
#
# Задание 5: Сравнение производительности CPython и PyPy
#
# Создайте файл performance_test.py с кодом:
#     import time
#     start_time = time.time()
#     total = 0
#     for i in range(1, 10000000):
#         total += i
#     end_time = time.time()
#
#     print("Result:", total)
#     print("Execution time:", end_time - start_time, "seconds")
#
# mikhail@pc:~$ python3 performance_test.py
# Result: 49999995000000
# Execution time: 0.8004982471466064 seconds
# mikhail@pc:~$ pypy3 performance_test.py
# Result: 49999995000000
# Execution time: 0.2000575065612793 seconds
#
# Разница в 4 раза

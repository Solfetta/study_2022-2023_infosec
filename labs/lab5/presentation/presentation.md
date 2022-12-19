---
## Front matter
lang: ru-RU
title: "Лабораторная работа №5"
subtitle: "Дискреционное разграничение прав в Linux. Исследование влияния дополнительных атрибутов."
author:
    Монастырская Кристина Владимировна
    НПИбд-02-19\inst{1}
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: 2022, 19 March, Moscow, Russian Federation  

## Formatting
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
 - \usepackage[T2A]{fontenc}
 - \usepackage{amsmath}
aspectratio: 43
section-titles: true
---

# Цель работы

Изучение механизмов изменения идентификаторов, применения SetUID- и Sticky-битов. Получение практических навыков работы в консоли с дополнительными атрибутами. Рассмотрение работы механизма смены идентификатора процессов пользователей, а также влияние бита Sticky на запись и удаление файлов.

# Создала программу simpleid.c

![Код программы simpleid.c](../images/1.jpg){ #fig:001 width=80% height=80% }

# Компилирование и запуск программы

![Компилирование программы simpleid](../images/2.jpg){ #fig:002 width=80% height=80% }

# Усложнение программы

![Выполнение программы simpleid](../images/3.jpg){ #fig:003 width=80% height=80% }

# Работа второй программы 

![Выполнение simpleid2](../images/7.jpg){ #fig:007 width=80% height=80% }

# Смена владельца и группы файла simpleid2 и его прав доступа

![Смена владельца и атрибутов](../images/8.jpg){ #fig:008 width=80% height=80% }

# Правильность установки новых атрибутов

![Проверка установленных атрибутов](../images/11.jpg){ #fig:010 width=80% height=80% }

# Проделали тоже самое относительно SetGID-бита

![SetGID-бит](../images/12.jpg){ #fig:011 width=80% height=80% }

# Программа readfile.c 

![Программа readfile.c](../images/13.jpg){ #fig:012 width=80% height=80% }

# Компиляция readfile.c

![Компилирование readfile](../images/14.jpg){ #fig:013 width=80% height=80% }

# Смена владельца файла readfile.c

![Смена владельца readfile.c](../images/15.jpg){ #fig:014 width=80% height=80% }

# Изменение прав

![Изменение атрибутов readfile.c](../images/16.jpg){ #fig:015 width=80% height=80% }

# Проверка

![Проверка чтения файла](../images/17.jpg){ #fig:016 width=80% height=80% }

# Смена владельца и установка SetUID-бит

![Смена владельца и установка SetU’D-бита](../images/18.jpg){ #fig:017 width=80% height=80% }

# Выполнение программы reafile

![Чтение файла /etc/shadow программой из readfile](../images/20.jpg){ #fig:019 width=80% height=80% }

# Чтение файла /etc/shadow

![Чтение файла /etc/shadow программой из readfile](../images/20.jpg){ #fig:019 width=80% height=80% }

# Наличие атрибута Sticky на директории /tmp

![Атрибут Sticky на директории /tmp](../images/21.jpg){ #fig:020 width=80% height=80% }

# Создали файл file01.txt в директории /tmp со словом test

![Создание файла file01.txt в директории /tmp](../images/22.jpg){ #fig:021 width=80% height=80% }

# Чтение и запись для категории пользователей «все остальные»

![Чтение и запись для категории пользователей «все остальные»](../images/23.jpg){ #fig:022 width=80% height=80% }

# От пользователя guest2 прочитали файл /tmp/file01.txt

![Чтение файла /tmp/file01.txt](../images/24.jpg){ #fig:023 width=80% height=80% }

# От пользователя guest2 дозаписали файл /tmp/file01.txt

![Дозапись файла /tmp/file01.txt](../images/25.jpg){ #fig:024 width=80% height=80% }

# От пользователя guest2 перезапись файла /tmp/file01.txt

![Перезапись файла /tmp/file01.txt](../images/27.jpg){ #fig:025 width=80% height=80% }

# Попытка удалить файл /tmp/file01.txt

![Попытка удаления файла /tmp/file01.txt](../images/29.jpg){ #fig:027 width=80% height=80% }

# От пользователя guest2 проверили, что атрибута t у директории /tmp нет

![Проверка атрибутов]](../images/30.jpg){ #fig:029 width=80% height=80% }

# Повторили предыдущие шаги

![Проверка атрибутов](../images/31.jpg){ #fig:030 width=80% height=80% }


# Вывод

Изучили механизмы изменения идентификаторов, применения SetUID- и Sticky-битов.

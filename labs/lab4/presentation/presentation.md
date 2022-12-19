---
## Front matter
lang: ru-RU
title: "Лабораторная работа №4"
subtitle: "Дискреционное разграничение прав в Linux. Расширенные атрибуты"
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

Получение практических навыков работы в консоли с расширенными
атрибутами файлов.

# Определила расширенные атрибуты файла file1

![Определение расширенных атрибутов файла](../images/1.jpg){ #fig:001 width=80% height=80% }

# Установила на файл file1 права, разрешающие чтение и запись

![Права, разрешающие чтение и запись для владельца](../images/2.jpg){ #fig:002 width=80% height=80% }

# Попробовала установить на файл /home/guest/dir1/file1 расширенный атрибут a

![Установка расширенного атрибута от имени обычного- и суперпользователя](../images/3.jpg){ #fig:003 width=80% height=80% }

# От пользователя guest проверила правильность установления атрибута

![Правильность установления атрибута](../images/4.jpg){ #fig:004 width=80% height=80% }

# Выполнила дозапись в файл file1

![Запись и чтение файла](../images/5.jpg){ #fig:005 width=80% height=80% }

# Попробовала удалить файл

![Попытка удаления файла файла](../images/6.jpg){ #fig:006 width=80% height=80% }

# Попробовала перезаписать файл

![Запись в файл](../images/7.jpg){ #fig:001 width=80% height=80% }

# Попробовала переименовать файл

![Попытка изменения прав доступа файла](../images/7.jpg){ #fig:007 width=80% height=80% }

# Сняла расширенный атрибут a с файла

![Снятие расширенного атрибута а](../images/8.jpg){ #fig:008 width=80% height=80% }

# Повторила операции, которые ранее не удавалось выполнить

![Повтор операций](../images/9.jpg){ #fig:009 width=80% height=80% }

# Заменила атрибут «a» атрибутом «i»

![Добавление атрибута i и операции с новым атрибутом](../images/10.jpg){ #fig:010 width=80% height=80% }

# Вывод

Опробовали на практике действие расширенных атрибутов «а» и «i».
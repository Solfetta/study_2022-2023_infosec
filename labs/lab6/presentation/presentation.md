---
## Front matter
lang: ru-RU
title: "Лабораторная работа №6"
subtitle: "Мандатное разграничение прав в Linux"
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

Развить навыки администрирования ОС Linux. Получить первое практическое знакомство с технологией SELinux1. Проверить работу SELinux на практике совместно с веб-сервером Apache.

# Убедилась, что SELinux работает в режиме enforcing политики targeted

![Режим SELinux](../images/1.jpg){ #fig:001 width=80% height=80% }

# Запустила веб-сервер

![Проверка работы веб-сервера](../images/2.jpg){ #fig:001 width=80% height=80% }

# Нашла веб-сервер Apache в списке процессов

![Список процессов](../images/3.jpg){ #fig:001 width=80% height=80% }

# Текущее состояние переключателей SELinux для Apache

![Состояние переключателей SELinux](../images/4.jpg){ #fig:001 width=80% height=80% }

# Статистика по политике

![Статистика SELinux](../images/5.jpg){ #fig:001 width=80% height=80% }

# Тип поддиректорий в директории /var/www 

![Тип поддиректорий в директории /var/www](../images/6.jpg){ #fig:001 width=80% height=80% }

# Круг пользователей с разрешением на создание файлов в /var/www/html

![Право на создание файлов](../images/8.jpg){ #fig:001 width=80% height=80% }

# Создала html-файл /var/www/html/test.html

![HTML-файл /var/www/html/test.html](../images/9.jpg){ #fig:001 width=80% height=80% }

# Проверила контекст созданного файла

![Контекст файла](../../image/9.png){ #fig:001 width=80% height=80% }

# Обратилась к файлу через веб-сервер

![Отображение файла test.html](../images/11.jpg){ #fig:001 width=80% height=80% }

# Изменила контекст файла /var/www/html/test.html

![Изменение контекста файла](../images/13.jpg){ #fig:001 width=80% height=80% }

# Обратилась к файлу через веб-сервер

![Доступ через веб-сервер](../images/14.jpg){ #fig:001 width=80% height=80% }

# Log-файлы веб-сервера Apache

![log-файл](../images/15.jpg){ #fig:001 width=80% height=80% }

# Посмотрела системный лог-файл

![Системный log-файл](../images/15_1.jpg){ #fig:001 width=80% height=80% }

# Запустила веб-сервер Apache на прослушивание ТСР-порта
81

![Включение прослушивания 81 порта](../images/16.jpg){ #fig:001 width=80% height=80% }

# Добавила порт 81 в список портов

![Список портов](../images/19.jpg){ #fig:001 width=80% height=80% }

# Вернула контекст httpd_sys_cоntent__t и обратилась к файлу через веб-сервер

![Контекст файла и отображение страницы](../images/21.jpg){ #fig:001 width=80% height=80% }

# Исправила конфигурационный файл apache

![Конфигурационный файл Apache](../images/22.jpg){ #fig:001 width=80% height=80% }

# Попробовала удалить привязку http_port_t к 81 порту

![Удаление порта из списка](../images/23.jpg){ #fig:001 width=80% height=80% }

# Удалила файл /var/www/html/test.html

![Удаление файла](../images/24.jpg){ #fig:001 width=80% height=80% }

# Вывод

Получили практическое знакомство с технологией SELinux1. Проверили работу SELinx на практике совместно с веб-сервером Apache.

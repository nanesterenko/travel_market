## Автоматизированное тестирование UI ##
### Сайт бронирования отелей https://cypress-tourism-app.herokuapp.com/ ###

[![CI Test Travel_Market](https://github.com/nanesterenko/travel_market/actions/workflows/test_travel_market.yml/badge.svg?branch=master)](https://github.com/nanesterenko/travel_market/actions/workflows/test_travel_market.yml)
![TeamCity build status](http://188.120.227.87:8111/app/rest/builds/buildType:id:AntennaTravelMarket_Test/statusIcon.svg)
---

#### Локальный запуск: ####

Необходим Python версии 3.9 и выше

При первом запуске надо создать виртуальное окружение:

```angular2html
python3 -m venv env
```

Активировать виртуальное окружение:

```angular2html
source env/bin/activate
```

Нужно установить зависимости проекта:

```angular2html
pip3 install -r requirements.txt
```

Запуск тестов:

```angular2html
pytest
```


Локальная проверка кода организована через pre-commit.
Подробнее https://pre-commit.com/


Логирование реализовано через пакет logging.
Подробнее https://docs.python.org/3/library/logging.html

---

#### Тестовая документация ####

Выполняемые тесты описаны в проекте через docstrings.
Также описание подтягивается в отчет Allure

---

#### Отчет через Allure: #### 

Запуск тестов с генерацией данных для отчета
```angular2html
pytest --alluredir=allure_results
```

Подготовка отчета
```angular2html
allure serve allure_results
```

---

#### Критерии проекта: #### 
 
 - [x] Необходимо настроить CI. В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с CI.

 - [x] Необходимо настроить линтер (программа, которая проверяет код на соответствие стандартам в соответствии с определенным набором правил), который должен запускаться локально/на стороне CI

 - [x] К каждому тесту должны присутствовать тест кейсы 

 - [x] README.md заполнен и содержит актуальную информацию

 - [x] В файле README.md стоят бейджики CI

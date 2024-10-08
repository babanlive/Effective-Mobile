## Установка и запуск проекта

1. Установка Poetry

Linux, macOS, Windows (WSL)

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

2. Клонируйте репозиторий и перейдите в папку проекта:

```shell
git clone git@github.com:babanlive/Effective-Mobile.git && cd Effective-Mobile
```

3. Установка проекта(зависимостей):

```shell
poetry install
```

4. Создание файла .env
- Создайте в папке приложения файл `.env` согласно образцу [.env_example](.env.example)

## "E2E UI" ТЕСТ

### Цель:
Создать автоматический e2e тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium или Playwright. Тест должен проверять процесс от авторизации до завершения покупки, с возможностью легко воспроизвести его на любом компьютере.

### Запуск теста:

```shell
poetry run python E2E-UI/main.py
```

## "GitHub API" ТЕСТ

### Цель:
Создать автоматический тест для проверки работы с GitHub API на языке Python. Тест должен уметь создавать, проверять наличие и удалять репозиторий на GitHub. Необходимо предоставить решение, которое легко воспроизводимо на любом компьютере.

### Запуск теста:

```shell
poetry run python Api-Github/test_api.py  
```

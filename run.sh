#!/bin/bash

INBOX_DIR="inbox"
PROCESSED_DIR="processed"
LOG_FILE="run.log"

echo "---Запуск скрипта автоматизации---"

if [ ! -d "$INBOX_DIR" ]; then
    echo "Папка  $INBOX_DIR не найдена. Создаю пустую папку..."
    mkdir -p "$INBOX_DIR"
    echo "Папка $INBOX_DIR создана. Скопируйте письма в папку $INBOX_DIR и запустите скрипт заново."
    exit 1
fi

mkdir -p "$PROCESSED_DIR"

echo "Запуск классификации (вывод ошибкок в $LOG_FILE)..."
py main.py 2>> "$LOG_FILE"

EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
    echo "Программа завершилась успешно: обработка почты завершена!"
else
    echo "ОШИБКА: Программа завершилась с кодом $EXIT_CODE. Проверьте $LOG_FILE."
fi

exit $EXIT_CODE
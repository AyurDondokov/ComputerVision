import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('Task3.png')

# Конвертация изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Бинаризация изображения (преобразование в черно-белое)
_, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Поиск контуров символов
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Словарь для хранения количества символов
character_counts = {}

# Перебор контуров
for contour in contours:
    # Вычисление границ контура
    x, y, w, h = cv2.boundingRect(contour)

    # Выделение символа на изображении
    character = gray[y:y+h, x:x+w]

    # Проверка, является ли символ достаточно большим
    if w > 10 and h > 10:
        # Ввод символа от пользователя
        symbol = input(f'Введите символ для контура ({x}, {y}): ')

        # Обновление счетчика символов
        character_counts[symbol] = character_counts.get(symbol, 0) + 1

# Вывод результатов
for symbol, count in character_counts.items():
    print(f'Символ {symbol}: {count} шт.')
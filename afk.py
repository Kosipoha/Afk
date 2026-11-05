import ctypes
import time
import math

# Настройки
RADIUS = 100     # Радиус круга в пикселях
STEP = 0.2       # Шаг угла (больше = быстрее крутится)
SPEED = 0.02     # Задержка между шагами

MOUSEEVENTF_MOVE = 0x0001
user32 = ctypes.windll.user32

def main():
    print("=" * 40)
    print("AFK скрипт - RF Online Next")
    print("=" * 40)
    print("Запуск через 3 секунды...")
    print("Остановка: Ctrl+C в этом окне")
    print()

    time.sleep(3)

    angle = 0.0
    px, py = float(RADIUS), 0.0

    try:
        while True:
            angle += STEP
            x = RADIUS * math.cos(angle)
            y = RADIUS * math.sin(angle)

            dx = int(round(x - px))
            dy = int(round(y - py))

            if dx or dy:
                user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)

            px, py = x, y
            time.sleep(SPEED)
    except KeyboardInterrupt:
        print("\nОстановлено")

if __name__ == "__main__":
    main()
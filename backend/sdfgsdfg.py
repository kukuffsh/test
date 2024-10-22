import matplotlib.pyplot as plt

# Данные
current = 4  # Сила тока (А)

# ЭДС для катушек
emf_no_core_1 = 5.7
emf_with_core_1 = 15.1
emf_no_core_2 = 2.5
emf_with_core_2 = 14.6

# Площадь поперечного сечения (мм^2)
areas = [531, 531, 531]  # Условно одинаковая площадь
emf_values_area = [5.7, 2.5, 5.7]  # ЭДС для каждой катушки

# Напряжение на источнике (В)
voltage = 4  # Напряжение на источнике
emf_values_voltage = [5.7, 2.5, 5.7]  # ЭДС для каждой катушки

# График 1: Зависимость ЭДС от силы тока
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot([current], [emf_no_core_1], 'o', label='Катушка 1 без сердечника')
plt.plot([current], [emf_with_core_1], 'o', label='Катушка 1 с сердечником')
plt.plot([current], [emf_no_core_2], 'o', label='Катушка 2 без сердечника')
plt.plot([current], [emf_with_core_2], 'o', label='Катушка 2 с сердечником')
plt.xlabel('Сила тока (А)')
plt.ylabel('ЭДС (В)')
plt.title('Зависимость ЭДС от силы тока')
plt.legend()

# График 2: Зависимость ЭДС от площади поперечного сечения
plt.subplot(3, 2, 2)
plt.plot(areas, emf_values_area, 'o')
plt.xlabel('Площадь поперечного сечения (мм^2)')
plt.ylabel('ЭДС (В)')
plt.title('Зависимость ЭДС от площади поперечного сечения')

# График 3: Зависимость ЭДС от напряжения на источнике
plt.subplot(3, 2, 3)
plt.plot([voltage] * len(emf_values_voltage), emf_values_voltage, 'o')
plt.xlabel('Напряжение на источнике (В)')
plt.ylabel('ЭДС (В)')
plt.title('Зависимость ЭДС от напряжения на источнике')

# График 4: Зависимость ЭДС от напряжения на источнике для катушек с одинаковой площадью
plt.subplot(3, 2, 4)
plt.plot([voltage] * 2, [emf_no_core_1, emf_no_core_2], 'o', label='Без сердечника')
plt.plot([voltage] * 2, [emf_with_core_1, emf_with_core_2], 'o', label='С сердечником')
plt.xlabel('Напряжение на источнике (В)')
plt.ylabel('ЭДС (В)')
plt.title('Зависимость ЭДС от напряжения на источнике для катушек')
plt.legend()

plt.tight_layout()
plt.show()

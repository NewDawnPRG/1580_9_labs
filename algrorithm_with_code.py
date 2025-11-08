import sys
import math

def get_coef(index, prompt):
    # Ввод коэффициентов
    while True: 
        # Пробуем получить коэффициент из аргументов командной строки
        try:
            coef_str = sys.argv[index]
        # Если аргументов нет - выводим приглашение и ждем ввод пользователя
        except:
            print(prompt)
            coef_str = input()
        # Пробуем преобразовать введенное значение в число
        try:
            return float(coef_str)
        # Если преобразование не удалось - выводим ошибку и повторяем ввод
        except ValueError:
            print("Ошибка: введите действительное число. Попробуйте снова.")

def get_roots(a, b, c):
    """
    Функция решения квадратного уравнения.

    Вычисляем дискриминант D квадратного уравнения a*x² + b*x + c = 0
    Если дискриминант меньше нуля:
        Возвращаем пустое множество корней
    Если дискриминант равен нулю:
       Находим единственный корень
       Возвращаем его
    Если дискриминант больше нуля:
       Находим корни
       Возвращаем их
    """
    result = []
    D = b**2 - 4*a*c
    
    if D < 0.0:
        return result  
    elif D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    else:
        sqrtD = math.sqrt(D)
        root1 = (-b + sqrtD) / (2.0*a)
        root2 = (-b - sqrtD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    
    return result

def main(): # Начало
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:') # Вводим данные пользователя

    roots = get_roots(a, b, c) # Вычисляем корни уравнения
    len_roots = len(roots) # Вычисляем кол-во корней

    if len_roots == 0: # Если корней нет
        print('Нет действительных корней') # Выведем что корней нет
    elif len_roots == 1: # Если есть 1 корень
        print('Один корень: {}'.format(roots[0])) # Укажем найденый корень
    else: # Если есть два корня
        print('Два корня: {} и {}'.format(roots[0], roots[1])) # Выведем оба корня

if __name__ == "__main__":
    main()
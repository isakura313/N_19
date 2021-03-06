import random
import math
#возьмем встроенную библиотеку random для случайных значений
inches = 40 #дюйму
centimtre = 101.6 #сантиметры

def kid_neuro(epoch, lr, accur):
    """
    epoch - сколько раз она попробует подобрать правильный вес
    lr - learning rate -какими шагами мы попробуем двигаться?
    accur  - какая точность для нас является удовлетворительной?
     """
    W_coef = random.uniform(1,3)
    print(f"Наш первональный вес равен: {W_coef}") #чтобы понимать, что нам выкинул рандом
    for i in range(epoch): # воспользуемся циклами для создания прокрутки эпох
        Error = centimtre - (inches * W_coef)
        #e или error - ошибка тоже важный элемент нейронной сети
        print(f"Наша ошибка составляет {Error}") #будем печатать ошибки для визуализации

        if abs(Error) < accur:
            print(f"Наш итогвый результат {W_coef}")
            #нас интересует только значение по модулю
        if Error > 0:
            W_coef += lr
            #если ошибка у нас положительная, тогда нам нужно начать наращивать вес
        elif Error < 0:
            W_coef -= lr
            #если ошибка у нас отрицательная, тогда нам нужно уменьшить вес
        

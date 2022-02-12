from pygame import *
# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((700, 500))
background = transform.scale(image.load("fon.jpg"), (win_width, win_height))


# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
game = True # флаг сбрасывается кнопкой закрытия окна
while game:
    window.blit(background, (0,0))
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False


        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
tempo = 0
cronometro = 0
pontuação = 0

def on_button_pressed_a():
    global cronometro
    global pontuação
    cronometro = input.running_time()
    pontuação = cronometro
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global tempo
    tempo = cronometro
    if pontuação == 7000:
        basic.show_string('Voce ganhou')
        basic.show_number(input.running_time())
    elif pontuação != 7000:
        basic.show_string('Voce perdeu')
        basic.show_number(abs(input.running_time()))
input.on_button_pressed(Button.B, on_button_pressed_b)

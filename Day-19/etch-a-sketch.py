from turtle import Turtle, Screen

tim = Turtle()
window = Screen()


tim_forward = False
tim_backward = False
tim_left = False
tim_right = False

def move_tim_forward():
    global tim_forward
    tim_forward = True
    tim_backward = False
def stop_tim_forward():
    global tim_forward
    tim_forward = False
    tim_backward = True

def move_tim_backward():
    global tim_backward
    tim_backward = True
def stop_tim_backward():
    global tim_backward
    tim_backward = False


def move_tim_right():
    global tim_right
    tim_right = True
def stop_tim_right():
    global tim_right
    tim_right = False

def move_tim_left():
    global tim_left
    tim_left = True
def stop_tim_left():
    global tim_left
    tim_left = False


def move_tim():
    global tim_forward
    if tim_forward:
        tim.forward(10)
    
    global tim_backward
    if tim_backward:
        tim.backward(10)

    global tim_right
    if tim_right:
        tim.right(10)

    global tim_left
    if tim_left:
        tim.left(10)

    window.ontimer(move_tim, 100)



def clear():
    tim.clear()
window.listen()

window.onkey(key="c", fun=clear)

window.onkeypress(key="w", fun=move_tim_forward)
window.onkeyrelease(key="w", fun=stop_tim_forward)

window.onkeypress(key="s", fun=move_tim_backward)
window.onkeyrelease(key="s", fun=stop_tim_backward)

window.onkeypress(key="a", fun=move_tim_right)
window.onkeyrelease(key="a", fun=stop_tim_right)

window.onkeypress(key="d", fun=move_tim_left)
window.onkeyrelease(key="d", fun=stop_tim_left)
move_tim()
window.exitonclick()
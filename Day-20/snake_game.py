from turtle import Turtle, Screen


snake = Turtle()
snake.color("white")
snake.shape("square")

window = Screen()
window.title("Snake Game")
window.bgcolor("Black")
window.setup(width = 600, height = 500)
window.exitonclick()
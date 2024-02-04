import turtle

def draw_pythagoras_tree(t, order, size, angle=45):
    if order == 0:
        return
    else:
        t.forward(size)
        t.left(angle)
        draw_pythagoras_tree(t, order - 1, size * 0.7, angle)
        t.right(2 * angle)
        draw_pythagoras_tree(t, order - 1, size * 0.7, angle)
        t.left(angle)
        t.backward(size)

def main():
    while True:
        recursion_level_input = input("Enter a level of recursion: ")
        if not recursion_level_input.isdigit():
            print('Level of recursion should be a number.')
        else:
            break

    window = turtle.Screen()
    turt = turtle.Turtle()
    turt.penup()
    turt.goto(-75, -225)
    turt.pendown()
    turt.speed(10)
    turt.left(90)
    turt.color("brown")
    draw_pythagoras_tree(turt, int(recursion_level_input), 150)
    window.exitonclick()

if __name__ == "__main__":
    main()

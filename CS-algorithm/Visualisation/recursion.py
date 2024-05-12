import turtle

def setup_turtle():
    t = turtle.Turtle()
    t.speed(1)
    t.setheading(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    return t

def branch(t, length, color_index=0):
    if length == 0: return
    nt = t.clone()
    colors = ['blue', 'brown', 'gray', 'red', 'green', 'pink', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'olive', 'maroon', 'navy']
    nt.color(colors[color_index % len(colors)])
    nt.forward(50)
    nt.left(20)
    branch(nt, length-1, color_index + 1)
    nt.right(40)
    branch(nt, length-1, color_index + 1)
    nt.hideturtle()

def branch_memo(t, length, color_index=0, memo=None):
    if memo is None:
        memo = {}
    if length == 0: return
    if (length, color_index) in memo:
        t = memo[(length, color_index)]
        return t
    nt = t.clone()
    colors = ['blue', 'brown', 'gray', 'red', 'green', 'pink', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'olive', 'maroon', 'navy']
    nt.color(colors[color_index % len(colors)])
    nt.forward(50)
    nt.left(20)
    branch_memo(nt, length-1, color_index + 1, memo)
    nt.right(40)
    branch_memo(nt, length-1, color_index + 1, memo)
    nt.hideturtle()
    memo[(length, color_index)] = nt
    return nt

def visualize_recursion():
    t = setup_turtle()
    branch(t, 7)
    window = turtle.Screen()
    window.exitonclick()

def visualize_recursion_with_memoization():
    t = setup_turtle()
    branch_memo(t, 7)
    window = turtle.Screen()
    window.exitonclick()

visualize_recursion()
visualize_recursion_with_memoization()

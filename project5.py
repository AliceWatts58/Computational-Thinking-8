import turtle, time, random, math
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup

set_background("jail cells 2")
s1 = create_sprite("prisoner",-200,0)
s2 = create_sprite("yellow light (1)",200,0)

# Section 3: define movement controls
def move_up():
    s1.setheading(90)
    s1.forward(15)
        
def move_down():
    s1.setheading(270)
    s1.forward(15)
    
def move_left():
    s1.setheading(180)
    s1.forward(15)
    
def move_right():    
    s1.setheading(0)
    s1.forward(15)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

def move_up():
    s2.setheading(90)
    s2.forward(10)
        
def move_down():
    s2.setheading(270)
    s2.forward(10)
    
def move_left():
    s2.setheading(180)
    s2.forward(10)
    
def move_right():    
    s2.setheading(0)
    s2.forward(10)

window.onkeypress(move_up, "i")
window.onkeypress(move_down, "k")

window.onkeypress(move_left, "j")
window.onkeypress(move_right, "l")

def reset():
    s1.goto(-200,0)
    s2.goto(200,0)
    set_background("jail cells 2")

window.onkeypress(reset,"r")



lives=3



# Section 5: game loop
window.listen()
while True:
    time.sleep(0.1)
    window.update()
    # code for automatic actions goes here

    if s1.xcor() >300:
        set_background("you win 2")

    if get_distance(s1,s2) < 50:
        lives-=1
        s1.goto(-200,0)
        s2.goto(200,0)

    if lives < 1:
        set_background("you lose")
        window.update()
        time.sleep(5)
        break
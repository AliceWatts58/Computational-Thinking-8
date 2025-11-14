# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(jailcells2):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{jailcells2}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{jailcells2}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)

# Section 3: movement controls
def move_up():
    s1.setheading(90)
    s1.forward(10)
        
def move_down():
    s1.setheading(270)
    s1.forward(10)
    
def move_left():
    s1.setheading(180)
    s1.forward(10)
    
def move_right():    
    s1.setheading(0)
    s1.forward(10)

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

# Section 2: Setup
# TODO - set your background
# TODO - set the starting value for your variable

# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  

	s1 = create_sprite ("prisoner",-90,-30)
	s2 = create_sprite ("yellow light (1)" ,90,-30)
	set_background("jail cells 2")
    
 	# TODO - code for automatic actions
	






	window.update()

	# if :
	# 	break
	

print("Game Over")
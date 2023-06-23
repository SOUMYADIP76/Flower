import turtle


t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(300)
col=['yellow','blue','white','green','purple','red']
c=0

for i in range(150):
    t.forward(i*2)
    t.right(69)
    t.color(col[c])
    if c==5:
        c=0
    else:
        c+=1

t.forward(50)
t.hideturtle()
turtle.done()

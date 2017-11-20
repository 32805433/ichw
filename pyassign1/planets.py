import turtle, math

def oval(a, b, t):
    c = []
    for j in range(6):
        c.append((a[j]*a[j] - b[j]*b[j]) ** 0.5)
        t[j].penup()
        t[j].goto(a[j] + c[j], 0)
        t[j].pendown()
    for i in range(1001):
        for j in range(6):
            co = math.cos(math.pi * i * (9-j) / 500)
            si = math.sin(math.pi * i * (9-j) / 500)
            r = b[j] * b[j] / (a[j] - c[j]*co)
            t[j].goto(r * co, r * si)
        
a = [23.2, 36.3, 50.7, 83.0, 271.9, 502.3]
b = [15.3, 35.8, 49.0, 68.9, 247.0, 449.0]
t = [turtle.Pen(), turtle.Pen(), turtle.Pen(), turtle.Pen(), turtle.Pen(), turtle.Pen()]
colors = ["blue", "green", "red", "black", "orange", "cyan"]
for j in range(6):
    t[j].pensize(2);
    t[j].speed(0)
    t[j].shape("circle")
    t[j].color(colors[j])
tt = turtle.Pen("circle")
tt.color("yellow")
oval(a, b, t)
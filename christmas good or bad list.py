import turtle

window = turtle.Screen()
window.bgcolor("sky blue")

tree = turtle.Turtle()
tree.color("forest green")

tree.setposition(50, -50)
tree.setposition(-50, -50)
tree.setposition(0, 0)
tree.begin_fill()
tree.setposition(50, -50)
tree.setposition(-50, -50)
tree.setposition(0, 0)
tree.end_fill()
def make_tree_segment():
    tree.begin_fill()
    tree.setposition(50, -50)
    tree.setposition(-50, -50)
    tree.setposition(0, 0)
    tree.end_fill()
    
make_tree_segment()
def make_tree_segment(size):
    tree.begin_fill()
    tree.setposition(size, -size)
    tree.setposition(-size, -size)
    tree.setposition(0, 0)
    tree.end_fill()
    make_tree_segment(50)
    def make_tree_segment(size, top_position):

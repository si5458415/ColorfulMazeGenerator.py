import random

# Генерация лабиринта
def generate_maze(width, height):
    maze = [[0 for x in range(width)] for y in range(height)]
    
    def create_path(x, y):
        maze[y][x] = 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                maze[(y+ny)//2][(x+nx)//2] = 1
                create_path(nx, ny)
    
    create_path(random.randint(0, width-1), random.randint(0, height-1))
    
    return maze

# Отображение лабиринта
def display_maze(maze):
    from PIL import Image, ImageDraw
    
    w, h = len(maze[0]), len(maze)
    cell_size = 10
    
    img = Image.new("RGB", (w*cell_size, h*cell_size))
    draw = ImageDraw.Draw(img)
    
    for y in range(h):
        for x in range(w):
            if maze[y][x] == 1:
                draw.rectangle((x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    img.show()

# Пример использования
maze = generate_maze(50, 30)
display_maze(maze)

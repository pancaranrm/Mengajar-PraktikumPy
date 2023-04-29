import pygame

# init 
pygame.init()
# var running game
isRun = True

# membuat disp surface object
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((500,500))

# object game
x = 250
y = 250

# ukuran 
panjang = 20
lebar = 20

# kecepatan
speed = 10 
    
while isRun:
    pygame.time.delay(10)
# user input, database input
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           isRun = False
           
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

# klik kiri
    if keys [pygame.K_LEFT] and x > 0:
        x-= speed

    # klik kanan
    if keys [pygame.K_RIGHT] and x < window_lebar-lebar:
        x+= speed
        
    if keys [pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
        
    if keys [pygame.K_UP] and y > 0:
        y -= speed    
    
    
    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))
    # render display
    pygame.display.update()
        
    
pygame.quit()



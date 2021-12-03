print(1)
import pygame
print(2)
import pygame_gui
print(3)
import element
print(4)

#from package.subpackage import subpackage1

pygame.init()
print(11)
pygame.display.set_caption('Quick Start')
print(12)
window_surface = pygame.display.set_mode((800, 600))
print(13)
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
print(14)
manager = pygame_gui.UIManager((800, 600))
print(15)
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello main',
                                            manager=manager)
print(16)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        manager.process_events(event)
        element.elementManager.process_events(event)
        if event.type == pygame.QUIT:
           is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print('Hello World!')

        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        element.elementManager.update(time_delta)
        element.elementManager.draw_ui(window_surface)

        pygame.display.update()

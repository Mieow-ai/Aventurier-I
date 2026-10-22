import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, left, top, images, scale, animation_time=0.04, loop=True):
        super().__init__()
        self.images = []
        width = None
        height = None
        for path in images:
            image = pygame.image.load(path)
            if width is None:
                width = image.get_width()*scale
            if height is None:
                height = image.get_height()*scale
            self.images.append(pygame.transform.scale(image, (width , height)))
        self.image = self.images[0]
        self.rect = pygame.Rect(left, top, width, height)
        self.index = 0
        self.animation_time = animation_time
        self.current_time = 0
        self.loop = loop  # <-- Ajouté
        self.finished = False  # <-- Ajouté
        
    def select_frame(self, index):
        self.index = index
        
    def update(self, dt):
        if self.finished:
            return
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            if self.loop:
                self.index = (self.index + 1) % len(self.images)
            else:
                if self.index < len(self.images) - 1:
                    self.index += 1
                else:
                    self.finished = True
            self.image = self.images[self.index]
        
    def move(self, left, top):
        x = left - self.rect.left
        y = top - self.rect.top
        self.rect.move_ip(x, y)
        

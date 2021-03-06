class Settings:
    def __init__(self):
        #main
        self.screen_width = 1280
        self.screen_height = 700
        self.bg_color = (253, 171, 159)
        self.caption = "Space Shooters"
        
        #ship
        self.image = "images/ship.bmp"
        self.ship_speed = 1.5

        #bullet
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #alien
        self.alien_image = "images/alien.bmp"
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

    


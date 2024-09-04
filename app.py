from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/tic_tac_toe')
def tic_tac_toe():
    return render_template('index_3pl.html')
@app.route('/start_game')
def start_game():
    import sys
    import pygame

    # Initialize Pygame
    pygame.init()

    #set window frame
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 600

    # Set up the game window
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Leap to Adventure: The Jumping Journey Begins!")
    pygame.display.update()

    #background image
    background_image=pygame.image.load("firstcollegeproject /project/static/mainback.jpeg")

    obstacle_image=pygame.image.load("firstcollegeproject /project/static/icecream.jpeg")
    obstacle_image1=pygame.image.load("firstcollegeproject /project/static/french fries.jpeg")
    obstacle_image2=pygame.image.load("firstcollegeproject /project/static/juice.jpeg")
    obstacle_image3=pygame.image.load("firstcollegeproject /project/static/chocolate.jpeg")
    obstacle_image4=pygame.image.load("firstcollegeproject /project/static/glassjuice.jpeg")
    obstacle_image5=pygame.image.load("firstcollegeproject /project/static/pastries.jpeg")
    obstacle_image6=pygame.image.load("firstcollegeproject /project/static/cupicecream.jpeg")
    boy_image=pygame.image.load("firstcollegeproject /project/static/boy.jpeg")
    # Set up the colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0 ,0)
    blue = (0,0,255)
    pink = (220,20,50)

    #variables
    velocity_x=0
    velocity_y=0
    pos_x=0
    pos_y=400
    size=40
    fps=60
    score=0
    #jumping variables
    jumping=False
    jump_count=11
    #obstacle variables
    obs_x,obs_y,obs_b,obs_h=170,380,50,90
    obs_x1,obs_y1,obs_b1,obs_h1=320,380,60,90
    obs_x2,obs_y2,obs_b2,obs_h2=490,380,60,90
    obs_x3,obs_y3,obs_b3,obs_h3=650,380,50,90
    obs_x4,obs_y4,obs_b4,obs_h4=790,380,50,90
    obs_x5,obs_y5,obs_b5,obs_h5=940,380,70,90
    obs_x6,obs_y6,obs_b6,obs_h6=1110,380,60,90

    #sounds 
    sound_play=pygame.mixer.Sound("firstcollegeproject /project/static/boyjump.mpeg")
    sound_play1=pygame.mixer.Sound("firstcollegeproject /project/static/endsound.mpeg")
    #obstacle image breadth and heigth
    obstacle_image=pygame.transform.scale(obstacle_image,(obs_b,obs_h))
    obstacle_image1=pygame.transform.scale(obstacle_image1,(obs_b1,obs_h1))
    obstacle_image2=pygame.transform.scale(obstacle_image2,(obs_b2,obs_h2))
    obstacle_image3=pygame.transform.scale(obstacle_image3,(obs_b3,obs_h3))
    obstacle_image4=pygame.transform.scale(obstacle_image4,(obs_b4,obs_h4))
    obstacle_image5=pygame.transform.scale(obstacle_image5,(obs_b5,obs_h5))
    obstacle_image6=pygame.transform.scale(obstacle_image6,(obs_b6,obs_h6))
    boy_image=pygame.transform.scale(boy_image,(40,60))

    clock=pygame.time.Clock()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 6
                    velocity_y = 0  

                if event.key == pygame.K_DOWN:
                    velocity_x = 0
                    velocity_y = 0     

                if event.key == pygame.K_UP and not jumping:  # Check if not jumping
                    jumping = True
                    pygame.mixer.Sound.play(sound_play)



        # Jumping mechanics
        if jumping: 
            if jump_count >= -11:
                neg = 1
                if jump_count < 0:
                    neg = -1
                pos_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 11


        # Check if the rectangle goes out of the screen
        if pos_x < 0 or pos_x > WINDOW_WIDTH:
            pos_x = 10  # Reset position to starting position
            score+=1

        pos_x += velocity_x  

        # Check for collision between the black rectangle and the red rectangle
        if (pos_x < obs_x + obs_b and pos_x + size > obs_x and pos_y < obs_y + obs_h and pos_y + size > obs_y) or  (pos_x < obs_x1 + obs_b1 and pos_x + size > obs_x1 and pos_y < obs_y1 + obs_h1 and pos_y + size > obs_y1) or (pos_x < obs_x2 + obs_b2 and pos_x + size > obs_x2 and pos_y < obs_y2 + obs_h2 and pos_y + size > obs_y2) or (pos_x < obs_x3 + obs_b3 and pos_x + size > obs_x3 and pos_y < obs_y3 + obs_h3 and pos_y + size > obs_y3) or (pos_x < obs_x4 + obs_b4 and pos_x + size > obs_x4 and pos_y < obs_y4 + obs_h4 and pos_y + size > obs_y4) or  (pos_x < obs_x5 + obs_b5 and pos_x + size > obs_x5 and pos_y < obs_y5 + obs_h5 and pos_y + size > obs_y5) or (pos_x < obs_x6 + obs_b6 and pos_x + size > obs_x6 and pos_y < obs_y6 + obs_h6 and pos_y + size > obs_y6):
            # Display "Game Over"
            font = pygame.font.SysFont(None, 50) # type: ignore
            game_over_text = font.render("Try Again!", True, red)
            window.blit(game_over_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 4))
            pygame.mixer.Sound.play(sound_play1)
            pygame.display.update()
            pygame.time.delay(1000)  # Pause for 1 seconds  
            pos_x=0
            velocity_x=0
            velocity_y=0  
            score=0

        #screen color
        window.blit(background_image,(0,0))
        #show images 
        
        window.blit(obstacle_image,(obs_x,obs_y))
        window.blit(obstacle_image1,(obs_x1,obs_y1))
        window.blit(obstacle_image2,(obs_x2,obs_y2))
        window.blit(obstacle_image3,(obs_x3,obs_y3))
        window.blit(obstacle_image4,(obs_x4,obs_y4))
        window.blit(obstacle_image5,(obs_x5,obs_y5))
        window.blit(obstacle_image6,(obs_x6,obs_y6))
        window.blit(boy_image,(pos_x,pos_y))

        #all fonts
        font=pygame.font.SysFont(None,30)  # type: ignore # Set up the font

        text1 = font.render("Press Right arrow key to start", True, blue)  # Render the text
        text2 = font.render("Press Up arrow key to jump", True, blue)
        text3 = font.render("Press Down arrow key to pause", True, blue)
        text_rect = text1.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 11))  # Get the rectangle containing the text
        window.blit(text1, text_rect)  # Draw the text on the screen 
        text_rect = text2.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 6.2))  # Get the rectangle containing the text
        window.blit(text2, text_rect)  # Draw the text on the screen 
        text_rect = text3.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 8))  # Get the rectangle containing the text
        window.blit(text3, text_rect)  # Draw the text on the screen 

        sc = font.render("Score: "+str(score), True, pink)
        window.blit(sc, (WINDOW_WIDTH // 9, WINDOW_HEIGHT // 4))

        
        pygame.display.update()
        clock.tick(fps)
  


if __name__ == '__main__':
    app.run(debug=True)

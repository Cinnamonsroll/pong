import pygame
from paddle import Paddle
from ball import Ball

def main():
    size = (700, 700)
    screen = pygame.display.set_mode(size)
    paddle_1 = Paddle(0)
    paddle_2 = Paddle(1)
    ball = Ball()
    pygame.init()

    running = True
    clock = pygame.time.Clock()

    key_states = {pygame.K_w: False, pygame.K_s: False, pygame.K_UP: False, pygame.K_DOWN: False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in key_states:
                    key_states[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in key_states:
                    key_states[event.key] = False

        screen.fill((0, 0, 0))

        if key_states[pygame.K_w]:
            paddle_1.move_up()
        elif key_states[pygame.K_s]:
            paddle_1.move_down()

        if key_states[pygame.K_UP]:
            paddle_2.move_up()
        elif key_states[pygame.K_DOWN]:
            paddle_2.move_down()

        paddle_1.update_position()
        paddle_1.draw()

        paddle_2.update_position()
        paddle_2.draw()

        ball.update_position()
        ball.check_collision([paddle_1, paddle_2])
        ball.check_wall_collision(size)
        ball.draw()

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"{ball.score_1} - {ball.score_2}", True, (255, 255, 255))
        screen.blit(score_text, (size[0] // 2 - score_text.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

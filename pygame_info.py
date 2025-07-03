import pygame
import sys


# Simple test to isolate the pygame issue
def pygame_debug():
    print("Testing pygame...")
    pygame.init()

    # Test 1: Create a small window
    width, height = 300, 300
    print(f"Creating window: {width}x{height}")

    try:
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Simple Test")
        print("Window created successfully!")

        # Test 2: Draw simple shapes
        clock = pygame.time.Clock()
        running = True
        frame = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Test different colors each second
            if frame < 60:
                screen.fill((255, 0, 0))  # Red
            elif frame < 120:
                screen.fill((0, 255, 0))  # Green
            elif frame < 180:
                screen.fill((0, 0, 255))  # Blue
            else:
                # Draw a checkerboard pattern
                screen.fill((255, 255, 255))  # White background
                for row in range(8):
                    for col in range(8):
                        if (row + col) % 2 == 0:
                            x = col * 30
                            y = row * 30
                            pygame.draw.rect(screen, (0, 0, 0), (x, y, 30, 30))

            pygame.display.flip()
            clock.tick(60)
            frame += 1

            if frame % 60 == 0:
                print(f"Frame {frame}")

            # Auto-quit after 10 seconds
            if frame > 600:
                running = False

        print("Test completed successfully!")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

    pygame.quit()


if __name__ == "__main__":
    pygame_debug()
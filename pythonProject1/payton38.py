import os
import pygame
import time

def main():
    # Initialize the pygame mixer
    pygame.mixer.init()

    # Define the music file name
    music_file = 'runner.mp3'  # Replace with the name of your music file

    # Check if the music file exists
    if os.path.exists(music_file):
        # Load the music file
        pygame.mixer.music.load(music_file)

        # Play the music
        pygame.mixer.music.play()

        # Keep the script running while the music plays
        while pygame.mixer.music.get_busy():
            time.sleep(1)  # Wait for 1 second before checking again
    else:
        print("Music file not found!")

if __name__ == '__main__':
    main()

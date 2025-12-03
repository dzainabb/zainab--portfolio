import time
import sys

def print_lyrics():
    lyrics = [
        'Twinkle, twinkle, little star,',
        'How I wonder what you are!',
        'Up above the world so high,',
        'Like a diamond in the sky.',
        'Twinkle, twinkle, little star,'
    ]
    delays = [1, 1, 1.5, 1.5, 1]

    print ("Starting to sing the song...\n")
    time.sleep(2)  # Initial delay before starting

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else: 
            time.sleep(1)

print_lyrics()
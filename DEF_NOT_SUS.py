import os
import time
import pyautogui
import requests
from io import BytesIO
from PIL import Image
from threading import Thread
from keyboard import block_key







# install packages if need be











# don't look



























# I said don't look
































# I'm very sad :'(












def blockMouseAndKeys(timeout):
    global blocking
    blockStartTime = time.time()
    pyautogui.FAILSAFE = False
    blocking = True
    
    def blockKeys(timeout):
        global blocking
        while blocking:
            if timeout:
                if time.time()-blockStartTime > timeout:
                    return
            for i in range(150):
                #bye bye keyboard
                try: block_key(i)
                except: pass
    def blockMouse(timeout):
        global blocking
        while blocking:
            #bye bye mouse
            def resetMouse(): pyautogui.moveTo(5,5)
            Thread(target=resetMouse).start()
            if timeout:
                if time.time()-blockStartTime > timeout:
                    return
    def blockTimeout(timeout):
        global blocking
        time.sleep(timeout)
        blocking = False
        pyautogui.FAILSAFE = False
        print('Done blocking inputs!')

    print('Blocking inputs...')
    Thread(target=blockKeys, args=[timeout]).start()
    Thread(target=blockMouse, args=[timeout]).start()
    Thread(target=blockTimeout, args=[timeout]).start()




def createGif():
    image_urls = [
        'https://csh.rit.edu/~zrc/gif_Images/i.jpg',
        'https://csh.rit.edu/~zrc/gif_Images/heart.jpg',
        'https://csh.rit.edu/~zrc/gif_Images/you.png',
    ]

    # Download and open images
    frames = []
    for url in image_urls:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert('RGBA')
        frames.append(img)



    # Save the frames as an animated GIF
    frames[0].save('animated.gif', 
                        save_all=True,  # Save all frames
                        append_images=frames[1:],  # Additional frames
                        duration=500,  # Duration of each frame in milliseconds
                        loop=0)  # 0 means the GIF will loop forever



def main():
    blockMouseAndKeys(52)
    createGif()
    os.startfile('animated.gif')
    time.sleep(5)
    os.startfile('https://youtu.be/b65MoVwANq4?si=C34WiFWOX2CV5EEL&t=9')
    time.sleep(15)
    os.startfile('https://youtu.be/ObhmrE6FyNs?si=jM45TErVibgd3v_u&t=41')
    time.sleep(15)
    os.startfile('https://www.youtube.com/watch?v=DLzxrzFCyOs')
    time.sleep(15)
    os.startfile('https://csh.rit.edu/~zrc/gif_Images/chaos.jpeg')


main()
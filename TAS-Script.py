from pynput.keyboard import Key, Controller
from time import *
sleep(4)
kb = Controller()

#if True:
while True:
    kb.press(Key.up)
    sleep(1)
    kb.press(Key.backspace)
    sleep(3)
    kb.release(Key.backspace)
    sleep(2)
    kb.press(Key.right)
    sleep(0.4)
    kb.release(Key.right)
    sleep(1)
    kb.press(Key.left)
    sleep(0.1)
    kb.release(Key.left)
    sleep(1)
    kb.press(Key.left)
    sleep(0.9)
    kb.release(Key.left)
    sleep(1.5)
    kb.press(Key.right)
    sleep(0.5)
    kb.release(Key.right)
    sleep(3)
    sleep(1.1)
    kb.press(Key.left)
    sleep(2)
    kb.release(Key.left)
    sleep(2.1)
    kb.press(Key.left)
    sleep(1.94)
    kb.release(Key.left)
    sleep(3)
    kb.press(Key.right)
    sleep(0.1)
    kb.release(Key.right)
    sleep(13)
    kb.release(Key.up)
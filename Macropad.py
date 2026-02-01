import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner
from kmk.scanners.keypad import KeysScanner

from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.matrix = MatrixScanner(
    rows=(board.D7, board.D6),
    cols=(board.D9, board.D10, board.D11),
    columns_to_anodes=False,
)

# Encoder button (acts like a normal key)
encoder_button = KeysScanner(
    pins=(board.D5,),
    value_when_pressed=False,      # Active LOW (pressed = GND)
)

keyboard.coord_mapping = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    6,
]

keyboard.matrix = [
    keyboard.matrix,
    encoder_button,
]

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D3, board.D1),
)

encoder.map = [
    (
        KC.VOLU,   # Turn right
        KC.VOLD,   # Turn left
    ),
]

keyboard.keymap = [
    [
        KC.Macro(Press(KC.LSFT), Press(KC.LCMD), Tap(KC_3), Release(KC.LCMD), Release(KC.LSFT)), KC.W, KC.ESC,
        KC.A, KC.S, KC.D,
        KC.MUTE,   # Encoder press
    ]
]

if __name__ == '__main__':
    keyboard.go()

# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard; keyboard = KMKKeyboard()
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.modtap import ModTap; keyboard.modules.append(ModTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())

keyboard.modules.append(Layers())

split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)
keyboard.debug_enabled = True

keyboard.row_pins = (board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP6)
keyboard.col_pins = (board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Cleaner key names]
_______ = KC.TRNS
XXXXXXX = KC.NO

X_X_X_X = KC.NO

FnKey = KC.MO(1)

colemakdhm_layer = [
    KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
    KC.TAB,     KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,       KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,    KC.PIPE,
    KC.LSFT,    KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.R, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.T, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.M, KC.MT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.E, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.I, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.MT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),KC.RSFT,
    KC.LCTRL,   KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200),KC.RCTRL,
    XXXXXXX, XXXXXXX, KC.LBRC, KC.RBRC, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(1, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.TT(2), KC.P, XXXXXXX,XXXXXXX,
    XXXXXXX, XXXXXXX, KC.VOLD, KC.VOLU, KC.MUTE, KC.LT(3, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),   KC.LT(2, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL),  XXXXXXX,    XXXXXXX,
]

# NUM
number_layer = [
    KC.F1,          KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,      KC.F12,
    KC.TAB, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.PIPE,
    KC.LSFT, KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.RSFT,
    KC.LCTRL, KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.RALT, KC.NO, KC.RCTRL,
    XXXXXXX, XXXXXXX, KC.LBRC, KC.RBRC, KC.DOT, KC.N0, KC.NO, KC.NO, KC.EQL, KC.MINS, XXXXXXX, XXXXXXX,
    XXXXXXX, XXXXXXX, KC.VOLD, KC.VOLU, KC.MUTE, KC.MINS, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL),  XXXXXXX,    XXXXXXX,
]

symbol_layer = [
    KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
    KC.TAB, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.PIPE,
    KC.LSFT, KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.RSFT,
    KC.LCTRL, KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, KC.NO, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.RALT, KC.NO, KC.RCTRL,
    XXXXXXX, XXXXXXX, KC.LBRC, KC.RBRC, KC.LPRN, KC.RPRN,  KC.NO, KC.NO, KC.TT(2), KC.P, XXXXXXX,XXXXXXX,
    XXXXXXX, XXXXXXX, KC.VOLD, KC.VOLU, KC.MUTE,  KC.UNDS,   KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL),  XXXXXXX,    XXXXXXX,
]

mouse_layer = [
    KC.GRV,     KC.N1,                                  KC.N2,                                  KC.N3,                                  KC.N4,                                  KC.N5,      KC.N6,      KC.N7,              KC.N8,              KC.N9,              KC.N0,      KC.BSPC,
    KC.TAB,     KC.TD(KC.NO, KC.RELOAD, tap_time=200),  KC.TD(KC.NO, KC.DF(2), tap_time=200),   KC.TD(KC.NO, KC.DF(1), tap_time=200),   KC.TD(KC.NO, KC.DF(0), tap_time=200),   KC.NO,      KC.NO,      KC.LSFT(KC.INS),    KC.LCTL(KC.INS),    KC.LSFT(KC.DEL),    KC.NO,      KC.PIPE,
    KC.LSFT,    KC.LGUI,                                KC.LALT,                                KC.LCTL,                                KC.LSFT,                                KC.NO,      KC.NO,      KC.MS_LT,           KC.MS_DN,           KC.MS_UP,           KC.MS_RT,   KC.RSFT,
    KC.LCTRL,   KC.NO,                                  KC.RALT,                                KC.TD(KC.NO, KC.DF(8), tap_time=200),   KC.TD(KC.NO, KC.DF(5), tap_time=200),   KC.NO,      KC.NO,      KC.NO,              KC.MW_DN,           KC.MW_UP,           KC.NO,      KC.RCTRL,
    XXXXXXX,    XXXXXXX,                                KC.LBRC,                                KC.RBRC,                                KC.NO,                                  KC.NO,      KC.MB_MMB,  KC.MB_RMB,          KC.TT(2),           KC.P,               XXXXXXX,    XXXXXXX,
    XXXXXXX,    XXXXXXX,                                KC.VOLD,                                KC.VOLU,                                KC.MUTE,                                KC.NO,      KC.MB_LMB,  KC.LSFT(KC.INS),    KC.LCTL(KC.INS),    KC.LSFT(KC.DEL),    XXXXXXX,    XXXXXXX,
]

navigation_layer = [
    KC.GRV,     KC.N1,                                  KC.N2,                                  KC.N3,                                  KC.N4,                                  KC.N5,      KC.N6,                                  KC.N7,              KC.N8,              KC.N9,              KC.N0,      KC.BSPC,
    KC.TAB,     KC.TD(KC.NO, KC.RELOAD, tap_time=200),  KC.TD(KC.NO, KC.DF(2), tap_time=200),   KC.TD(KC.NO, KC.DF(1), tap_time=200),   KC.TD(KC.NO, KC.DF(0), tap_time=200),   KC.NO,      KC.NO,                                  KC.LSFT(KC.INS),    KC.LCTL(KC.INS),    KC.LSFT(KC.DEL),    KC.NO,      KC.PIPE,
    KC.LSFT,    KC.NO,                                  KC.LALT,                                KC.LCTL,                                KC.LSFT,                                KC.NO,      KC.TD(KC.CW, KC.CAPS, tap_time=200),    KC.LEFT,            KC.DOWN,            KC.UP,              KC.RGHT,    KC.RSFT,
    KC.LCTRL,   KC.NO,                                  KC.RALT,                                KC.TD(KC.NO, KC.DF(7), tap_time=200),   KC.TD(KC.NO, KC.DF(4), tap_time=200),   KC.NO,      KC.INS,                                 KC.HOME,            KC.PGDN,            KC.PGUP,            KC.END,     KC.RCTRL,
    XXXXXXX,    XXXXXXX,                                KC.LBRC,                                KC.RBRC,                                KC.NO,                                  KC.NO,      KC.BSPC,                                KC.DEL,             KC.TT(2),           KC.P,               XXXXXXX,    XXXXXXX,
    XXXXXXX,    XXXXXXX,                                KC.VOLD,                                KC.VOLU,                                KC.MUTE,                                KC.NO,      KC.ENT,                                 KC.LSFT(KC.INS),    KC.LCTL(KC.INS),    KC.LSFT(KC.DEL),    XXXXXXX,    XXXXXXX,
]

keyboard.keymap = [
    colemakdhm_layer,
    number_layer,
    symbol_layer,
    mouse_layer,
    navigation_layer
]

if __name__ == '__main__':
    keyboard.go()
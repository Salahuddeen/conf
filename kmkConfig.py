print("Starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.capsword import CapsWord

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Power())
keyboard.modules.append(TapDance())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(CapsWord())

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_side=SplitSide.LEFT,
    split_type=SplitType.UART,
    data_pin=board.GP28,
    data_pin2=board.GP29,
    use_pio=True,
    split_target_left=True
    )

keyboard.modules.append(split)

thumb_one = KC.Q
thumb_two = KC.W
thumb_three = KC.E
thumb_four = KC.R


keyboard.keymap = [

# BASE
[
KC.N1, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT, KC.TAB,
KC.NO, KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.R, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.S, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.T, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.M, KC.HT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.E, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.I, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.GUI,
KC.LSHIFT, KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LSHIFT,
KC.NO, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), thumb_two, thumb_one, thumb_four, thumb_three, KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),
],
# EXTRA
[
KC.N2, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.TAB,
KC.GUI, KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, KC.H, KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.GUI,
KC.LSHIFT, KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LSHIFT,
KC.NO, KC.NO, KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LCTRL
],
# TAP
[
KC.N3, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT, KC.TAB,
KC.GUI, KC.A, KC.R, KC.S, KC.T, KC.G, KC.M, KC.N, KC.E, KC.I, KC.O, KC.GUI,
KC.LSHIFT, KC.Z, KC.X, KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.DOT, KC.SLSH, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.ESC, KC.SPC, KC.TAB, KC.ENT, KC.BSPC, KC.DEL, KC.LCTRL
],
# BUTTON
[
KC.N4, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INS), KC.LSFT(KC.INS), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.TAB,
KC.GUI, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.GUI,
KC.LSHIFT, KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INS), KC.LSFT(KC.INS), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, KC.LCTRL
],
# NAV
[
KC.N5, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.TAB,
KC.LGUI, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.TD(KC.CW, KC.CAPS, tap_time=200), KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.LGUI,
KC.LSHIFT, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.NO, KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL, KC.LCTRL
],
# MOUSE
[
KC.N6, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO, KC.TAB,
KC.LGUI, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, KC.LGUI,
KC.LSHIFT, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.NO, KC.NO, KC.NO, KC.MW_DN, KC.MW_UP, KC.NO, KC.LSHIFT,
KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB, KC.LCTRL
],
# MEDIA
[
KC.N7, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TAB,
KC.LGUI, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.PS_TOG, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT, KC.LGUI,
KC.LSHIFT, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.NO, KC.HID, KC.NO, KC.NO, KC.NO, KC.NO, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.MSTP, KC.MPLY, KC.MUTE, KC.LCTRL
],
# NUM
[
KC.N8, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TAB,
KC.LGUI, KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI,
KC.LSHIFT, KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.RALT, KC.NO, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO, KC.LCTRL
],
# SYM
[
KC.N9, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TAB,
KC.LGUI, KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI,
KC.LSHIFT, KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, KC.NO, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.RALT, KC.NO, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.LPRN, KC.RPRN, KC.UNDS, KC.NO, KC.NO, KC.NO, KC.LCTRL
],
# FUN
[
KC.Q, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
KC.TAB, KC.F12, KC.F7, KC.F8, KC.F9, KC.PSCR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TAB,
KC.LGUI, KC.F11, KC.F4, KC.F5, KC.F6, KC.SLCK, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI,
KC.LSHIFT, KC.F10, KC.F1, KC.F2, KC.F3, KC.PAUS, KC.NO, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.RALT, KC.NO, KC.LSHIFT,
KC.LCTRL, KC.NO, KC.NO, KC.APP, KC.SPC, KC.TAB, KC.NO, KC.NO, KC.NO, KC.LCTRL
],
]

layer_names_list = [
"Base", "Extra", "Tap", "Button", "Nav", "Mouse", "Media", "Num", "Sym", "Fun",
]

if __name__ == '__main__':
     print('starting Miryoku KMK')
     keyboard.go()

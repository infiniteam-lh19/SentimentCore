import subprocess

_command = "g810-led"

def _cmd(args):
    l = [_command]
    l.extend(args)
    subprocess.run(l)

def set_color_key_nc(key, color):
    _cmd(["-kn", key, color])

def set_color_logo_nc(color):
    set_color_key_nc("logo", color)

def set_color_all_nc(color):
    _cmd(["-an", color])

def commit():
    _cmd(["-c"])

def _hex_byte(b):
    return "%02x" % b

def hex(r, g, b):
    return _hex_byte(r) + _hex_byte(g) + _hex_byte(b)
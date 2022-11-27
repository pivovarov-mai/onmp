'''
    This is the file which can help you output something important more adorable
    You can choose color and format for your message
'''
# Black        0;30     Dark Gray     1;30
# Red          0;31     Bold Red      1;31
# Green        0;32     Bold Green    1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37
bash_colors = {
    'black': '0;30',
    'red': '0;31',
    'green': '1;32',
    'orange': '0;33',
    'blue': '0;34',
    'purple': '0;35',
    'cyan': '0;36',
    'light gray': '0;37',
    'dark gray': '1;30',
    'light red': '1;31',
    'light green': '1;32',
    'yellow': '1;33',
    'light blue': '1;34',
    'light purple': '1;35',
    'light cyan': '1;36',
    'white': '1;37',
    'reset': '0',
}

GOOD = bash_colors['green']
WARNING = bash_colors['yellow']
ERROR = bash_colors['red']

def get_full_text_color(clr):
    return f'\033[{clr}m'

def message(msg, color):
    print(f"{get_full_text_color(color)}{msg}{get_full_text_color(bash_colors['reset'])}")

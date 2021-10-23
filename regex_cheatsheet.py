import re

# Base for Cheatsheet
play_string = '''
    abcdefghijklmnopqurtuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
    Ha HaHa
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    lietuva.com
    +37060482010
    +370.604.82.010
    +370-604-82-010
    860482010
'''


pattern = re.compile(r'')

result = pattern.finditer(play_string)


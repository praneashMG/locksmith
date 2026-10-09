import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's forcefully change to fa-phone and add fa-flip-horizontal
    content = content.replace('fa-phone-flip', 'fa-phone fa-flip-horizontal')
    # If there are any fa-phone without fa-flip-horizontal, we could flip them, but let's just do a blanket replace for all fa-phone variants.
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

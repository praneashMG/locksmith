import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's replace 'fa-phone fa-flip-horizontal' with 'fa-phone" style="display:inline-block; transform: scaleX(-1);'
    content = content.replace('class="fas fa-phone fa-flip-horizontal"', 'class="fas fa-phone" style="display:inline-block; transform: scaleX(-1);"')
    content = content.replace('class="fas fa-phone-volume fa-flip-horizontal', 'class="fas fa-phone-volume" style="display:inline-block; transform: scaleX(-1);" ')
    
    # Just in case there are others
    content = content.replace('class="fas fa-phone-alt"', 'class="fas fa-phone" style="display:inline-block; transform: scaleX(-1);"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the inline styles that mirror the icon to the left
    content = content.replace('class="fas fa-phone" style="display:inline-block; transform: scaleX(-1);"', 'class="fas fa-phone"')
    content = content.replace('class="fas fa-phone-volume" style="display:inline-block; transform: scaleX(-1);" ', 'class="fas fa-phone-volume"')
    
    # Also clean up any lingering fa-flip-horizontal or fa-phone-flip from previous attempts
    content = content.replace('fa-phone fa-flip-horizontal', 'fa-phone')
    content = content.replace('fa-phone-flip', 'fa-phone')
    content = content.replace('fa-phone-alt', 'fa-phone')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

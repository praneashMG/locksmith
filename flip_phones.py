import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We replace 'fa-phone-alt' with 'fa-phone fa-flip-horizontal'
    content = content.replace('fa-phone-alt', 'fa-phone fa-flip-horizontal')
    # If they have 'fa-phone-volume', we might also want to flip it:
    content = content.replace('fa-phone-volume', 'fa-phone-volume fa-flip-horizontal')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

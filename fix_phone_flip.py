import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Reset any previous flips
    content = content.replace('fa-phone fa-flip-horizontal', 'fa-phone-flip')
    content = content.replace('fa-phone-alt', 'fa-phone-flip')
    content = content.replace('fa-phone-volume fa-flip-horizontal', 'fa-phone-volume fa-flip-horizontal') # Keep this as fa-flip-horizontal since there is no fa-phone-volume-flip
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

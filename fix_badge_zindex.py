import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # The badge container classes:
    # "w-14 h-14 mx-auto -mt-14 mb-4 rounded-2xl bg-custom-gradient flex items-center justify-center shadow-lg border-4 border-background"
    
    # Let's replace it with the same plus " relative z-10"
    search_str = 'w-14 h-14 mx-auto -mt-14 mb-4 rounded-2xl bg-custom-gradient flex items-center justify-center shadow-lg border-4 border-background'
    replace_str = search_str + ' relative z-10'
    
    content = content.replace(search_str, replace_str)
    
    # Just in case there are other similar badges with a slightly different class string:
    search_str_2 = 'w-14 h-14 mx-auto -mt-12 mb-4 rounded-2xl bg-custom-gradient flex items-center justify-center shadow-lg border-4 border-background'
    replace_str_2 = search_str_2 + ' relative z-10'
    content = content.replace(search_str_2, replace_str_2)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

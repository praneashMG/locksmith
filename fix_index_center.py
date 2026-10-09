import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Target the 'Learn More' and similar inline-flex links that were given mt-auto
    search_link = 'class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all mt-auto"'
    replace_link = 'class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all mt-auto mx-auto"'
    
    content = content.replace(search_link, replace_link)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

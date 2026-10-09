import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add h-full to the services cards
    search = 'class="bg-background rounded-3xl border border-border p-8 shadow-sm hover:shadow-xl hover:border-[#EAB308] transition-all duration-300 text-center group flex flex-col"'
    replace = 'class="bg-background rounded-3xl border border-border p-8 shadow-sm hover:shadow-xl hover:border-[#EAB308] transition-all duration-300 text-center group flex flex-col h-full"'
    content = content.replace(search, replace)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

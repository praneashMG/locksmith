import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add 'flex flex-col' to the card container
    search_card = 'class="bg-background rounded-3xl border border-border p-8 shadow-sm hover:shadow-xl hover:border-[#EAB308] transition-all duration-300 text-center group"'
    replace_card = 'class="bg-background rounded-3xl border border-border p-8 shadow-sm hover:shadow-xl hover:border-[#EAB308] transition-all duration-300 text-center group flex flex-col"'
    content = content.replace(search_card, replace_card)
    
    # 2. Add 'flex-grow' to the paragraph inside these cards.
    # The paragraph is: <p class="text-secondary-text leading-relaxed text-sm mb-5">
    # Wait, this paragraph class is used heavily. It's safe to add flex-grow if it's in a flex-col, 
    # but maybe we should just replace it globally or selectively.
    # Let's add mt-auto to the links instead. That's safer.
    # The links look like: class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all"
    
    search_link = 'class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all"'
    replace_link = 'class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all mt-auto"'
    content = content.replace(search_link, replace_link)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

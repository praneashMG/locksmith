with open('services.html', 'r', encoding='utf-8') as file:
    content = file.read()

search_link = 'class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all mt-auto"'
replace_link = 'class="text-[#EAB308] font-bold text-sm inline-flex items-center gap-2 hover:gap-3 transition-all mt-auto mx-auto"'

content = content.replace(search_link, replace_link)

with open('services.html', 'w', encoding='utf-8') as file:
    file.write(content)

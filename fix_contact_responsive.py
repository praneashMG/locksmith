with open('contact.html', 'r', encoding='utf-8') as file:
    content = file.read()

search_grid = '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">'
replace_grid = '<div class="grid grid-cols-1 lg:grid-cols-3 gap-4 md:gap-6 lg:gap-8 max-w-5xl mx-auto">'

content = content.replace(search_grid, replace_grid)

with open('contact.html', 'w', encoding='utf-8') as file:
    file.write(content)

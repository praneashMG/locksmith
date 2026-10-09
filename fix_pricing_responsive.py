with open('pricing.html', 'r', encoding='utf-8') as file:
    content = file.read()

# 1. Remove the negative margin that pops the middle card out
search_middle = 'class="bg-custom-gradient rounded-3xl p-8 text-center shadow-xl hover:shadow-2xl transition-all flex flex-col relative overflow-hidden md:-mt-4 md:mb-4"'
replace_middle = 'class="bg-custom-gradient rounded-3xl p-8 text-center shadow-xl hover:shadow-2xl transition-all flex flex-col h-full relative overflow-hidden"'
content = content.replace(search_middle, replace_middle)

# 2. Make sure the container grid is nicely spaced on tablet, and the cards have h-full
search_grid = '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">'
replace_grid = '<div class="grid grid-cols-1 md:grid-cols-3 gap-4 lg:gap-8 max-w-5xl mx-auto">'
content = content.replace(search_grid, replace_grid)

# 3. Add h-full to the basic and bulk cards too (if they don't have it)
search_basic = 'class="bg-background rounded-3xl border border-border p-8 text-center shadow-sm hover:shadow-xl transition-all flex flex-col"'
replace_basic = 'class="bg-background rounded-3xl border border-border p-6 lg:p-8 text-center shadow-sm hover:shadow-xl transition-all flex flex-col h-full"'
content = content.replace(search_basic, replace_basic)

with open('pricing.html', 'w', encoding='utf-8') as file:
    file.write(content)

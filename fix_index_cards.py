with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Make the card a flex column
search_card = 'class="group bg-background rounded-3xl border border-border overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-300 hover:-translate-y-1"'
replace_card = 'class="group bg-background rounded-3xl border border-border overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 flex flex-col h-full"'
content = content.replace(search_card, replace_card)

# Make the inner text container a flex column that grows
search_inner = 'class="p-7 text-center"'
replace_inner = 'class="p-7 text-center flex flex-col flex-grow"'
content = content.replace(search_inner, replace_inner)

# Ensure the paragraph inside flex-grow doesn't act weirdly, but since we have mt-auto on the link, it should be fine.

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(content)

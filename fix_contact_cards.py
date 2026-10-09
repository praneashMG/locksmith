with open('contact.html', 'r', encoding='utf-8') as file:
    content = file.read()

# 1. Change 'block' to 'flex flex-col h-full' for the contact cards
# Search string: hover:-translate-y-1 block"
# Replace with: hover:-translate-y-1 flex flex-col h-full"
search_card = 'hover:-translate-y-1 block"'
replace_card = 'hover:-translate-y-1 flex flex-col h-full"'
content = content.replace(search_card, replace_card)

# 2. Push the contact detail to the bottom by adding 'mt-auto' to it
# Search string: class="text-[#B45309] font-black text-lg"
# Replace with: class="text-[#B45309] font-black text-lg mt-auto"
search_text = 'class="text-[#B45309] font-black text-lg"'
replace_text = 'class="text-[#B45309] font-black text-lg mt-auto"'
content = content.replace(search_text, replace_text)

with open('contact.html', 'w', encoding='utf-8') as file:
    file.write(content)

with open('pricing.html', 'r', encoding='utf-8') as file:
    content = file.read()

target = '<i class="fas fa-question text-white text-sm"></i>'

content = content.replace(target, '<span class="text-white text-lg font-black">1</span>', 1)
content = content.replace(target, '<span class="text-white text-lg font-black">2</span>', 1)
content = content.replace(target, '<span class="text-white text-lg font-black">3</span>', 1)
content = content.replace(target, '<span class="text-white text-lg font-black">4</span>', 1)

with open('pricing.html', 'w', encoding='utf-8') as file:
    file.write(content)

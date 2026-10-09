with open('about.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace min-h-[80vh] with min-h-[100vh]
content = content.replace('min-h-[80vh]', 'min-h-[100vh]')

with open('about.html', 'w', encoding='utf-8') as file:
    file.write(content)

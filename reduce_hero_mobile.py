import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Heading
    content = content.replace('text-4xl sm:text-5xl md:text-6xl', 'text-3xl sm:text-5xl md:text-6xl')
    
    # 2. Paragraphs directly under hero (usually text-lg sm:text-xl)
    content = content.replace('text-lg sm:text-xl', 'text-base sm:text-xl')
    
    # 3. Buttons in hero section
    # Usually: px-8 py-4 rounded-full font-bold text-lg
    content = content.replace('px-8 py-4 rounded-full font-bold text-lg', 'px-6 sm:px-8 py-3 sm:py-4 rounded-full font-bold text-base sm:text-lg')
    # And for the outlined buttons which might have slightly different classes
    # e.g., btn-outline px-8 py-4 rounded-full font-bold text-lg
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

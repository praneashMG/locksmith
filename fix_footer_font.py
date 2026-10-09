import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the gray text and sm size classes so it inherits the footer defaults
    search = '<ul class="space-y-4 text-gray-400 text-sm">'
    replace = '<ul class="space-y-4">'
    
    content = content.replace(search, replace)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

import glob
import re

files = glob.glob('*.html')

# We need to add the active ::after style to the head
style_addition = '''
        .nav-link.active::after {
            transform: scaleX(1);
        }
'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '.nav-link.active::after' not in content:
        content = content.replace('.nav-link:hover::after {', style_addition + '        .nav-link:hover::after {')

    # Remove all active states first
    # Desktop
    content = re.sub(r'class="nav-link active py-2 px-3 rounded-full hover:bg-hover text-accent', 'class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent text-primary-text', content)
    
    # Mobile
    content = re.sub(r'class="block text-accent font-bold text-lg py-2 w-full text-left flex justify-between items-center"', 'class="block text-primary-text font-semibold text-lg py-2 w-full text-left flex justify-between items-center"', content)
    
    # Now set the correct one to active based on the filename
    if f == 'index.html':
        # Desktop Home
        content = content.replace('class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent text-primary-text font-semibold transition-all flex items-center gap-1">\n                        Home', 'class="nav-link active py-2 px-3 rounded-full hover:bg-hover text-accent font-semibold transition-all flex items-center gap-1">\n                        Home')
        # Mobile Home
        content = content.replace('class="block text-primary-text font-semibold text-lg py-2 w-full text-left flex justify-between items-center" id="mobile-homes-toggle">\n                        Home', 'class="block text-accent font-bold text-lg py-2 w-full text-left flex justify-between items-center" id="mobile-homes-toggle">\n                        Home')
    
    elif f == 'services.html':
        content = content.replace('href="services.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Services</a>', 'href="services.html" class="nav-link active py-2 px-3 rounded-full hover:bg-hover text-accent font-semibold transition-all">Services</a>')
        content = content.replace('href="services.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Services</a>', 'href="services.html" class="block text-accent font-bold text-lg py-2 hover:text-accent transition-colors">Services</a>')

    elif f == 'pricing.html':
        content = content.replace('href="pricing.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Pricing Guide</a>', 'href="pricing.html" class="nav-link active py-2 px-3 rounded-full hover:bg-hover text-accent font-semibold transition-all">Pricing Guide</a>')
        content = content.replace('href="pricing.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Pricing Guide</a>', 'href="pricing.html" class="block text-accent font-bold text-lg py-2 hover:text-accent transition-colors">Pricing Guide</a>')

    elif f == 'contact.html':
        content = content.replace('href="contact.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Contact</a>', 'href="contact.html" class="nav-link active py-2 px-3 rounded-full hover:bg-hover text-accent font-semibold transition-all">Contact</a>')
        content = content.replace('href="contact.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Contact</a>', 'href="contact.html" class="block text-accent font-bold text-lg py-2 hover:text-accent transition-colors">Contact</a>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)


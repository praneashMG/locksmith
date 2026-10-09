import glob

files = glob.glob('*.html')

desktop_search = '<a href="contact.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Contact</a>'
desktop_replacement = '<a href="locations.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Locations</a>\n                <a href="faq.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">FAQ</a>\n                ' + desktop_search

mobile_search = '<a href="contact.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Contact</a>'
mobile_replacement = '<a href="locations.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Locations</a>\n                <a href="faq.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">FAQ</a>\n                ' + mobile_search

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(desktop_search, desktop_replacement)
    content = content.replace(mobile_search, mobile_replacement)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

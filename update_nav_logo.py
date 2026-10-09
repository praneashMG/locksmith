import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix logo
content = re.sub(r'<img[^>]*src="assets/fav\.png"[^>]*>', '<i class="fas fa-key text-3xl text-[#EAB308]"></i>', content)

# Desktop Nav Replacement
desktop_nav_replacement = '''
            <div class="hidden xl:flex items-center space-x-1 flex-1 justify-center">
                <div class="dropdown-wrapper px-1">
                    <button class="nav-link active py-2 px-3 rounded-full hover:bg-hover text-accent font-semibold transition-all flex items-center gap-1">
                        Home
                        <svg class="w-3 h-3 ml-1 relative top-[1px] transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="dropdown-menu">
                        <a href="index.html">Home 1</a>
                        <a href="home2.html">Home 2</a>
                    </div>
                </div>
                <a href="about.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">About</a>
                <a href="services.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Services</a>
                <a href="pricing.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Pricing Guide</a>
                <a href="contact.html" class="nav-link py-2 px-3 rounded-full hover:bg-hover hover:text-accent font-semibold transition-all text-primary-text">Emergency Contact</a>
            </div>
'''
content = re.sub(r'<div class="hidden xl:flex items-center space-x-1 flex-1 justify-center">.*?</div>\s*<div class="hidden xl:flex items-center space-x-3 rtl:space-x-reverse">', desktop_nav_replacement + '\n            <div class="hidden xl:flex items-center space-x-3 rtl:space-x-reverse">', content, flags=re.DOTALL)


# Mobile Nav Replacement
mobile_nav_replacement = '''
            <nav class="flex flex-col space-y-2 py-4">
                <div>
                    <button class="block text-accent font-bold text-lg py-2 w-full text-left flex justify-between items-center" id="mobile-homes-toggle">
                        Home <svg class="w-4 h-4 transform transition-transform duration-200 text-primary-text" id="homes-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div id="mobile-homes-menu" class="hidden pl-4 flex flex-col space-y-1 mt-1 border-l-2 border-border">
                        <a href="index.html" class="block text-accent hover:text-accent text-base py-1">Home 1</a>
                        <a href="home2.html" class="block text-secondary-text hover:text-accent text-base py-1">Home 2</a>
                    </div>
                </div>
                <a href="about.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">About</a>
                <a href="services.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Services</a>
                <a href="pricing.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Pricing Guide</a>
                <a href="contact.html" class="block text-primary-text font-semibold text-lg py-2 hover:text-accent transition-colors">Emergency Contact</a>
            </nav>
'''
content = re.sub(r'<nav class="flex flex-col space-y-2 py-4">.*?</nav>', mobile_nav_replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

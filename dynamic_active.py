import glob
import re

files = glob.glob('*.html')

js_snippet = '''
<script>
document.addEventListener('DOMContentLoaded', () => {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    // Desktop Nav
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active', 'text-accent', 'font-bold');
        if (!link.classList.contains('text-primary-text')) {
            link.classList.add('text-primary-text');
        }
        
        let isMatch = false;
        if (link.tagName === 'A' && link.getAttribute('href') === currentPage) {
            isMatch = true;
        } else if (link.tagName === 'BUTTON' && (currentPage === 'index.html' || currentPage.startsWith('home')) && link.textContent.trim().startsWith('Home')) {
            isMatch = true;
        }
        
        if (isMatch) {
            link.classList.add('active', 'text-accent');
            link.classList.remove('text-primary-text');
        }
    });

    // Mobile Nav
    document.querySelectorAll('#mobile-menu-drawer nav > a, #mobile-menu-drawer nav > div > button').forEach(link => {
        link.classList.remove('text-accent', 'font-bold');
        if (!link.classList.contains('text-primary-text')) {
            link.classList.add('text-primary-text', 'font-semibold');
        }
        
        let isMatch = false;
        if (link.tagName === 'A' && link.getAttribute('href') === currentPage) {
            isMatch = true;
        } else if (link.tagName === 'BUTTON' && (currentPage === 'index.html' || currentPage.startsWith('home')) && link.textContent.trim().startsWith('Home')) {
            isMatch = true;
        }
        
        if (isMatch) {
            link.classList.add('text-accent', 'font-bold');
            link.classList.remove('text-primary-text', 'font-semibold');
        }
    });
});
</script>
'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove the active underline CSS rule I added
    content = re.sub(r'\s*\.nav-link\.active::after\s*\{\s*transform:\s*scaleX\(1\);\s*\}', '', content)
    
    # 2. Reset hardcoded active states in HTML so JS can take over seamlessly
    content = content.replace('nav-link active', 'nav-link')
    content = content.replace('text-accent font-semibold transition-all', 'hover:text-accent text-primary-text font-semibold transition-all')
    content = content.replace('class="block text-accent font-bold text-lg py-2 w-full text-left flex justify-between items-center"', 'class="block text-primary-text font-semibold text-lg py-2 w-full text-left flex justify-between items-center"')
    
    # 3. Add the JS snippet before </body> if it's not already there
    if 'const currentPage = window.location.pathname.split' not in content:
        content = content.replace('</body>', js_snippet + '\n</body>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

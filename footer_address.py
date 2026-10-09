import glob
import re

files = glob.glob('*.html')

new_col = '''                <div>
                    <h4 class="footer-heading font-medium text-xl mb-6">Contact</h4>
                    <ul class="space-y-4 text-gray-400 text-sm">
                        <li class="flex items-start gap-3"><i class="fas fa-map-marker-alt text-[#FACC15] mt-1"></i> <span>123 Security Avenue,<br>Downtown, NY 12345</span></li>
                        <li class="flex items-center gap-3"><i class="fas fa-phone-alt text-[#FACC15]"></i> <span>(555) 123-4567</span></li>
                        <li class="flex items-center gap-3"><i class="fas fa-envelope text-[#FACC15]"></i> <span>info@securelock.com</span></li>
                    </ul>
                </div>
'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the grid columns
    content = content.replace('lg:grid-cols-5', 'lg:grid-cols-6')
    
    # 2. Insert the new column before Quick Links
    # We will use regex to find the Quick Links div and insert the new_col before it.
    # The structure is roughly: <div>\s*<h4 class="footer-heading font-medium text-xl mb-6">Quick Links</h4>
    
    search_pattern = r'(<div>\s*<h4 class="footer-heading[^"]*">Quick Links</h4>)'
    
    # We only want to replace the first occurrence in the footer, though it should only exist once anyway.
    if 'Contact' not in content or '123 Security Avenue' not in content:
        content = re.sub(search_pattern, new_col + r'\1', content)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

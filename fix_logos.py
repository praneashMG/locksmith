import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Fix Footer Logo
    search_footer_logo = '''<a href="index.html" class="flex items-center gap-2 mb-4">
                        <i class="fas fa-key text-3xl text-[#EAB308]"></i>
                        <h1 class="text-3xl font-serif font-semibold" style="color:#EAB308">SecureLock</h1>
                    </a>'''
    
    replace_footer_logo = '''<a href="index.html" class="flex-shrink-0 flex items-center gap-2 mb-4 group">
                        <i class="fas fa-key text-3xl text-[#EAB308]"></i>
                        <span class="text-2xl font-serif font-black tracking-tight text-[#EAB308]">SecureLock</span>
                    </a>'''
    
    # Also handle in case spacing is slightly different
    content = content.replace(search_footer_logo, replace_footer_logo)
    
    # Try a more robust regex for the footer logo if the simple string replace fails
    import re
    content = re.sub(
        r'<a href="index\.html"[^>]*>\s*<i class="fas fa-key[^>]*></i>\s*<h1[^>]*>SecureLock</h1>\s*</a>',
        replace_footer_logo,
        content
    )

    # 2. Fix Mobile Menu Logo
    search_mobile = '''<a href="index.html" class="flex items-center gap-2">
                    <i class="fas fa-key text-3xl text-[#EAB308]"></i>
                    <span class="text-2xl font-serif font-extrabold tracking-wide" style="color: #EAB308;">SecureLock</span>
                </a>'''
    
    replace_mobile = '''<a href="index.html" class="flex-shrink-0 flex items-center gap-2 group">
                    <i class="fas fa-key text-3xl text-[#EAB308]"></i>
                    <span class="text-2xl font-serif font-black tracking-tight text-[#EAB308]">SecureLock</span>
                </a>'''
                
    content = content.replace(search_mobile, replace_mobile)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

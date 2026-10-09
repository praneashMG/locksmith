with open('404.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace HTML
search_html = '''    <!-- Theme toggle (top-right, minimal) -->
    <div class="absolute top-5 right-5 rtl:right-auto rtl:left-5 z-30">
        <button id="theme-toggle" class="p-2.5 rounded-full bg-hover border border-border shadow-sm text-primary-text hover:text-[#EAB308] transition">
            <svg class="w-5 h-5 light-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            <svg class="w-5 h-5 dark-icon hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </button>
    </div>'''

replace_html = '''    <!-- Theme & RTL toggle (top-right, minimal) -->
    <div class="absolute top-5 right-5 rtl:right-auto rtl:left-5 z-30 flex items-center gap-3">
        <button id="theme-toggle" class="p-2.5 rounded-full bg-hover border border-border shadow-sm text-primary-text hover:text-[#EAB308] transition">
            <svg class="w-5 h-5 light-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            <svg class="w-5 h-5 dark-icon hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </button>
        <button id="lang-icon" class="p-2.5 rounded-full bg-hover border border-border shadow-sm text-primary-text hover:text-[#EAB308] transition" title="Toggle RTL">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7.5 21 3 16.5m0 0L7.5 12M3 16.5h13.5m0-13.5L21 7.5m0 0L16.5 12M21 7.5H7.5" /></svg>
        </button>
    </div>'''

content = content.replace(search_html, replace_html)

# Replace JS
search_js = '''            // Apply stored RTL direction if any
            html.setAttribute('dir', localStorage.getItem('language') === 'ar' ? 'rtl' : 'ltr');
        });'''
        
replace_js = '''            // Apply stored RTL direction if any
            html.setAttribute('dir', localStorage.getItem('language') === 'ar' ? 'rtl' : 'ltr');
            
            const langBtn = document.getElementById('lang-icon');
            if(langBtn) {
                langBtn.addEventListener('click', () => {
                    const current = localStorage.getItem('language') === 'ar' ? 'en' : 'ar';
                    localStorage.setItem('language', current);
                    html.setAttribute('dir', current === 'ar' ? 'rtl' : 'ltr');
                });
            }
        });'''

content = content.replace(search_js, replace_js)

with open('404.html', 'w', encoding='utf-8') as file:
    file.write(content)

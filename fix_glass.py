import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add the .bg-glass CSS definition if not present
    if '.bg-glass' not in content:
        css_glass = '''
        .bg-glass { background-color: rgba(255, 255, 255, 0.95); }
        html[data-theme='dark'] .bg-glass { background-color: rgba(0, 0, 0, 0.85); }
        '''
        # Insert before closing </style>
        content = content.replace('</style>', css_glass + '</style>')
    
    # 2. Replace the broken Tailwind class with our new custom class
    content = content.replace('bg-background/95', 'bg-glass')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # LIGHT THEME FIXES
    # Find --color-secondary-text in the light theme block and replace it
    content = re.sub(r'(--color-secondary-text:\s*)(#[A-Fa-f0-9]{6})(;)', r'\1#4B5563\3', content, count=1) 
    # Find --color-hover in the light theme block and replace it
    content = re.sub(r'(--color-hover:\s*)(#[A-Fa-f0-9]{6})(;)', r'\1#F9FAFB\3', content, count=1)
    
    # DARK THEME FIXES
    # The second occurrence of secondary-text and hover will be in the dark theme block
    content = re.sub(r'(--color-secondary-text:\s*)(#[A-Fa-f0-9]{6})(;)', r'\1#9CA3AF\3', content) # re.sub replaces all, so we can just do a precise replace by targeting the dark theme block
    
    # Let's just do it directly using a block replace
    # We will grab everything between :root, html[data-theme='light'] { and }
    def light_theme_replacer(match):
        block = match.group(0)
        block = re.sub(r'--color-secondary-text:\s*#[A-Fa-f0-9]+;', '--color-secondary-text: #4B5563;', block)
        block = re.sub(r'--color-hover:\s*#[A-Fa-f0-9]+;', '--color-hover: #F9FAFB;', block)
        return block

    content = re.sub(r":root,\s*html\[data-theme='light'\]\s*\{[^}]*\}", light_theme_replacer, content)
    
    def dark_theme_replacer(match):
        block = match.group(0)
        block = re.sub(r'--color-secondary-text:\s*#[A-Fa-f0-9]+;', '--color-secondary-text: #9CA3AF;', block)
        block = re.sub(r'--color-hover:\s*#[A-Fa-f0-9]+;', '--color-hover: #1F2937;', block)
        return block

    content = re.sub(r"html\[data-theme='dark'\]\s*\{[^}]*\}", dark_theme_replacer, content)

    # In case there are other inline text colors hardcoded to orange where they shouldn't be:
    # Actually, the user's issue is clearly about the background color of the card and the text color.
    # The card has g-hover, which was light green #F1F8F1 or dark green #1A261A.
    # And the text was orange #B45309 (from my earlier replacement) instead of dark gray.
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

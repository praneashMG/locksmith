import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add flex flex-col to the testimonial card container
    search_card = 'bg-white/5 backdrop-blur-sm border border-white/10 rounded-3xl p-8 hover:bg-white/10 transition-colors"'
    replace_card = 'bg-white/5 backdrop-blur-sm border border-white/10 rounded-3xl p-8 hover:bg-white/10 transition-colors flex flex-col"'
    content = content.replace(search_card, replace_card)
    
    # Add flex-grow to the paragraph
    search_p = 'class="text-gray-200 leading-relaxed mb-6 text-sm"'
    replace_p = 'class="text-gray-200 leading-relaxed mb-6 text-sm flex-grow"'
    content = content.replace(search_p, replace_p)
    
    # Add mt-auto to the profile block, it is currently "flex items-center gap-4"
    search_profile = 'class="flex items-center gap-4"'
    replace_profile = 'class="flex items-center gap-4 mt-auto"'
    content = content.replace(search_profile, replace_profile)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

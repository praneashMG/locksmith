with open('contact.html', 'r', encoding='utf-8') as file:
    content = file.read()

# The HTML block to replace
search_block = '''          <div class="h-64 md:h-full min-h-[260px] relative bg-[#0a0f1c]">
            <!-- Decorative map mockup -->
            <div class="absolute inset-0 opacity-30" style="background-image: radial-gradient(circle, #EAB308 1px, transparent 1px); background-size: 24px 24px;"></div>
            <div class="absolute inset-0 flex items-center justify-center">
              <div class="text-center">
                <div class="w-16 h-16 mx-auto rounded-full bg-custom-gradient flex items-center justify-center shadow-2xl border-4 border-white/20 animate-pulse">
                  <i class="fas fa-map-marker-alt text-white text-2xl"></i>
                </div>
                <p class="text-white font-bold text-sm mt-3">SecureLock HQ</p>
              </div>
            </div>
          </div>'''

replace_block = '''          <div class="h-64 md:h-full min-h-[260px] relative bg-[#0a0f1c] overflow-hidden">
            <!-- Google Maps Iframe -->
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.25279998634!2d-74.14448744169722!3d40.69766374868249!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2s!4v1711202888497!5m2!1sen!2s" class="absolute inset-0 w-full h-full" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>'''

content = content.replace(search_block, replace_block)

with open('contact.html', 'w', encoding='utf-8') as file:
    file.write(content)

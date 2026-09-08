import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# Replace the border-t class in the menu overlay
old_class = 'className="mt-4 pt-6 border-t border-black/5 dark:border-white/10 flex flex-col gap-6"'
new_class = 'className="mt-4 pt-2 flex flex-col gap-6"'

content = content.replace(old_class, new_class)

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


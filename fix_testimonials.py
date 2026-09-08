import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# 1. Remove the hover pause that makes it stuck
content = content.replace("""                .animate-marquee:hover {
                  animation-play-state: paused;
                }""", "")

# 2. Force text to be white
content = content.replace(
    'bg-gray-50 dark:bg-black/20',
    'bg-black/20'
)

content = content.replace(
    'text-black/80 dark:text-white/80 transition-colors duration-1000',
    'text-white/90'
)

content = content.replace(
    '<p className="font-medium transition-colors duration-1000">{t.name}</p>',
    '<p className="font-medium text-white">{t.name}</p>'
)

content = content.replace(
    '<p className="text-sm text-black/50 dark:text-white/50 transition-colors duration-1000">{t.company}</p>',
    '<p className="text-sm text-white/60">{t.company}</p>'
)


with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


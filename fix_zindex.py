import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# Upgrade z-50 to z-[100] in nav and overlay
content = content.replace('className="fixed top-0 left-0 right-0 z-50', 'className="fixed top-0 left-0 right-0 z-[100]')
content = content.replace('shadow-2xl z-50 flex', 'shadow-2xl z-[100] flex')
content = content.replace('z-[60]"', 'z-[110]"')

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


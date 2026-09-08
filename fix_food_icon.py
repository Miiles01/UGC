import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# Add FoodIcon import
if 'FoodIcon' not in content:
    content = content.replace("import { Menu, Instagram, Twitter, Mail, Play, X } from 'lucide-react';", 
                              "import { Menu, Instagram, Twitter, Mail, Play, X } from 'lucide-react';\nimport { FoodIcon } from '../Icons/FoodIcon';")

# Replace Play with FoodIcon in the mobile carousel
content = content.replace('<Play className="w-12 h-12 text-white/50 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" />', 
                          '<FoodIcon className="w-12 h-12 text-white/80 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" />')

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


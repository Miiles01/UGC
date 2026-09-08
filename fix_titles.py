import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# Register SplitText
content = content.replace(
    'gsap.registerPlugin(ScrollTrigger);',
    'gsap.registerPlugin(ScrollTrigger, SplitText);'
)

# Add the animation logic to the useEffect
title_logic = """
    // Title animations with SplitText on scroll
    const titles = gsap.utils.toArray('.animated-title');
    titles.forEach((title) => {
      const split = new SplitText(title, { type: 'words' });
      gsap.from(split.words, {
        scrollTrigger: {
          trigger: title,
          start: 'top 85%',
          once: true
        },
        opacity: 0,
        y: 25,
        stagger: 0.06,
        duration: 0.6,
        ease: 'power2.out'
      });
    });
"""

content = content.replace(
    '// Paragraph animations',
    title_logic + '\n    // Paragraph animations'
)

# Now, we need to remove Framer Motion from h1 and h2 and add animated-title class
# The pattern for the injected framer-motion props was:
# <motion.h1 ... initial={{ opacity: 0, y: 40 }} ... transition={{ ... }}>
# Since it's multi-line, we'll use a regex to clean it up.

def replacer(match):
    tag = match.group(1) # 'h1' or 'h2'
    attributes = match.group(2)
    
    # We want to remove the framer motion props: initial, whileInView, viewport, transition
    # Let's just remove them manually. They start at 'initial={{' and end at '}}' for each
    attrs_clean = re.sub(r'initial={{.*?}}\s*', '', attributes, flags=re.DOTALL)
    attrs_clean = re.sub(r'whileInView={{.*?}}\s*', '', attrs_clean, flags=re.DOTALL)
    attrs_clean = re.sub(r'viewport={{.*?}}\s*', '', attrs_clean, flags=re.DOTALL)
    attrs_clean = re.sub(r'transition={{.*?}}\s*', '', attrs_clean, flags=re.DOTALL)
    
    # Add animated-title class
    attrs_clean = attrs_clean.replace('className="', 'className="animated-title ')
    
    return f'<{tag}{attrs_clean}>'

# Find <motion.h1 ... > and <motion.h2 ... >
content = re.sub(r'<motion\.(h[12])([^>]+)>', replacer, content, flags=re.DOTALL)

# Replace closing tags
content = content.replace('</motion.h1>', '</h1>')
content = content.replace('</motion.h2>', '</h2>')

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


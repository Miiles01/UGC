import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# 1. Remove the GSAP useEffect block for mwg_effect027
gsap_pattern = re.compile(r'\s*// Rolling Letters Title GSAP Logic \(mwg_effect027\).*?\}\);\s*return \(\) => ctx\.revert\(\);\s*\}, \[\]\);', re.DOTALL)
content = gsap_pattern.sub('', content)

# 2. Replace the complex mwg_effect027 markup with a clean H1 that uses animated-title
markup_pattern = re.compile(r'<div className="mwg_effect027.*?</ul>\s*</div>', re.DOTALL)
new_markup = """<div className="flex flex-col items-center md:items-start mb-8 md:mb-16 w-full">
                <h1 className="animated-title text-5xl sm:text-6xl md:text-[90px] lg:text-[130px] font-semibold tracking-tighter leading-[0.85] text-black dark:text-white transition-colors duration-1000">
                  Soy Laura,<br />
                  creadora de<br />
                  historias
                </h1>
              </div>"""
content = markup_pattern.sub(new_markup, content)

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# Extract Navbar and Overlay
nav_pattern = re.compile(r'\s*\{\/\* Floating Navbar \*\/\}.*?<\/AnimatePresence>', re.DOTALL)
nav_match = nav_pattern.search(content)

if nav_match:
    nav_code = nav_match.group(0)
    # Remove it from the current location
    content = content.replace(nav_code, '')
    
    # Insert it at the end of the relative wrapper
    # The relative wrapper ends with:
    #           </footer>
    #         </main>
    #       </div>
    #     </div>
    #   </PortfolioSmoothScroll>
    
    insert_pattern = re.compile(r'(<\/main>\s*)', re.DOTALL)
    content = insert_pattern.sub(r'\1' + nav_code + '\n', content)

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


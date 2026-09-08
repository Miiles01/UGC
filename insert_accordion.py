import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# 1. Prepare CSS and HTML
new_section = """
            {/* About Me Accordion (Light) */}
            <section id="sobre-mi" className="theme-section flex flex-col gap-8 w-full" data-theme="light">
              <h2 className="animated-title text-3xl md:text-5xl font-light tracking-tight transition-colors duration-1000">
                Sobre <span className="font-semibold text-4xl md:text-6xl">mí</span>
              </h2>
              
              <style>{`
                .mwg_effect109 .container-slides {
                    height: 506px;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    width: 100%;
                    max-width: 100%;
                }
                .mwg_effect109 .slide {
                    position: relative;
                    flex: 0 0 88px;
                    height: 506px;
                    overflow: hidden;
                    background-color: #f3f4f6;
                }
                :global(.dark) .mwg_effect109 .slide {
                    background-color: #171717;
                }
                .mwg_effect109 .slide:not(.on) {
                    cursor: pointer;
                }
                .mwg_effect109 .content-slide {
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    padding: 2rem;
                    width: 100%;
                }
                .mwg_effect109 .small-title {
                    width: 506px;
                    position: absolute;
                    bottom: 0;
                    left: 100%;
                    transform: rotate(-90deg);
                    transform-origin: 0 100%;
                    padding-left: 2rem;
                    padding-bottom: 1.5rem;
                    display: flex;
                    align-items: center;
                }
              `}</style>
              
              <div className="mwg_effect109 w-full">
                <div className="container-slides">
                  {[
                    {
                      title: "Trayectoria",
                      smallTitle: "Trayectoria",
                      text: "Comencé mi carrera digital hace más de 4 años, enfocándome en el estilo de vida y la moda. He colaborado con marcas globales, construyendo una voz única y sólida.",
                      img: "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800&q=80"
                    },
                    {
                      title: "Marcas Top",
                      smallTitle: "Marcas",
                      text: "A lo largo de los años he trabajado con firmas como Chanel, Vogue, Adidas y L'Oréal, creando contenido visual y narrativas de alto impacto para sus campañas.",
                      img: "https://images.unsplash.com/photo-1529139574466-a303027c028c?w=800&q=80"
                    },
                    {
                      title: "Estética Visual",
                      smallTitle: "Estética",
                      text: "Mi enfoque se basa en el minimalismo y la autenticidad. Cada pieza está diseñada para transmitir elegancia pura, cuidando la luz y la composición fotográfica.",
                      img: "https://images.unsplash.com/photo-1445205170230-053b83016050?w=800&q=80"
                    },
                    {
                      title: "La Comunidad",
                      smallTitle: "Comunidad",
                      text: "Más allá de las marcas, conecto con personas reales. Fomento un espacio donde la moda es accesible y el estilo de vida se comparte desde una perspectiva humana.",
                      img: "https://images.unsplash.com/photo-1512413914564-9273641777b7?w=800&q=80"
                    }
                  ].map((s, i) => (
                    <div key={i} className={`slide rounded-2xl ${i === 0 ? 'on' : ''}`}>
                      <div className="content-slide">
                        <p className="text-3xl md:text-4xl font-light">{s.title}</p>
                        <div className="bottom-slide mt-auto">
                          <img className="w-full h-40 md:h-56 object-cover rounded-xl mb-6" src={s.img} alt={s.title} />
                          <p className="text-sm md:text-base text-black/70 dark:text-white/70">{s.text}</p>
                        </div>
                      </div>
                      <div className="small-title">
                        <p className="text-lg tracking-widest font-medium opacity-50 whitespace-nowrap">{s.smallTitle}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </section>
"""

# Replace the old section
pattern = re.compile(r'\{\/\* About Me \(Light\) \*\/\}.*?<\/section>', re.DOTALL)
content = pattern.sub(new_section.strip(), content)

# 2. Add the useEffect for the GSAP accordion logic
js_logic = """
  // Accordion GSAP Logic
  useEffect(() => {
    const root = document.querySelector('.mwg_effect109')
    if (!root) return
    const container = root.querySelector('.container-slides')
    const slides = [...container.querySelectorAll('.slide')]

    const contents = slides.map(item => item.querySelector('.content-slide'))
    const smallTitles = slides.map(item => item.querySelector('.small-title'))
    const bottoms = slides.map(item => item.querySelector('.bottom-slide'))

    // Responsive widths
    const containerWidth = container.clientWidth || window.innerWidth
    let widthClosed = window.innerWidth < 768 ? 60 : 88
    let widthOpen = containerWidth - (widthClosed * (slides.length - 1)) - (6 * (slides.length - 1))
    if (widthOpen > 736) widthOpen = 736
    
    let borderRadiusClosed = window.innerWidth < 768 ? 30 : 44
    let heightClosed = window.innerWidth < 768 ? 340 : 400
    let heightHover = window.innerWidth < 768 ? 360 : 420
    let slideHeight = window.innerWidth < 768 ? 420 : 506
    
    let smallTitleXOpen = window.innerWidth < 768 ? 40 : 60
    let contentXLeft = -720
    let contentXRight = 70
    let axis = 'x'

    let lastIndexEntered = 0
    slides[0].classList.add('on')

    gsap.set(slides[0], { flex: '0 0 ' + widthOpen + 'px', borderRadius: 20, height: slideHeight })
    gsap.set(slides.slice(1), { borderRadius: borderRadiusClosed, height: heightClosed })
    gsap.set(smallTitles[0], { [axis]: smallTitleXOpen })
    gsap.set(smallTitles.slice(1), { width: heightClosed })
    gsap.set(contents.slice(1), { [axis]: contentXLeft })
    gsap.set(bottoms.slice(1), { autoAlpha: 0 })

    function handleMouseEnter(item, index) {
        if (item.classList.contains('on')) return
        gsap.to(item, { height: heightHover, duration: 0.3, ease: 'back.out(2)' })
        gsap.to(smallTitles[index], { width: heightHover, duration: 0.3, ease: 'back.out(2)' })
    }

    function handleMouseLeave(item, index) {
        if (item.classList.contains('on')) return
        gsap.to(item, { height: heightClosed, duration: 0.3, ease: 'back.out(2)' })
        gsap.to(smallTitles[index], { width: heightClosed, duration: 0.3, ease: 'back.out(2)' })
    }

    function handleMouseClick(item, index) {
        const isBefore = index < lastIndexEntered

        if (index !== lastIndexEntered) {
            slides.forEach(slide => slide.classList.remove('on'))
            gsap.to(slides, {
                flex: '0 0 ' + widthClosed + 'px',
                height: heightClosed,
                borderRadius: borderRadiusClosed,
                duration: 0.5,
                ease: 'back.inOut(0.9)',
            })
            gsap.to(contents[lastIndexEntered], {
                [axis]: isBefore ? contentXLeft : contentXRight,
                duration: 0.5,
                ease: 'back.inOut(0.9)',
            })
            gsap.to(smallTitles, {
                [axis]: 0,
                width: heightClosed,
                duration: 0.5,
                ease: 'back.inOut(0.9)',
            })
            gsap.to(bottoms, {
                autoAlpha: 0,
                duration: 0.4,
                ease: 'power1.inOut',
            })

            item.classList.add('on')
            gsap.to(item, {
                flex: '0 0 ' + widthOpen + 'px',
                borderRadius: 20,
                height: slideHeight,
                duration: 0.5,
                ease: 'back.inOut(0.9)',
            })
            gsap.fromTo(contents[index], {
                [axis]: isBefore ? contentXRight : contentXLeft,
            }, {
                [axis]: 0,
                duration: 0.5,
                ease: 'back.inOut(0.9)',
            })
            gsap.to(smallTitles[index], {
                [axis]: isBefore ? -704 : smallTitleXOpen,
                width: slideHeight,
                duration: 0.5,
                ease: 'back.inOut(0.9)',
            })
            gsap.to(bottoms[index], {
                autoAlpha: 1,
                duration: 0.4,
                ease: 'power1.inOut',
            })
        }
        lastIndexEntered = index
    }

    const enterListeners = []
    const leaveListeners = []
    const clickListeners = []

    slides.forEach((item, index) => {
        const enter = () => handleMouseEnter(item, index)
        const leave = () => handleMouseLeave(item, index)
        const click = () => handleMouseClick(item, index)
        item.addEventListener('mouseenter', enter)
        item.addEventListener('mouseleave', leave)
        item.addEventListener('click', click)
        enterListeners.push(enter)
        leaveListeners.push(leave)
        clickListeners.push(click)
    })

    return () => {
        slides.forEach((item, index) => {
            item.removeEventListener('mouseenter', enterListeners[index])
            item.removeEventListener('mouseleave', leaveListeners[index])
            item.removeEventListener('click', clickListeners[index])
        })
    }
  }, []);
"""

content = content.replace('  useEffect(() => {', js_logic + '\n  useEffect(() => {')

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


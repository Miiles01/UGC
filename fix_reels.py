import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# 1. Prepare HTML and CSS for the new Reels section
new_reels_section = """
            {/* Reels / Video Content GSAP (Dark) */}
            <section id="contenidos" className="theme-section w-full mb-12 md:mb-0" data-theme="dark">
              
              <style>{`
                  .no-scrollbar::-webkit-scrollbar {
                      display: none;
                  }
                  .no-scrollbar {
                      -ms-overflow-style: none;
                      scrollbar-width: none;
                  }
                  .mwg_effect007 .pin-height {
                      height: 400vh;
                      width: 100%;
                  }
                  .mwg_effect007 .container-pin {
                      position: relative;
                      height: 100vh;
                      width: 100vw;
                      left: 50%;
                      right: 50%;
                      margin-left: -50vw;
                      margin-right: -50vw;
                      overflow: hidden;
                  }
                  .mwg_effect007 .circle {
                      width: 300%;
                      aspect-ratio: 1;
                      position: absolute;
                      top: 50%;
                      left: -100%;
                      pointer-events: none;
                  }
                  .mwg_effect007 .media {
                      width: 25vw;
                      max-width: 400px;
                      aspect-ratio: 0.5625;
                      border-radius: 1.5rem;
                      object-fit: cover;
                      position: absolute;
                      top: 0;
                      left: 50%;
                      transform: translate(-50%, -50%);
                      pointer-events: auto;
                  }
              `}</style>
              
              {/* Reels GSAP (Desktop) */}
              <div className="hidden md:block w-full mwg_effect007 relative">
                  <div className="pin-height">
                      <div className="container-pin">
                          <h2 className="animated-title text-3xl md:text-6xl lg:text-7xl font-light tracking-tight absolute top-12 md:top-24 left-0 w-full text-center z-10 transition-colors duration-1000">
                              Contenido en <span className="font-semibold text-4xl md:text-7xl lg:text-8xl">movimiento</span>
                          </h2>
                          {[
                            "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600&q=80",
                            "https://images.unsplash.com/photo-1529139574466-a303027c028c?w=600&q=80",
                            "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=600&q=80",
                            "https://images.unsplash.com/photo-1509319117193-57bab727e09d?w=600&q=80",
                            "https://images.unsplash.com/photo-1534126511673-b6899657816a?w=600&q=80",
                            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=600&q=80"
                          ].map((src, i) => (
                              <div key={i} className="circle">
                                  <img className="media" src={src} alt={`Reel ${i + 1}`} />
                              </div>
                          ))}
                      </div>
                  </div>
              </div>

              {/* Reels Carousel (Mobile) */}
              <div className="block md:hidden w-full flex flex-col gap-8 pt-12">
                  <h2 className="animated-title text-4xl font-light tracking-tight text-center transition-colors duration-1000">
                      Contenido en <span className="font-semibold text-5xl">movimiento</span>
                  </h2>
                  <div className="flex gap-4 overflow-x-auto snap-x snap-mandatory pb-8 w-screen -mx-6 px-6 no-scrollbar">
                      {[
                        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600&q=80",
                        "https://images.unsplash.com/photo-1529139574466-a303027c028c?w=600&q=80",
                        "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=600&q=80",
                        "https://images.unsplash.com/photo-1509319117193-57bab727e09d?w=600&q=80",
                        "https://images.unsplash.com/photo-1534126511673-b6899657816a?w=600&q=80",
                        "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=600&q=80"
                      ].map((src, i) => (
                          <div key={i} className="snap-center shrink-0 w-[75vw] aspect-[9/16] relative rounded-2xl overflow-hidden bg-neutral-900 transition-colors duration-1000">
                              <img className="w-full h-full object-cover opacity-80" src={src} alt={`Reel ${i + 1}`} />
                              <Play className="w-12 h-12 text-white/50 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" />
                          </div>
                      ))}
                  </div>
              </div>
            </section>
"""

# Replace the old Reels section
pattern = re.compile(r'\{\/\* Reels \/ Video Content \(Dark\) \*\/\}.*?<\/section>', re.DOTALL)
content = pattern.sub(new_reels_section.strip(), content)

# 2. Add the JS logic
js_logic = """
  // Rotating Circle Gallery GSAP Logic (mwg_effect007)
  useEffect(() => {
    let ctx = gsap.context(() => {
      if (window.innerWidth >= 768) {
        const pinHeight = document.querySelector('.mwg_effect007 .pin-height');
        const container = document.querySelector('.mwg_effect007 .container-pin');
        const circles = document.querySelectorAll('.mwg_effect007 .circle');
        
        if (pinHeight && container && circles.length) {
          ScrollTrigger.create({
            trigger: pinHeight,
            start: 'top top',
            end: 'bottom bottom',
            pin: container
          });

          gsap.fromTo(circles, {
            rotation: 30
          }, {
            rotation: -30,
            ease: 'power2.inOut',
            stagger: 0.06,
            scrollTrigger: {
              trigger: pinHeight,
              start: 'top top',
              end: 'bottom bottom',
              scrub: true
            }
          });
        }
      }
    });
    return () => ctx.revert();
  }, []);
"""

content = content.replace('  // Pinned Mask Gallery GSAP Logic', js_logic + '\n  // Pinned Mask Gallery GSAP Logic')

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


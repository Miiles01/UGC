import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# 1. Prepare HTML and CSS
new_gallery = """
            {/* Portfolio Gallery GSAP (Light) */}
            <section className="theme-section mwg_effect037 w-full -mx-6 md:-mx-12 lg:-mx-24 px-6 md:px-12 lg:px-24" data-theme="light">
              <style>{`
                  .mwg_effect037 .pin-height {
                      height: 500vh;
                      width: 100%;
                  }
                  .mwg_effect037 .container-pin {
                      width: 100%;
                      height: 100vh;
                      display: grid;
                      grid-template-columns: 1fr auto 1fr;
                      align-items: center;
                      padding: 0;
                  }
                  .mwg_effect037 .container-pin > *:nth-child(1) { justify-self: start; }
                  .mwg_effect037 .container-pin > *:nth-child(2) { justify-self: center; }
                  .mwg_effect037 .container-pin > *:nth-child(3) { justify-self: end; }
                  
                  .mwg_effect037 .text-side {
                      font-weight: 300;
                      font-size: clamp(1.5rem, 4vw, 4rem);
                      letter-spacing: -0.05em;
                  }
                  
                  .mwg_effect037 .images-stack {
                      width: 70vw;
                      max-width: 320px;
                      aspect-ratio: 0.75;
                      position: relative;
                  }
                  
                  @media (min-width: 768px) {
                      .mwg_effect037 .images-stack {
                          width: 30vw;
                          max-width: 500px;
                      }
                  }
                  
                  .mwg_effect037 .hidden-mask {
                      width: 100%;
                      height: 100%;
                      position: absolute;
                      top: 0;
                      left: 0;
                      overflow: hidden;
                      border-radius: 1.5rem;
                      -webkit-mask-image: linear-gradient(transparent 100%, #000 125%, #000 225%);
                      mask-image: linear-gradient(transparent 100%, #000 125%, #000 225%);
                  }
                  
                  .mwg_effect037 .media-img {
                      width: 100%;
                      height: calc(100% + 60px);
                      object-fit: cover;
                      will-change: transform;
                  }
              `}</style>
              
              <div className="pin-height">
                  <div className="container-pin">
                      <p className="text-side animated-title">Dirección<br/><span className="font-semibold">Creativa</span></p>
                      <div className="images-stack">
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800&q=80" alt="Galeria 1" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800&q=80" alt="Galeria 2" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=800&q=80" alt="Galeria 3" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1509319117193-57bab727e09d?w=800&q=80" alt="Galeria 4" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1534126511673-b6899657816a?w=800&q=80" alt="Galeria 5" /></div>
                      </div>
                      <p className="text-side animated-title text-right">Colección<br/><span className="font-semibold">24-25</span></p>
                  </div>
              </div>
            </section>
"""

# Replace the old section
pattern = re.compile(r'\{\/\* Portfolio Gallery \(Light\) \*\/\}.*?<\/section>', re.DOTALL)
content = pattern.sub(new_gallery.strip(), content)


# 2. Add the JS logic
js_logic = """
  // Pinned Mask Gallery GSAP Logic
  useEffect(() => {
    const pinHeight = document.querySelector('.mwg_effect037 .pin-height');
    if (!pinHeight) return;
    
    const container = document.querySelector('.mwg_effect037 .container-pin');
    const medias = document.querySelectorAll('.mwg_effect037 .hidden-mask');
    const mediasChild = document.querySelectorAll('.mwg_effect037 .media-img');

    const distancePerImage = (pinHeight.clientHeight - window.innerHeight) / medias.length;

    let ctx = gsap.context(() => {
        ScrollTrigger.create({
            trigger: pinHeight,
            start: 'top top',
            end: 'bottom bottom',
            pin: container
        });

        gsap.to(medias, {
            maskImage: 'linear-gradient(transparent -25%, #000 0%, #000 100%)',
            webkitMaskImage: 'linear-gradient(transparent -25%, #000 0%, #000 100%)',
            stagger: 0.5,
            ease: 'power3.inOut',
            scrollTrigger: {
                trigger: pinHeight,
                start: 'top top',
                end: 'bottom bottom',
                scrub: true
            }
        });
        
        gsap.to(mediasChild, {
            y: -30,
            stagger: 0.5,
            ease: 'power3.inOut',
            scrollTrigger: {
                trigger: pinHeight,
                start: 'top top',
                end: 'bottom bottom',
                scrub: true
            }
        });
        
        gsap.to(mediasChild, {
            y: -60,
            stagger: 0.5,
            immediateRender: false,
            ease: 'power3.inOut',
            scrollTrigger: {
                trigger: pinHeight,
                start: 'top top-=' + distancePerImage,
                end: 'bottom bottom-=' + distancePerImage,
                scrub: true
            }
        });
    });

    return () => ctx.revert();
  }, []);
"""

content = content.replace('  // Accordion GSAP Logic', js_logic + '\n  // Accordion GSAP Logic')

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


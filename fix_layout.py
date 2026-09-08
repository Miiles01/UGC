import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

new_gallery_html = """
            {/* Portfolio Gallery GSAP (Light) */}
            <section className="theme-section mwg_effect037 w-full -mx-6 md:-mx-12 lg:-mx-24 px-6 md:px-12 lg:px-24 relative" data-theme="light">
              <style>{`
                  .mwg_effect037 .pin-height {
                      height: 500vh;
                      width: 100%;
                  }
                  .mwg_effect037 .container-pin {
                      width: 100%;
                      height: 100vh;
                      display: flex;
                      justify-content: space-between;
                      align-items: center;
                      position: relative;
                  }
                  
                  .mwg_effect037 .text-side {
                      font-weight: 300;
                      font-size: clamp(2rem, 4vw, 4rem);
                      letter-spacing: -0.05em;
                      line-height: 1.1;
                      z-index: 10;
                      position: relative;
                  }
                  
                  .mwg_effect037 .images-stack {
                      width: 80vw;
                      max-width: 320px;
                      aspect-ratio: 0.75;
                      position: absolute;
                      left: 50%;
                      top: 50%;
                      transform: translate(-50%, -50%);
                      z-index: 1;
                  }
                  
                  @media (min-width: 768px) {
                      .mwg_effect037 .images-stack {
                          width: 35vw;
                          max-width: 480px;
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
                      <p className="text-side text-left">Dirección<br/><span className="font-semibold">Creativa</span></p>
                      
                      <div className="images-stack">
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800&q=80" alt="Galeria 1" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800&q=80" alt="Galeria 2" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=800&q=80" alt="Galeria 3" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1509319117193-57bab727e09d?w=800&q=80" alt="Galeria 4" /></div>
                          <div className="hidden-mask"><img className="media-img" src="https://images.unsplash.com/photo-1534126511673-b6899657816a?w=800&q=80" alt="Galeria 5" /></div>
                      </div>
                      
                      <p className="text-side text-right">Colección<br/><span className="font-semibold">24-25</span></p>
                  </div>
              </div>
            </section>
"""

# We need to replace the old section
pattern = re.compile(r'\{\/\* Portfolio Gallery GSAP \(Light\) \*\/\}.*?<\/section>', re.DOTALL)
content = pattern.sub(new_gallery_html.strip(), content)

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


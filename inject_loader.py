import re

with open('src/components/Plantillas/Plantilla01.tsx', 'r') as f:
    content = f.read()

# 1. Inject the loader DOM element at the top of the return
loader_dom = """
      {/* Intro Curtain Loader */}
      <div className="intro-curtain fixed inset-0 z-[10000] bg-white flex items-center justify-center">
        <div className="overflow-hidden">
          <p className="intro-text text-sm tracking-[0.3em] font-medium text-black uppercase transform translate-y-full">Portfolio</p>
        </div>
      </div>
"""
content = content.replace("<PortfolioSmoothScroll>", f"<PortfolioSmoothScroll>{loader_dom}")


# 2. Refactor the title animation into a function and add the intro timeline
old_title_logic = """    // Title animations with SplitText on scroll
    const titles = gsap.utils.toArray('.animated-title');
    titles.forEach((title) => {
      // Split into lines to create the mask wrappers, and chars for the animation
      const split = new SplitType(title as HTMLElement, { types: 'lines, chars' });
      
      // The user's requested clipPath technique applied to each line so it works with multiline text
      gsap.set(split.lines, { clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0% 100%)' });
      gsap.set(split.chars, { yPercent: 100 });

      gsap.to(split.chars, {
        scrollTrigger: {
          trigger: title,
          start: 'top 85%',
          once: true
        },
        yPercent: 0,
        duration: 0.8,
        ease: 'power2.out',
        stagger: { 
          each: 0.05, 
          from: "random" 
        },
        onComplete: () => {
          gsap.set(split.lines, { clearProps: 'clipPath' });
        }
      });
    });"""

new_title_logic = """    // Prevent scrolling while loading
    document.body.style.overflow = 'hidden';

    function initTitleAnimations() {
      const titles = gsap.utils.toArray('.animated-title');
      titles.forEach((title) => {
        const split = new SplitType(title as HTMLElement, { types: 'lines, chars' });
        gsap.set(split.lines, { clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0% 100%)' });
        gsap.set(split.chars, { yPercent: 100 });

        gsap.to(split.chars, {
          scrollTrigger: {
            trigger: title,
            start: 'top 85%',
            once: true
          },
          yPercent: 0,
          duration: 0.8,
          ease: 'power2.out',
          stagger: { 
            each: 0.05, 
            from: "random" 
          },
          onComplete: () => {
            gsap.set(split.lines, { clearProps: 'clipPath' });
          }
        });
      });
      // Trigger ScrollTrigger refresh in case positions changed
      ScrollTrigger.refresh();
    }

    const introTl = gsap.timeline();
    
    introTl.to('.intro-text', {
      y: 0,
      duration: 1,
      ease: 'power3.out',
      delay: 0.3
    })
    .to('.intro-text', {
      y: '-100%',
      duration: 0.8,
      ease: 'power3.in',
      delay: 0.6
    })
    .to('.intro-curtain', {
      yPercent: -100,
      duration: 1.2,
      ease: 'power4.inOut',
      onComplete: () => {
        document.body.style.overflow = '';
        initTitleAnimations();
      }
    }, "-=0.4");"""

content = content.replace(old_title_logic, new_title_logic)

with open('src/components/Plantillas/Plantilla01.tsx', 'w') as f:
    f.write(content)


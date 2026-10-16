"""Build index.html from the template.

    python3 build.py                              # relative links (works anywhere)
    SITE_URL=https://example.com/ python3 build.py  # absolute share-card links once you have a domain
"""
import os
t=open('tpl.html').read(); d=open('data.json').read()
L=open('layouts.json').read() if os.path.exists('layouts.json') else '{}'
site=os.environ.get('SITE_URL','').strip()
if site and not site.endswith('/'): site+='/'
canon=f'<link rel="canonical" href="{site}">\n<meta property="og:url" content="{site}">\n' if site else ''
out=t.replace('__DATA__',d).replace('__LAYOUTS__',L).replace('__SITE__',site).replace('__CANONICAL__',canon)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','index.html') if os.path.basename(os.path.dirname(os.path.abspath(__file__)))=='src' else 'courses-i-love.html','w').write(out)
print('built',len(out),'bytes', 'for '+site if site else '(relative links)')

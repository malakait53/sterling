import glob
parts=sorted(glob.glob('/tmp/sterling/src/*'))
out=''
for p in parts:
    out+=open(p).read()
    if not out.endswith('\n'):out+='\n'
open('/tmp/sterling/www/index.html','w').write(out)
import re
js=re.search(r'<script>(.*)</script>',out,re.S).group(1)
open('/tmp/sterling_check.js','w').write(js)
print(len(out))

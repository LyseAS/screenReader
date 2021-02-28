import re
string = open('69.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', '', string)
open('69c.txt', 'w').write(new_str)
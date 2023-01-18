import os

if not os.path.exists('output/CNAME'):
    with open("output/CNAME", 'w') as outfile:
        outfile.write("steadytrekker.com")
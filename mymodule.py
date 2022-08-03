import requests
import json,sys;
from PIL import Image;
print(sys.path);
def convert_png():
    im = Image.open("img.jpg");
    basewidth = 300
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    # im.show(); 
    im.save("img1.png","PNG");
def get_image():
    r = requests.get("https://api.catboys.com/img");# GET info from site
    j = json.loads(r.content);# Convert site text to json
    r = requests.get(j['url']);# get url from json
    out = open(".\img.jpg", "wb");# open file to save as img.png
    out.write(r.content);# save this image to pc
    out.close();
    convert_png();
    
    
    

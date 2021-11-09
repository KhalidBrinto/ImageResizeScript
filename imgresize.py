from PIL import Image
import sys, os

def resize_img(path, outpath):
    count =0 
    for item in os.listdir(path):
        print(item)
        if os.path.isfile(os.path.join(path,item)):
            f, e = os.path.splitext(item)
            output = os.path.join(outpath, f + '_resized.jpg')
            im = Image.open(os.path.join(path,item))
            imResize = im.resize((500,500), Image.ANTIALIAS)
            imResize.save(output, 'JPEG', quality=100)
        count = count + 1
    print("\nTotal files: ", count)

        
if __name__ == "__main__":
    path = str(sys.argv[1])
    outpath = str(sys.argv[2])
    try:
        resize_img(path,outpath)
        print("Successfully resized all images.")
    except:
        print("Error occured.")
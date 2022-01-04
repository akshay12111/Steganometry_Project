from src.utilSteg import is_encodable,pair,get_pixel_MSB,Image
from src.util_Isteg import *

#2pixels for flag -> In first two pixel all rgb component will be even
#next 6pixel for image dimensions 3+3 width and height -> 2* 2,2,2  2,2,2  1,1,1
#next 5 pixel for num of pixels in secret image -> 2,2,2  2,2,2  2,2,2  2,2,2  1,1,1
HEADER_SIZE     = 13 #pixels
FLAG_SIZE       = 2 #pixels
WIDTH_SIZE      = 3 #pixels
HEIGHT_SIZE     = 3 #pixels
SECRET_IMG_SIZE = 5 #pixels

def encodeImgData(original_image_pixels,secret_image_pixels,secret_image_size):
    num_payload_pixels  = len(secret_image_pixels)
    original_pixel_data,offset = add_header(original_image_pixels,secret_image_size,num_payload_pixels)

    for pixel in secret_image_pixels:
        first2_msb,next2_msb = pixel_MSB(pixel)
        original_image_pixels[offset] = encode_data(original_image_pixels[offset],first2_msb)
        offset += 1
        original_image_pixels[offset] = encode_data(original_image_pixels[offset],next2_msb)
        offset += 1
    
    return original_image_pixels

def decodeImgData(source_img):
    recreated_secret_pixels = []
    if(check_FLAG(source_img)):
        offset=2
        dimension,offset = get_dimensions(source_img,WIDTH_SIZE,HEIGHT_SIZE,offset)
        secret_img_size,offset = get_size(source_img,offset)
        EOF = offset + (2*secret_img_size)
        
        for pix1,pix2 in pair(source_img[offset:EOF]):
            secret_pixel_data = get_pixel_MSB(bin(pix1),bin(pix2)).ljust(8,'0')
            recreated_secret_pixels.append(secret_pixel_data)
            
        return tuple(recreated_secret_pixels)        
    else:
        return -1
    
    
def HideData(orig_img_path='media/sierra.jpg',second_img_path='media/mac.jpg'):
    try:
        original_image_pixels = Image.open(orig_img_path)
    except:
        print(f"Unable to open image {orig_img_path}")
        exit(0)
    else:
        original_pixel_data = list(original_image_pixels.getdata())
        
    try:
        secret_image = Image.open(second_img_path)
    except:
        print(f"Unable to open image {second_img_path}")
        exit(0)
    else:
        secret_pixel_data = list(secret_image.getdata())
            
    if is_encodable(original_pixel_data,secret_pixel_data,HEADER_SIZE):
        encoded_msg_bytes = encodeImgData(original_pixel_data,secret_pixel_data,secret_image.size)
        
        new_img = Image.new(original_image_pixels.mode,original_image_pixels.size)
        new_img.putdata(tuple(encoded_msg_bytes))
        new_img.save('test.png')
        print("[+] Successfully encoded in image")
        pass

    else:
        print("[-] Process Unsuccessful")
        return
    pass

def ExtractData(source_path='media/test.png',destination_path='extract.png'):
    try:
        source_img = Image.open(source_path)
    except:
        print("Error:File Not Found")
        exit(0)
    
    img_data,dimensions = decodeImgData(source_img)
    
    try:
        dest_img = Image.new("RGB",dimensions)
        dest_img.putdata(img_data)
    except:
        print("")
        

    pass

if __name__ == '__main__':
    HideData()
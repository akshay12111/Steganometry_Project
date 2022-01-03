from src.utilSteg import is_encodable,pair,add_header,Image
from src.util_Isteg import *

#2pixels for flag -> In first two pixel all rgb component will be even
#next 6pixel for image dimensions 3+3 width and height -> 2* 2,2,2  2,2,2  1,1,1
#next 5 pixel for num of pixels in secret image -> 2,2,2  2,2,2  2,2,2  2,2,2  1,1,1
HEADER_SIZE = 13 #pixels

def HideData(orig_img_path='media/sierra.jpg',second_img_path='media/mac.jpg'):
    try:
        original_image = Image.open(orig_img_path)
    except:
        print(f"Unable to open image {orig_img_path}")
        exit(0)
    else:
        original_pixel_data = list(original_image.getdata())
        
    
    try:
        secret_image = Image.open(second_img_path)
        pass
    except:
        print(f"Unable to open image {second_img_path}")
        exit(0)
    else:
        secret_pixel_data = list(secret_image.getdata())
        num_payload_pixels = len(secret_pixel_data)
        
    # msg_bytes = msg_to_binary(message)
    
    if is_encodable(original_pixel_data,secret_pixel_data,HEADER_SIZE):
        # original_pixel_data = add_header(original_pixel_data,secret_pixel_data.size,num_payload_pixels)
        # encoded_msg_bytes = encode_message(original_pixel_data, msg_bytes)
        
        # new_img = Image.new(original_image.mode,original_image.size)
        # new_img.putdata(tuple(encoded_msg_bytes))
        # new_img.save('media/test.png')
        # print("[+] Successfully encoded in image")
        pass

    else:
        print("[-] Process Unsuccessful")
        return
    pass

if __name__ == '__main__':
    HideData()
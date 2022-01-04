from PIL import Image
FLAG = 8*'0'

def msg_to_binary(msg):
    msg_list = [bin(ord(ch))[2:].rjust(8,'0') for ch in msg]
    return msg_list

def is_encodable(original_img_pixels,data,num_header_pixels=0):
    num_original_pixel = len(original_img_pixels)
    
    num_required_pixel = 2*len(data) + num_header_pixels
    return (num_original_pixel >= num_required_pixel)

def pair(iterable):
    i = iter(iterable)
    return zip(i,i)

def split_byte(byte_value):
    return [byte_value[0:4],byte_value[4:8]]

def get_pixel_MSB(pix1,pix2):
    pixel_data = []
    
    for component1,component2 in zip(pix1,pix2):
        img_component_val = bin(component1)[2:].rjust(8,'0')[-2:] + bin(component2)[2:].rjust(8,'0')[-2:]
        img_component_val = img_component_val.ljust(8,'0')
        pixel_data.append(int(img_component_val,2))
    
    return tuple(pixel_data)

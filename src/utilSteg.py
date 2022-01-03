from PIL import Image
FLAG = '00000000'

def msg_to_binary(msg):
    msg_list = [bin(ord(ch))[2:].rjust(8,'0') for ch in msg]
    return msg_list

def is_encodable(original_img_pixels,data,header_size=0):
    num_original_pixel = len(original_img_pixels)
    num_required_pixel = 2*len(data)
    return (num_original_pixel >= (num_required_pixel + header_size))

def pair(iterable):
    i = iter(iterable)
    return zip(i,i)

def split_byte(byte_value):
    return [byte_value[0:4],byte_value[4:8]]

def add_header(original_img_pixels,num_payload_pixels):
    for i in range(2):
        pixel_data = []
        for component in original_img_pixels[i]:
            if component%2 == 0:
                pixel_data.append(component)
            else:
                pixel_data.append(component+1)
        original_img_pixels[i] = pixel_data
    size_payload = bin(num_payload_pixels)
    pass
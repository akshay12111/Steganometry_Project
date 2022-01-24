from PIL import Image

def msg_to_binary(msg: str) -> list:
    '''
    This function converts a string to list of
    binary string of each character in the string
    ----------
    msg: string message (required)
    return: list
    '''
    msg_list = [bin(ord(ch))[2:].rjust(8,'0') for ch in msg]
    return msg_list

def is_encodable(original_img_pixels: list, data: list, num_header_pixels: int = 0) -> bool:
    '''
    This function checks if the given image
    data can be used to hide text or not
    ----------
    original_img_pixels: list of pixels(tuple) where each pixel has r,g,b (int) value (0<=value<=255)
    data: list of binary strings of given data (message)
    num_header_pixels: number of pixels used for header (optional)
    ----------
    return: if the number of pixels present is greater than the number of required pixels
    '''
    num_original_pixel = len(original_img_pixels)
    
    num_required_pixel = 2*len(data) + num_header_pixels
    return (num_original_pixel >= num_required_pixel)

def pair(iterable) -> tuple:
    '''
    iterable: Iterable
    return: tuple
    '''
    i = iter(iterable)
    return zip(i,i)

def split_byte(byte_value: str) -> list:
    '''
    This function splits given binary string in half and returns them as list
    --------
    byte_value: binary string for one byte data
    return: list
    '''
    return [byte_value[0:4],byte_value[4:8]]

def get_pixel_MSB(pix1: tuple, pix2: tuple) -> tuple:
    '''
    This function takes two pixels and extract data from
    their LSB 2 to form 4 MSB of a new pixel.
    It takes LSB 2 from pix1 + LSB 2 from pix2 r,g,b and creates
    MSB 4 + '0000' for new pixel r,g,b and then convert the
    new pixel to r,g,b (int)
    --------
    pix1: first  pixel data (tuple)
    pix2: second pixel data (tuple)
    return: new pixel (tuple)
    '''
    pixel_data = []
    
    for component1,component2 in zip(pix1,pix2):
        '''This iterates over both pixels at the same time, if pixels are (1,2,3) (4,5,6)
        so it will iterate like: (1,2) (3,4) (5,6)'''
        img_component_val = bin(component1)[2:].rjust(8,'0')[-2:] + bin(component2)[2:].rjust(8,'0')[-2:]
        img_component_val = img_component_val.ljust(8,'0')
        pixel_data.append(int(img_component_val,2)) #type casting byte string to int
    
    return tuple(pixel_data)

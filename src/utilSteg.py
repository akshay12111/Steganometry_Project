from PIL import Image
FLAG = '00000000'

def msg_to_binary(msg):
    msg_list = [bin(ord(ch))[2:].rjust(8,'0') for ch in msg]
    return msg_list

def is_encodable(pixels,data):
    num_pixel = len(pixels)
    num_bytes = len(data)
    return (num_pixel >= (2*num_bytes))

def pair(iterable):
    i = iter(iterable)
    return zip(i,i)

def split_byte(byte_value):
    return [byte_value[0:4],byte_value[4:8]]

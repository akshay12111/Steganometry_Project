from src.utilSteg import *

def pixel_to_bin(pixel):
    r,g,b = pixel 
    mask1 = (1 << 1) - 1
    mask2 = (1 << 2) - 1
    
    half_byte = ''
    half_byte += ("{0:b}".format(mask2 & r).rjust(2,'0'))
    half_byte += (str(mask1 & g))
    half_byte += (str(mask1 & b))
    return half_byte

def encode_to_pixel(pixel,half_byte):
    r,g,b = pixel
    r = r>>2
    r = r<<2
    r += int(half_byte[0:2],2)
    
    g = g>>1
    g = g<<1
    g += int(half_byte[2])
    
    b = b>>1
    b = b<<1
    b += int(half_byte[3])
    
    return (r,g,b)

def encode_message(original_pixels,byte_stream):
    for index,byte in enumerate(byte_stream):
        idx = index*2
        data1,data2 = split_byte(byte)
        byte_list = [encode_to_pixel(original_pixels[idx],data1),
                     encode_to_pixel(original_pixels[idx+1],data2)]
        
        original_pixels[(idx):(idx+2)] = byte_list
    
    return original_pixels

def decode_message(pixels):
    if ( pixel_to_bin(pixels[0]) + pixel_to_bin(pixels[1]) ) != FLAG:
        return -1
    data = ""
    for pix1,pix2 in pair(pixels[2:]):
        byte = pixel_to_bin(pix1) + pixel_to_bin(pix2)
        if(byte == FLAG):
            break
        
        data += chr(int(byte,2))
    return data

def HideData(image_path='sierra.jpg',message=""):
    original_image = Image.open(image_path)
    original_pixel_data = list(original_image.getdata())
    msg_bytes = [FLAG] + msg_to_binary(message) + [FLAG]
    
    if is_encodable(original_pixel_data,msg_bytes):    
        encoded_msg_bytes = encode_message(original_pixel_data, msg_bytes)
        
        new_img = Image.new(original_image.mode,original_image.size)
        new_img.putdata(tuple(encoded_msg_bytes))
        new_img.save('media/test.png')
        print("[+] Data successfully encoded in image")

    else:
        print("[-] Can not hide data in this image")
        return
    pass

def ExtractData(image_path='media/test.png'):
    image = Image.open(image_path)
    image_pixel_data = list(image.getdata())
    message = decode_message(image_pixel_data)

    if message == -1:
        print("[-] No FLAG byte found!\n\tThis image does not contain any message")
    else:
        print('[+] Data successfully decoded from image')
    return message

def ExtractDataTo(image_path='meida/test.png',file_path='message.txt'):
    message = ExtractData(image_path)
    if message != -1:
        with open(file_path,'w') as file:
            file.write(message)
        print(f"[+] Data successfully exported to {file_path}")
        return 1
    else:
        return 0


if __name__ == '__main__':
    #to encode
    HideData()

    #to decode
    ExtractData()

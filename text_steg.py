from PIL import Image
FLAG = '00000000'

def get_binary_message(msg):
    msg_list = [ bin(ord(ch))[2:].rjust(8,'0') for ch in msg]
    return msg_list

def encode_data(pixel,half_byte):
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
    pass

def put_data(original_pixels,data_stream):
    counter = 0
    for data in data_stream:
        p1 = data[0:4]
        p2 = data[4:8]
        # print("p1  ",p1)
        # print("p2  ",p2)
        # print("orig ",original_pixels[counter])
        original_pixels[counter] = encode_data(original_pixels[counter],p1)
        # print("mod ",original_pixels[counter])
        counter += 1
        # print("orig ",original_pixels[counter])
        original_pixels[counter] = encode_data(original_pixels[counter],p2)
        # print("mod ",original_pixels[counter])
        counter += 1
    
    # for i in range(20):
        # print(original_pixels[i])
    # print("--------END OF MOD---------")
    return original_pixels
    # list_iter = iter(original_pixels)
    # pixel_pair = zip(list_iter,list_iter)
    
    # remaining_bytes = len(data_stream)
    # counter = 0
    # for pixel1,pixel2 in pixel_pair:
    #     if(remaining_bytes == 0):
    #         break
    #     original_pixels[counter] = 
    pass

def get_data(pixels):
    # for i in range(20):
        # print(pixels[i])
    # print("--------END OF NEW---------")
    buffer1 = []
    buffer2 = []
    counter = 0
    flag_counter = 0
    mask1 = (1 << 1) - 1
    mask2 = (1 << 2) - 1
    for pixel in pixels:
        if(counter%2==0):
            s = ''.join(buffer1+buffer2)
            if(s == '00000000'):
                if(flag_counter == 1):
                    break
                flag_counter += 1
            if(s != ''):
                t = chr(int(s,2))
                print(t,end="")
            buffer1 = []
            buffer2 = []
            r,g,b = pixel
            buffer1.append("{0:b}".format(mask2 & r).rjust(2,'0'))
            buffer1.append(str(mask1 & g))
            buffer1.append(str(mask1 & b))
        else:
            r,g,b = pixel
            buffer2.append("{0:b}".format(mask2 & r).rjust(2,'0'))
            buffer2.append(str(mask1 & g))
            buffer2.append(str(mask1 & b))
        counter+=1
        # if(counter == 50):
        #     break


def main():
    original_image = Image.open("catalina.jpg")
    original_pixel_data = list(original_image.getdata())
    # for i in range(20):
        # print(original_pixel_data[i])
    # print("--------END OF ORIGINAL---------")
        
    message = 'Hello there this is my secret message'
    raw_msg_list = [FLAG] + get_binary_message(message) + [FLAG]
    # print(raw_msg_list)
    
    result = put_data(original_pixel_data, raw_msg_list)
    new_img = Image.new(original_image.mode,original_image.size)
    new_img.putdata(tuple(result))
    new_img.save('test.png')
    pass

def main2():
    image = Image.open('test.png')
    original_pixel_data = list(image.getdata())
    get_data(original_pixel_data)

    

if __name__ == '__main__':
    #to encode
    main()
    
    #to decode
    main2()
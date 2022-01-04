from PIL import Image

def encode_data(original_pixel,img_pixel):
    r,g,b = original_pixel
    r1,g1,b1 = img_pixel
    
    r = r>>2
    r = r<<2
    r += r1
    
    g = g>>2
    g = g<<2
    g += g1
    
    b = b>>2
    b = b<<2
    b += b1
    
    return (r,g,b)

def img_bits(pixel):
    r,g,b = pixel
    r = bin(r)[2:].rjust(8,'0')
    g = bin(g)[2:].rjust(8,'0')
    b = bin(b)[2:].rjust(8,'0')
    
    r1 = int(r[0:2],2)
    r2 = int(r[2:4],2)
    
    g1 = int(g[0:2],2)
    g2 = int(g[2:4],2)
    
    b1 = int(b[0:2],2)
    b2 = int(b[2:4],2)
    
    return ((r1,g1,b1),(r2,g2,b2))
    # first_two = '11000000'
    # next_two  = '00110000'
    
    # val1 = int(first_two,2)
    # val2 = int(next_two,2)
    
    
    # r1 = r & val1
    # r2 = r & val2
    
    # g1 = g & val1
    # g2 = g & val2
    
    # b1 = b & val1
    # b2 = b & val2
    
    # return ((r1,g1,b1),(r2,g2,b2))
    pass

def put_data(original_pixels,img_pixel):
    # original_pixels[0] = encode_data(original_pixels[0],(0,0,0))
    # original_pixels[1] = encode_data(original_pixels[1],(0,0,0))
    original_pixels[0] = (0,1,0)
    original_pixels[1] = (0,1,0)
    counter = 2
    for pixel in img_pixel:
        data1,data2 = img_bits(pixel)
        original_pixels[counter] = encode_data(original_pixels[counter],data1)
        counter += 1
        original_pixels[counter] = encode_data(original_pixels[counter],data2)
        counter += 1
        pass
    # original_pixels[counter] = encode_data(original_pixels[counter],(0,0,0))
    # original_pixels[counter+1] = encode_data(original_pixels[counter+1],(0,0,0))
    original_pixels[counter]   = (0,1,0)
    original_pixels[counter+1] = (0,1,0)
    
    return original_pixels
    pass

def get_data(pixel_data):
    buf1 = []
    buf2 = []
    pixel_list = []
    mask = (1 << 2) - 1
    counter = 0
    flag_counter = 0
    for pixel in pixel_data:
        if(counter==0):
            r,g,b = pixel
            buf1.append(r & mask)
            buf1.append(g & mask)
            buf1.append(b & mask)
            pass
        
        elif(counter%2==0):
            
            bin_r1 = (bin(buf1[0])[2:].rjust(2,'0') + bin(buf2[0])[2:].rjust(2,'0')).ljust(8,'0') 
            bin_g1 = (bin(buf1[1])[2:].rjust(2,'0') + bin(buf2[1])[2:].rjust(2,'0')).ljust(8,'0') 
            bin_b1 = (bin(buf1[2])[2:].rjust(2,'0') + bin(buf2[2])[2:].rjust(2,'0')).ljust(8,'0')
            
            r1 = int(bin_r1,2)
            g1 = int(bin_g1,2)
            b1 = int(bin_b1,2)
            
            # print("aaa")               
            if((r1,g1,b1) == (0,80,0)):
                print("Here")
                if(flag_counter == 1):
                    break
                flag_counter += 1
                
            else:
                pixel_list.append((r1,g1,b1))
            
            buf1 = []
            buf2 = []
            r,g,b = pixel
            buf1.append(r & mask)
            buf1.append(g & mask)
            buf1.append(b & mask)
            pass
        
        else:
            r,g,b = pixel
            buf2.append(r & mask)
            buf2.append(g & mask)
            buf2.append(b & mask)
            pass
        counter+=1
        pass
    
    return tuple(pixel_list)
    pass

def main():
    original_image = Image.open("media/sierra.jpg")
    original_pixel_data = list(original_image.getdata())
    
    img = Image.open("media/mac.jpg")
    img_pixel_data = list(img.getdata())
    
    result = put_data(original_pixel_data,img_pixel_data)
    new_img = Image.new(original_image.mode,original_image.size)
    new_img.putdata(tuple(result))
    new_img.save('test2.png')
    pass

def main2():
    image = Image.open('test2.png')
    pixel_data = list(image.getdata())
    # print(pixel_data[0],pixel_data[1],pixel_data[-2],pixel_data[-1])
    data = get_data(pixel_data)
    
    # for i in range(100):
        # print(data)
    # print(len(data))
    
    # new_img = Image.new('RGB',(5000,3124))
    new_img = Image.new('RGB',(1920,1080))
    new_img.putdata(data)
    new_img.save("new.png")

if __name__ == '__main__':
    main()
    main2()


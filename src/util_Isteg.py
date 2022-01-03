#Both height and width will use 3 pixels 222222111
def encode_to_pixel(pixel,bin_pixel_data):
    print(len(pixel))
    r,g,b = pixel
    shift = len(bin_pixel_data)//3
    
    r = r>>shift
    r = r<<shift    
    g = g>>shift
    g = g<<shift
    b = b>>shift
    b = b<<shift
    
    if   len(bin_pixel_data) == 6:
        r += int(bin_pixel_data[0:2],2)
        g += int(bin_pixel_data[2:4],2)
        b += int(bin_pixel_data[4:6],2)
        
    elif len(bin_pixel_data) == 3:
        r += int(bin_pixel_data[0:1],2)
        g += int(bin_pixel_data[1:2],2)
        b += int(bin_pixel_data[2:3],2)
    
    return (r,g,b)

def add_dimensions(original_img_pixels,offset,bin_width,bin_height):
    original_img_pixels[offset]   = encode_to_pixel(original_img_pixels[offset],bin_width[0:6])
    original_img_pixels[offset+1] = encode_to_pixel(original_img_pixels[offset+1],bin_width[6:12])
    original_img_pixels[offset+2] = encode_to_pixel(original_img_pixels[offset+2],bin_width[12:15])
    
    original_img_pixels[offset+3] = encode_to_pixel(original_img_pixels[offset+3],bin_height[0:6])
    original_img_pixels[offset+4] = encode_to_pixel(original_img_pixels[offset+4],bin_height[6:12])
    original_img_pixels[offset+5] = encode_to_pixel(original_img_pixels[offset+5],bin_height[12:15])
    
    offset += 6
    return original_img_pixels,offset

def add_data_size(original_img_pixels,offset,bin_payload_size):
    original_img_pixels[offset]     = encode_to_pixel(original_img_pixels[offset],bin_payload_size[0:6])
    original_img_pixels[offset+1]   = encode_to_pixel(original_img_pixels[offset+1],bin_payload_size[6:12])
    original_img_pixels[offset+2]   = encode_to_pixel(original_img_pixels[offset+2],bin_payload_size[12:18])
    original_img_pixels[offset+3]   = encode_to_pixel(original_img_pixels[offset+3],bin_payload_size[18:24])
    original_img_pixels[offset+4]   = encode_to_pixel(original_img_pixels[offset+4],bin_payload_size[24:27])
    
    offset += 5
    return original_img_pixels,offset

def add_header(original_img_pixels,payload_dimensions,
               num_payload_pixels,num_flag_pixels=2):
    
    # offset = 0
    
    #FLAG-> All even
    for i in range(num_flag_pixels):
        pixel_data = []
        for component in original_img_pixels[i]:
            if component%2 == 0:
                pixel_data.append(component)
            else:
                pixel_data.append(component+1)
        original_img_pixels[i] = tuple(pixel_data)
        
    pixel_offset = 2
    payload_width,payload_height = payload_dimensions
    
    bin_width  = bin(payload_width)[2:].rjust(15,'0')
    bin_height = bin(payload_height)[2:].rjust(15,'0')
    bin_size   = bin(num_payload_pixels)[2:].rjust(27,'0')
    
    original_img_pixels,pixel_offset = add_dimensions(original_img_pixels,pixel_offset,bin_width,bin_height)
    original_img_pixels,pixel_offset = add_data_size (original_img_pixels,pixel_offset,bin_size)
    
    return original_img_pixels,pixel_offset

def pixel_MSB(pixel):
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

def encode_data(original_pixel,half_img_pixel):
    r,g,b = original_pixel
    r1,g1,b1 = half_img_pixel
    
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
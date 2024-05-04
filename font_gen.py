from PIL import ImageFont, ImageDraw, Image



def GenBackground(cell_size, padding_size, maximum_cell_number):
    width = maximum_cell_number * (padding_size + cell_size) + padding_size 
    height = width
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0)) 
    return img

def GetChar(txt_path):
    with open(txt_path, 'r', encoding="utf-8") as f:
        chars = f.readline().split(' ')
    return chars

def WriteChar(chars, img, font_path, font_size, cell_size, padding_size, maximum_cell_number):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    width_offset = padding_size
    height_offset = padding_size + cell_size
    char_count = 0
    for char in chars:
        draw.text((width_offset,height_offset), text = char, fill='black', anchor = 'ld', font=font)
        char_count +=1
        width_offset += cell_size + padding_size
        if char_count == maximum_cell_number:
            char_count = 0
            width_offset = padding_size
            height_offset += cell_size + padding_size
    return img

def main():
    cell_size = 30
    padding_size = 1
    maximum_cell_number = 20

    font_size = 20

    txt_path = 'a.txt'
    font_path = 'JetBrainsMonoJP-Regular.ttf'
    chars = GetChar(txt_path)
    img = GenBackground(cell_size, padding_size, maximum_cell_number)
    img = WriteChar(chars, img, font_path, font_size, cell_size, padding_size, maximum_cell_number)
    img.show()


if __name__ == '__main__':
    main()

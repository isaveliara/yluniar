from PIL import Image, ImageDraw, ImageFont
from flask import Response
from io import BytesIO

def replace_chars_for_render_in_image(step):
    return step.replace('^2', '²').replace('/', ' ÷ ').replace('*', ' × ').replace('+'," + ").replace("-",' - ')
#this function render the steps of equation for create the image of them
def render_steps_to_image(steps, output_image=None):
    # Font and image size setup
    img_width = 600
    img_height = 100 + len(steps) * 40 #adjust height based on number of steps
    font_size_large = 24
    font_size_small = 18
    
    #load fonts
    try:
        font_large = ImageFont.truetype("./static/fonts/Roboto-Light.ttf", font_size_large)
        font_small = ImageFont.truetype("./static/fonts/Roboto-Light.ttf", font_size_small)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    #create the image
    img = Image.new("RGB", (img_width, img_height), "#2C2C2C") #dark gray background
    draw = ImageDraw.Draw(img)
    
    #starting point for text ps.
    y_position = 20
    
    #"Solution" title
    draw.text((img_width//2 - 60, y_position), "Solution", font=font_large, fill="white")
    y_position += 50 #space after title
    
    # Render each step onto the image
    for idx, text in enumerate(steps):
        if idx == 0 or idx == 1: #larger for the first lines
            draw.text((20, y_position), text, font=font_large, fill=(39, 155, 161))#cyan
        elif idx == 2:
            draw.text((20, y_position), text, font=font_large, fill=(168, 29, 29))#red
        else:
            draw.text((20, y_position), text, font=font_small, fill=(171,150,29))#yellow
        y_position += 40 #move to the next line
    
    #save the image
    if output_image:
        #save the image to a file if output_image is provided like from tests.py
        img.save(f"results.{output_image}")
        print(f"Solution steps saved to ./results/{output_image}")
        return None
    else:
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)

        #return the image as a response for flask
        return Response(img_io, mimetype='image/png')
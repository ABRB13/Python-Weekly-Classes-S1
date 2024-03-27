def load_image(image):

    from PIL import Image
    
    global px 
    image = Image.open(image)

    px = image.load()

    return px

def process():
    
    global pixels
    global coordinates 

    pixels = []
    coordinates = []

    for a in range (0, 768):
        for b in range (0,768): #0, 0
            rgb = px[a,b] #px[0,0], 
            coordinates.append([a,b])

            if rgb[0] <= 20:
                pixels.append((0,0,0))
            else:
                pixels.append((80,80,80))
    return pixels, coordinates 

def dataframe():

    import pandas as pd 

    column = ['coordinates', 'pixels']
    global df

    df = pd.DataFrame(zip(coordinates, pixels), columns = column)

def build_image(output_dir):
    from PIL import ImageDraw, Image 

    ouput = Image.new("RGB", (768,768))
    draw = ImageDraw.Draw(ouput)


    for row in df.itertuples(index=True, name='Pandas'):
        draw.point(row.coordinates, row.pixels)

    ouput.save(output_dir)
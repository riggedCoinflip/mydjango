from PIL import Image, ImageDraw

class Circlefy(object):
    '''
    crop an image to a circle.
    requires aspect ratio 1:1, not tested with other aspect ratios
    '''
    def process(self, image: Image):
        # create new RGBA image from image
        back = Image.new('RGBA', image.size)
        back.paste(image)
        # create a mask with the same size, but nontransparent
        mask = Image.new('RGBA', image.size, (0, 0, 0, 255))
        # make the inner circle transparent
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=(255, 255, 255, 0))
        # add visible (non-circle-outline) to image. This is used for JPEG as alpha channel is not supported.
        # better solutions for alpha-channel-supporting formats exists.
        back.paste(mask, mask=mask)
        return back

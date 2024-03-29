import pytesseract
from PIL import Image, ImageChops
# import keras
# from keras.preprocessing import image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\andre\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class ImageRecognizer:
    def __init__(self):
        self.recognizer = pytesseract

    def trim(self, img):
        bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return img.crop(bbox)
        
    def transformToSize(self, img): # target 28x28
        target_size = 28
        width, height = img.size

        aspect_ratio = width / height if width < height else height / width
        if width > height:
            new_width = target_size
            new_height = int(target_size * aspect_ratio)
        else:
            new_height = target_size
            new_width = int(target_size * aspect_ratio)
        img_resized = img.resize((new_width, new_height))

        square_image = Image.new("RGB", (target_size, target_size), "white")
        x_offset = (target_size - new_width) // 2
        y_offset = (target_size - new_height) // 2
        square_image.paste(img_resized, (x_offset, y_offset))
        return square_image
    
    # def predict(img_path):
    #     model = keras.models.load_model("weights.hdf5")
    #     img_generator = image.ImageDataGenerator(preprocessing_function=lambda img: img/255.0)
    #     validation_generator = img_generator.flow_from_directory(directory=img_path, target_size=(28,28), shuffle=False,
    #                                                             batch_size=1, color_mode="grayscale",)

    def imageToNumbers(self, canvasImage):
        trimmed_image = self.trim(canvasImage)
        transformed_image = self.transformToSize(trimmed_image)
        image_name = 'answer_drawing.png'
        transformed_image.save(image_name)
        # number = self.predict(image_name)
        number = self.recognizer.image_to_string(transformed_image, config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
        print(number)
        return number
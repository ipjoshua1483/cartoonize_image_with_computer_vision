import cv2
import io
from IPython.display import display
from ipywidgets import FileUpload
import numpy as np
import matplotlib.pyplot as plt

class Cartoonize:
    def __init__(self):
        self.image = None

    def upload_image(self):
        self.upload_widget = FileUpload(accept='', multiple=False)
        display(self.upload_widget)

    def load_image(self, content):
        file_content = np.frombuffer(content, np.uint8)
        self.image = cv2.imdecode(file_content, cv2.IMREAD_COLOR)
        self.image_original = self.image.copy()
        self._edge_mask_before()

    def save_image(self, file_path, original: bool = True):
        if original:
            cv2.imwrite(file_path, self.image_original)
        else:
            cv2.imwrite(file_path, self.image)

    def _check_upload_widget(self):
        if self.upload_widget.value:
            try:
                content = self.upload_widget.value[0]['content']
                self.load_image(content)
            except:
                print("Please upload an image")
    
    def display_image(self):
        if self.image is None:
            self._check_upload_widget()
        if self.image is None:
            print("Please upload an image before displaying")
        else:
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            plt.imshow(image_rgb)
            plt.axis('off')
            plt.show()
    
    def color_quantization(self, k = 9):
        data = np.float32(self.image).reshape((-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
        ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        self.image = center[label.flatten()].reshape(self.image.shape)

    def bilateral_filter(self):
        self.image = cv2.bilateralFilter(
            self.image, d = 7, sigmaColor = 200, sigmaSpace = 200
        )

    def _edge_mask_before(self, line_size = 7, blur_value = 7):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, blur_value)
        self.edges = cv2.adaptiveThreshold(
            gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value
        )
        # self.image = cv2.bitwise_and(self.image, self.image, mask = self.edges)
    
    def edge_mask(self):
        self.image = cv2.bitwise_and(self.image, self.image, mask = self.edges)
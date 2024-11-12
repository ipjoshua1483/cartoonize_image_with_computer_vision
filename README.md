# Cartoonize Image with Computer Vision
This repo contains the code of cartoonizing custom images with Computer Vision. The webapp deployed with Flask on AWS can be found here: [(https://tinyurl.com/ipjoshua-cartoon-CV)](https://tinyurl.com/ipjoshua-cartoon-CV) and the jupyter notebook that cartoonizes locally can be found here: [```cartoonize_visualize.ipynb```](https://github.com/ipjoshua1483/cartoonize_image_with_computer_vision/blob/main/cartoonize_visualize.ipynb).
This README provides a step-by-step process on cartoonizing with an example.

# Cartoonize with webapp deployed with Flask on AWS

<div align="center">
  <img src="/images/webapp_1.png" alt="Webapp home"/>
</div>

The [link](https://tinyurl.com/ipjoshua-cartoon-CV) to the webapp will direct you to this page. To cartoonize an image, first click on 'Browse' and select an image, then click on 'Cartoonize' to convert it.

<div align="center">
  <img src="/images/webapp_2.png" alt="Webapp cartoonized"/>
</div>

This will display the original and cartoonized images side-by-side. Click on 'Download Cartoonized Image' to download and click on 'Cartoonize Another Image' to repeat this process on another image of your choice.

# Cartoonize locally with jupyter notebook

## Installation
Install python verison 3.12.7 and run the following commands:

```bash
pip install -r requirements_local.txt
```

## Upload image
```python
import cartoonize
cartoonize_obj = cartoonize.Cartoonize()
cartoonize_obj.upload_image()
```

## Display original image
```python
cartoonize_obj.display_image()
```
<div align="center">
  <img src="/images/test_original.png" alt="Original Image"/>
</div>

## Reduce color palette via color quantization through K-means clustering
```python
cartoonize_obj.color_quantization()
cartoonize_obj.display_image()
```
<div align="center">
  <img src="/images/test_color_quantization.png" alt="Image with Color Quantization"/>
</div>

## Apply a bilateral filter to further blur the image
```python
cartoonize_obj.bilateral_filter()
cartoonize_obj.display_image()
```
<div align="center">
  <img src="/images/test_bilateral_filter.png" alt="Image with Bilateral Filter"/>
</div>

## Create an edge mask and use bitwise operations to insert them into the image
```python
cartoonize_obj.edge_mask()
cartoonize_obj.display_image()
```
<div align="center">
  <img src="/images/test_edge_mask.png" alt="Image with Edge Mask"/>
</div>




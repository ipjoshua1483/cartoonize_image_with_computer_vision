# Cartoonize Image with Computer Vision
This repo contains the code of cartoonizing an image with Computer Vision. This provides a step-by-step process on cartoonizing with an example; please refer to ```cartoonize_visualize.ipynb``` to cartoonize custom images. 

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

## Display image
```python
cartoonize_obj.display_image()
```

![image_original](/images/test_original.png)

## Reduce color palette via color quantization through K-means clustering.
```python
cartoonize_obj.color_quantization()
cartoonize_obj.display_image()
```
![image_original](/images/test_color_quantization.png)

## Apply a bilateral filter to further blur the image
```python
cartoonize_obj.bilateral_filter()
cartoonize_obj.display_image()
```
![image_original](/images/test_bilateral_filter.png)

## Create an edge mask and use bitwise operations to insert them into the image
```python
cartoonize_obj.edge_mask()
cartoonize_obj.display_image()
```
![image_original](/images/test_edge_mask.png)




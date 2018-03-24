# 问题记录
记录计算机视觉项目中遇到的问题
*******

## opencv

- python opencv error in Emacs when running cv2.Canny() ?

load your image `img= np.uint8(img)`. Use `cv2.Canny` after

```
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
```

## **Redundancy Remover**
Images usually consists of an important memory saved in the form of jpg, jpeg, png, etc. However, we're often stuck with several copies of the same images, saved under different names on our devices and manually sorting through them is tedious to say the least. For this, I created a web application called 'Redundancy Remover' using Python, Flask, HTML, CSS, and JavaScript that takes several images as an input, searches for similar images among them, deletes copies of an existing image and produces a zipped file of single copies of all the uploaded images as an output.

### **Detection of Similar Images**
To detect similar images, I've use the hashing method that is specifically developed for images: Average Hashing.

Following are the steps for identifying similar images using the Average Hashing Algorithm:
1. Reduction of the image's size
2. Gray Scaling
3. Calculating the mean pixel value of the whole image
4. Convert the entire image into binary bits using the mean pixel value of the whole image as a threshold value.
5. Construct the hash value
6. Compare the hash value of all the uploaded images. 
7. If simlar hash values are found, a duplicate is detected else the image is unique and passed on to the user as the ouput.

### **How to run this project?**

1. After downloading this repository and opening it in any IDE, activate the environment by typing the following in the terminal

```
env\Scripts\activate
```
> By doing this, you won't need to install any external modules or packages as everything that is required to run the program will be available in the environment. These modules can viewed in the [env folder](https://github.com/jendcruz22/RedundancyRemover/tree/master/env).

2. Once you've done this, the environment name (in this case 'env') should be visible at the beginning of a new terminal line. Now, run the python program to start the server.


```
python main.py
```
3. Go to the browser and type 


```
localhost:5000
```

or


```
http://127.0.0.1:5000/
```

### **Demonstration**
https://vimeo.com/509730343





 

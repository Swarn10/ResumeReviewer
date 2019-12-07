from pdf2image import convert_from_path
import cv2 
import numpy as np 
import pytesseract 
from PIL import Image   


def pdf_to_image_to_text(pdf_path):
	all_text = ""
	pages = convert_from_path(pdf_path,500)  
	for page in pages :
	    page.save('out.jpg','JPEG') 
	    all_text += get_string('out.jpg')  

	return all_text 


def get_string(img_path) :

	img = cv2.imread(img_path) 
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	kernel = np.ones((1,1), np.uint8)

	img = cv2.dilate(img, kernel, iterations=1) 
	img = cv2.erode(img, kernel, iterations=1) 

	cv2.imwrite("removed_noise.png", img) 

	cv2.imwrite(img_path, img) 

	result = pytesseract.image_to_string(Image.open(img_path))

	return result 



if __name__ == "__main__" :

	pdf_path = "cvGenerate.pdf"  
	all_text = pdf_to_image_to_text(pdf_path) 
	with open("PDF.txt","w") as f :
		f.write(all_text) 





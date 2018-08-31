import face_recognition
import os 
import shutil
import os.path


# put how many pictures you have instead of 111 
picnumber = 111 

# add the file that has your face in it 
if not os.path.exists("found"):
    os.makedirs("found")

# load the face and encode it 
image = face_recognition.load_image_file("face.jpg")
main_encoding = face_recognition.face_encodings(image)[0]

# to select the image
pic = 1

#encode every image and compare incodings 
while picnumber >=0 :		
	img = str(pic) +".jpg"
	unknown_image = face_recognition.load_image_file(img)
	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
	results = face_recognition.compare_faces([main_encoding], unknown_encoding)

	#see if the results is true move the image to found file  
	if results[0] == True :
		shutil.move(img, "found/"+ img)
	# else will print the file name 
	else :
		print("Can't detect wanted face in" + str(pic) +".jpg")	
	pic = pic + 1
	picnumber -= 1
	#----------------------------------------

import cv2,os,shutil,glob



images = glob.glob("*.jpg")
destination = "C:\\Users\\[your_username]\\Downloads\\Test3"
source = r"C:\Users\mrbea\Downloads\Sample-Images\sample-images"

for image in images:
    img = cv2.imread(image,1)
    resized_images = cv2.resize(img,(500,500))
   
    cv2.imshow("Hey",resized_images)      
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,resized_images)

    for root, subdirs, files in os.walk(source):
            path = os.path.join(root,"resized_"+image)
            shutil.move(path,destination)

        
                

    
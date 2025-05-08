import serial
import cv2
import time
import numpy as np

# Set the serial port name and baud rate to match the Arduino
ser = serial.Serial('com2', 115200)
time.sleep(5)

# Function to send a 2D array over serial
def send_2d_array(img_arr):
    print(img_arr.shape)
    rows, cols= img_arr.shape

    ser.write(str(rows).encode())  # Send the number of rows
    ser.write(b' ')
    ser.write(str(cols).encode())  # Send the number of columns
    ser.write(b' ')

    for row in img_arr:
        for item in row:
            ser.write(str(item).encode())  # Convert int to bytes and send
            ser.write(b',')  # Send a space as a separator

    ser.write(b'\n')  # Send a newline character to indicate the end of the array


def image_to_binary_array(image):
    try:
        _, binary_image = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY)

        # Convert the binary image to a NumPy array
        binary_array = (binary_image/255).astype(int)
        
        return binary_array
        
    except Exception as e:
        print(f"Error: {e}")
        return None
   
nose_img = cv2.imread('mata dan hidung biner V3\img_42_mata dan hidung biner.jpg', cv2.IMREAD_GRAYSCALE) # gambar grayscale
# print (nose_img[:50, :50])
data_to_send = image_to_binary_array(nose_img)
send_2d_array(data_to_send)
time.sleep(0.5)



# data_to_send = image_to_binary_array(nose_img)
# send_2d_array(data_to_send)
# time.sleep(0.5)
    
# Close the serial port
ser.close()

# nose_img = cv2.imread('img_63_mata dan hidung.jpg') # gambar grayscale
# print("ukuran gambar full = ",nose_img.shape)
# print ("\nBGRimage")
# print (nose_img[:2, :3, :3])
# img = cv2.cvtColor(nose_img,cv2.COLOR_BGR2GRAY)
# print ("\ngrayimage")
# print (img[:2, :3])
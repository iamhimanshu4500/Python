import qrcode
import image
 
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10, # size of the box where qr code will be displayed
    border = 5 # it is the white part of image border in all 4 sides with white color
)

data = "https://translate.google.co.in/"

# if you don't want to redirect and create for normal text that write text in the quotes
 
qr.add_data(data)
 
qr.make(fit= True)
 
img  = qr.make_image(fill="black", back_color="white")
 
img.save("test.png")

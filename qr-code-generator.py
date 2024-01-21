import qrcode
from qrcode.image.styledpil import StyledPilImage as SPI
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer as RMD

print("\nWelcome to the one and only QR Code generator created by Maverick L. the apprentice programmer!\n\n"+"A few questions will be asked below in order to generate said QR Code.\n")

while True:
    website_link = input("Enter link : ")
    name = input("Enter the name of your soon-to-be QR Code : ")
    try:
        qr = qrcode.QRCode(version = float(input("Enter a number in between 1 and 40 to set QR code size : ")), 
                        box_size = float(input("Enter a number in between 1 and 75 to set the pixels in a single box of the QR Code : ")), 
                        border = float(input("Enter a number in between 1 and 75 to set how many boxes thick the border is going to be : ")))
        if qr.version >= 1 and qr.version <= 40 and qr.box_size >= 1 and qr.box_size <= 75 :
            continue
        else:
            print("The numbers were too big, or something unexpected was entered, please try again.")
             
    except:
        print("Error, you have entered something unexpected, please try again.")
        break
    qr.add_data(website_link) and qr.make()

    if input("Do you want rounded squares? Type Yes if so, and type anything else for No.") == "Yes":
        r_img = qr.make_image(image_factory=SPI, module_drawer=RMD())
        r_img.save(name+".png")
    else:
        img = qr.make_image()
        img.save(name+".png")
    if input("Do you want to make another QR Code? If so, write Yes, if not, write anything else.\n") == "Yes":continue
    else: 
        print("Ok, see you later then!")
        break

#Documentation here : https://github.com/lincolnloop/python-qrcode 
# and this https://www.codedex.io/projects/generate-a-qr-code-with-python
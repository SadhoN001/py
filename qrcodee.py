import qrcode

text = input("enter the text to convert in the qr code(.com): ")
filename= input("enter the file name to save the qr code(.png): ")

def generate_qr_code(text, filename):
    #qrcode make()
    image_qrcode= qrcode.make(text)
    #save the img
    image_qrcode.save(filename)

generate_qr_code(text, filename)
###-------------------------------------------
# import qrcode

# # text = input("enter the text to convert in the qr code(.com): ")
# # filename= input("enter the file name to save the qr code(.png): ")

# def generate_qr_code(filepath):
#     with open(filepath, 'r') as file:
#         lines= file.readlines() #[0 inext first line, 1 index 2nd line]
        
#     text= lines[0].strip()
#     filename= lines[1].strip()
    
    
#     #qrcode make()
#     image_qrcode= qrcode.make(text)
#     #save the img
#     image_qrcode.save(filename)

# generate_qr_code('qrcodee.txt')

import qrcode

user_input = input("Enter the text or URL: ").strip()
file_name = input("Enter filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=3)
qr.add_data(user_input)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)

print(f"Success! QR code saved as {file_name}")
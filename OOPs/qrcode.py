import qrcode
# the link to be converted into QR code
link = "https://www.example.com/"

# create QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add data to QR code
qr.add_data(link)

# create and save QR code image file
img = qr.make_image(fill_color="black", back_color="white")
img.save("example.png")
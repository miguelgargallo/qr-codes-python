import qrcode

link = "https://www.example.com"

img = qrcode.make(link)

img.save("qr-short.png")

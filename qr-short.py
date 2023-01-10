import qrcode

link = "https://miguelgargallo.com"

img = qrcode.make(link)

img.save("qr-short.png")

import qrcode
img = qrcode.make('https://l2ep.univ-lille.fr/')
type(img)  # qrcode.image.pil.PilImage
img.save("laboratoirel2ep.png")

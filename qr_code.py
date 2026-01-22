import qrcode
data="hi this is my QR"
qr=qrcode.make(data)
qr.save(file_path)
print(f"QR Code generated and saved to {file_path}")
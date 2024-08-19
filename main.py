import pyqrcode

url=input("URL Giriniz:")

qr_code =pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=6)

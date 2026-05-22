import qrcode, sys, os

def generate_qr(data, output='qr.png', size=10, border=2):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(output)
    print(f'QR code saved to {output} ({os.path.getsize(output)} bytes)')

if __name__=='__main__':
    data = sys.argv[1] if len(sys.argv)>1 else 'https://github.com'
    output = sys.argv[2] if len(sys.argv)>2 else 'qr.png'
    generate_qr(data, output)

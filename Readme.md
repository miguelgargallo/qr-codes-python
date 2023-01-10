# QR Code Generation

![qr-codes-python](https://user-images.githubusercontent.com/5947268/211444197-0dd85aa6-8963-484e-87c8-cf7b111ab2d8.png)

- [QR Code Generation](#qr-code-generation)
  - [Usage](#usage)
    - [qr-short.py](#qr-shortpy)
    - [qr-long.py](#qr-longpy)
  - [Customization](#customization)
  - [License](#license)

These scripts generate QR codes containing a link or a long message, using the qrcode library in Python.
Requirements

- Python
- qrcode library (can be installed using pip install qrcode)

## Usage

### qr-short.py

This script generates a QR code containing a link.

To use it, modify the link variable to contain the desired link, and then run the script:

```python
python qr-short.py
```

This will generate a QR code image called "qr-short.png" that, when scanned, will open the link in a web browser.

### qr-long.py

This script generates a QR code containing a long message, using segmentation to split the data into multiple QR codes.

To use it, modify the data variable to contain the desired message, and then run the script:

```python
python qr-long.py
```

This will generate a QR code image called "qr-long.png" that contains the message.

## Customization

Both scripts allow for some customization of the QR code appearance. In qr-short.py, you can use the size, error_correction, and border options of the qrcode.make function to set the size, error correction level, and border of the QR code, respectively.

In qr-long.py, you can use the version, error_correction, box_size, and border options of the qrcode.QRCode class to set the version, error correction level, box size, and border of the QR code, respectively. You can also use the fill_color and back_color options of the qrcode.make_image function to set the colors of the QR code.

## License

We use a Pylar AI creative ML License, more info in our file [License](LICENSE.md)

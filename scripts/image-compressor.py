import os, sys
from pathlib import Path

def compress_image(filepath, quality=85, max_size=None):
    from PIL import Image
    img = Image.open(filepath)
    if max_size:
        img.thumbnail(max_size)
    output = filepath.replace(Path(filepath).suffix, '_compressed' + Path(filepath).suffix)
    img.save(output, quality=quality, optimize=True)
    orig = os.path.getsize(filepath)
    comp = os.path.getsize(output)
    ratio = (1 - comp/orig) * 100
    print(f'{filepath}: {orig} -> {comp} bytes (-{ratio:.1f}%)')

if __name__=='__main__':
    compress_image(sys.argv[1])

"""Arma un reel vertical (1080×1920, 30 fps, MP4 H.264 + audio mudo) a partir de imágenes.

Uso:
  python scripts/reel.py --out out/reel.mp4 --imagenes out/post1_1.png out/post1_2.png ... [--seg 2.8]

Cada imagen se centra sobre fondo negro de la marca con un zoom lento (efecto Ken Burns)
y un fundido entre una y otra. Si la imagen ya es 1080×1920 ocupa toda la pantalla.
La última imagen dura un poco más (es la del llamado a la acción).
"""
import argparse, shutil, subprocess
from PIL import Image

W, H, FPS = 1080, 1920, 30
FONDO = (11, 11, 12)


def ffmpeg_bin():
    f = shutil.which('ffmpeg')
    if f:
        return f
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def lienzo(img, zoom):
    """Devuelve un frame 1080×1920 con la imagen centrada y escalada por `zoom`."""
    base = Image.new('RGB', (W, H), FONDO)
    w = int(W * zoom)
    h = int(img.height * w / img.width)
    if h > H * zoom:  # imagen vertical completa (historia)
        h = int(H * zoom)
        w = int(img.width * h / img.height)
    im = img.resize((w, h), Image.LANCZOS)
    base.paste(im, ((W - w) // 2, (H - h) // 2))
    return base


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--imagenes', nargs='+', required=True)
    ap.add_argument('--seg', type=float, default=2.8, help='segundos por imagen')
    a = ap.parse_args()
    imgs = [Image.open(p).convert('RGB') for p in a.imagenes]
    n_fade = int(0.4 * FPS)
    cmd = [ffmpeg_bin(), '-y', '-loglevel', 'error',
           '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100',
           '-shortest', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
           '-profile:v', 'high', '-movflags', '+faststart', '-c:a', 'aac', '-b:a', '128k', a.out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_last = None
    for i, img in enumerate(imgs):
        seg = a.seg + (1.2 if i == len(imgs) - 1 else 0)
        n = int(seg * FPS)
        for f in range(n):
            frame = lienzo(img, 1.0 + 0.05 * f / n)
            if prev_last is not None and f < n_fade:
                frame = Image.blend(prev_last, frame, (f + 1) / n_fade)
            p.stdin.write(frame.tobytes())
        prev_last = frame
    p.stdin.close()
    if p.wait():
        raise SystemExit('ffmpeg falló al armar el reel')
    print('Reel listo:', a.out)


if __name__ == '__main__':
    main()

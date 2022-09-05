from blind_watermark import WaterMark

def Aa():
    bwm1 = WaterMark(password_wm=1, password_img=1)
    # read original image
    bwm1.read_img('/Users/qin/Desktop/a.png')
    # read watermark
    bwm1.read_wm('/Users/qin/Desktop/b.png')
    # embed
    bwm1.embed('/Users/qin/Desktop/c.png')


def Ab():
    bwm1 = WaterMark(password_wm=1, password_img=1)
    # notice that wm_shape is necessary
    bwm1.extract(filename='/Users/qin/Desktop/c.png', wm_shape=(64, 64), out_wm_name='/Users/qin/Desktop/d.png', )

if __name__ == '__main__':
    # Aa()
    Ab()
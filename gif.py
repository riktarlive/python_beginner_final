import imageio.v3 as iio

filenames = ["ezio1.jpg", 'ezio2.jpg', 'ezio3.jpg']

images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('ezio.gif', images, duration = 800, loop = 0)

 
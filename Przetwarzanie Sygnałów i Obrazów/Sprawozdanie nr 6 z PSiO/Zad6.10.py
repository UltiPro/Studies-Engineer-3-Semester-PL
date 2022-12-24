import cv2
import multibin as mb
import utility as ut
from matplotlib import pyplot as plt
from IPython.display import display

bin_methods = [
    {
        'type': 'niblack',
        'window_size': 61,
        'k_factor': 0.2
    },
    {
        'type': 'niblack',
        'window_size': 11,
        'k_factor': 0.4
    },
    {
        'type': 'sauvola',
        'window_size': 31,
        'k_factor': 0.4
    }
]
    
photo = cv2.imread('kot.jpg')
plt.imshow(photo)

KERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
RESIZE = (700,400)

photo = cv2.imread('kot.jpg')
plt.imshow(photo)

KERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
RESIZE = (700,400)

bin_photos = mb.binarize(photo, bin_methods, resize=RESIZE, morph_kernel=KERNEL, return_original=True)
original_photo = bin_photos[0]

fig=plt.figure(figsize=(10,4),tight_layout=1)

plot_idx = 1

for idx, bin_photo in enumerate(bin_photos[1:]):
    title = "Type: {}; w: {}; k: {}".format(bin_methods[idx]['type'], bin_methods[idx]['window_size'], bin_methods[idx]['k_factor'])
    fig.add_subplot(2, 2, plot_idx, title=title)
    plt.imshow(bin_photo, cmap='gray')
    plot_idx += 1                      
plt.show()

candidate_boxes = []
candidate_centroids = []

for bin_photo in bin_photos[1:]:
    plot_photo = original_photo.copy()
    boxes, centroids = ut.get_candidate_regions(bin_photo)
    candidate_boxes += boxes
    candidate_centroids += centroids
    plot_photo =ut.plot_blobs(plot_photo, boxes)        
    fig.add_subplot(2, 2, plot_idx)
    plt.imshow(plot_photo, cmap='gray')
    plot_idx += 1    

plt.show()

fig=plt.figure(figsize=(10,4),tight_layout=1)

plot_photo = original_photo.copy()

ut.plot_blobs(plot_photo, candidate_boxes, plot_line=True, centroids=candidate_centroids)  
plt.imshow(plot_photo)
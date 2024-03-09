#include "../include/imageManager.h"
#include "../include/bmpStructs.h"
#include <stdlib.h>

/**
 * Creates an image from given width and height sizes
 * @param width - Number of pixels in uint64_t
 * @param height - Number of pixels in uint64_t
 * @return empty image with given parameters
 */
struct image* create_image(uint64_t width, uint64_t height) {
    struct image* image = (struct image*) malloc(sizeof(struct image));
    if (!image) return NULL;

    image->width = width;
    image->height = height;
    image->data = (struct pixel*) malloc(width * height * sizeof(struct pixel));

    if (!image->data) {
        free(image);
        return NULL;
    }

    return image;
}

/**
 * Frees memory of the image
 * @param img - pointer to the image to free memory from
 */
void destroy_image(struct image* img) {
    if (!img) return;
    if (img->data) {
        free(img->data);
    }
    free(img);
}


/**
 * Creates an image with content from a given image
 * @param image - image to copy
 * @return image with the copied content of the given image
 */
struct image* copy_image(const struct image* image) {
    struct image* new_image = create_image(image->width, image->height);
    if (!new_image) return NULL;

    for (size_t i = 0; i < image->width * image->height; i++) {
        new_image->data[i] = image->data[i];
    }

    return new_image;
}

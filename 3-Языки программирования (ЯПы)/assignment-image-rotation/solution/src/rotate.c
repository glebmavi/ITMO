#include "../include/rotate.h"
#include "../include/bmpStructs.h"
#include "../include/imageManager.h"
#include <stddef.h>

/**
 * Creates a new image from a rotated by 90 degrees to the left image
 * @param image - Input image
 * @return Rotated image or NULL
 */
struct image* rotate_left(const struct image* image) {
    struct image* new_image = create_image(image->height, image->width);
    if (!new_image) return NULL;

    for (size_t y = 0; y < image->height; y++) {
        for (size_t x = 0; x < image->width; x++) {
            new_image->data[y+((new_image->height-x-1) * new_image->width)] = image->data[x+y * image->width];
        }
    }

    return new_image;
}

/**
 * Creates a new image from a rotated by 90 degrees to the right image
 * @param image - Input image
 * @return Rotated image or NULL
 */
struct image* rotate_right(const struct image* image) {
    struct image* new_image = create_image(image->height, image->width);
    if (!new_image) return NULL;

    for (size_t y = 0; y < image->height; y++) {
        for (size_t x = 0; x < image->width; x++) {
            new_image->data[(new_image->width-y-1)+x * new_image->width] = image->data[x+y * image->width];
        }
    }

    return new_image;
}



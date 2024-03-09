#ifndef ASSIGNMENT_IMAGE_ROTATION_IMAGEMANAGER_H
#define ASSIGNMENT_IMAGE_ROTATION_IMAGEMANAGER_H
#include <stdint.h>

struct image* create_image(uint64_t width, uint64_t height);

void destroy_image(struct image* img);

struct image* copy_image(const struct image* image);

#endif //ASSIGNMENT_IMAGE_ROTATION_IMAGEMANAGER_H

#ifndef ASSIGNMENT_IMAGE_ROTATION_IMAGE_H
#define ASSIGNMENT_IMAGE_ROTATION_IMAGE_H
#include "bmpStructs.h"
#include <stdio.h>

// Constants
#define HEX_SIGNATURE 0x4D42 // hex description of bmp signature
#define BMP_HEADER_SIZE 40
#define RESERVED 0
#define COLOR_PLANES 1
#define PIXEL_BITS 24 // only 24-bit bmps are supported
#define COMPRESSION 0
#define X_PIXELS_PER_METER 0
#define Y_PIXELS_PER_METER 0
#define COLORS_USED 0
#define COLORS_IMPORTANT 0

/*  deserializer   */
enum read_status  {
    READ_OK = 0,
    READ_INVALID_SIGNATURE,
    READ_INVALID_BITS,
    READ_INVALID_HEADER,
    READ_MEMORY_ALLOCATION_ERROR,
    READ_INVALID_PIXEL_COUNT
    /* коды других ошибок  */
};

enum read_status from_bmp(FILE* input, struct image** image);

/*  serializer   */
enum  write_status  {
    WRITE_OK = 0,
    WRITE_HEADER_ERROR,
    WRITE_ERROR
    /* коды других ошибок  */
};

enum write_status to_bmp(FILE* output, struct image const* image);

struct bmp_header create_header(struct image const* image);
uint64_t get_padding(struct image const* image);
size_t get_image_size(struct image const* image);

#endif //ASSIGNMENT_IMAGE_ROTATION_IMAGE_H

#include "../include/bmp_io.h"
#include "../include/imageManager.h"
#include <stdio.h>

/**
 * Calculates the padding of a given image
 * @param image - Image to be given
 * @return padding value in bytes
 */
uint64_t get_padding(struct image const* image) {
    size_t bytes_per_row = image->width * sizeof(struct pixel);
    uint64_t padding = 0;

    if (bytes_per_row % 4 != 0) {
        padding = 4 - (bytes_per_row % 4);
    }

    return padding;
}

/**
 * Calculates the size of a given image, without the header
 * @param image - Image to be given
 * @return size of the image in bytes
 */
size_t get_image_size(struct image const* image) {
    uint64_t padding = get_padding(image);
    return (image->width * sizeof(struct pixel) + padding) * image->height;
}


/**
 * Creates a header struct from given image
 * @param image - It is used for getting width, height and padding
 * @return A bmp header struct with filled info
 */
struct bmp_header create_header(struct image const* image) {
    struct bmp_header header;
    header.bfType = HEX_SIGNATURE;
    header.bfileSize = get_image_size(image) + sizeof(struct bmp_header); // same as SizeImage + header size
    header.bfReserved = RESERVED;
    header.bOffBits = sizeof(struct bmp_header);
    header.biSize = BMP_HEADER_SIZE;
    header.biWidth = image->width;
    header.biHeight = image->height;
    header.biPlanes = COLOR_PLANES;
    header.biBitCount = PIXEL_BITS;
    header.biCompression = COMPRESSION;
    header.biSizeImage = get_image_size(image);
    header.biXPelsPerMeter = X_PIXELS_PER_METER;
    header.biYPelsPerMeter = Y_PIXELS_PER_METER;
    header.biClrUsed = COLORS_USED;
    header.biClrImportant = COLORS_IMPORTANT;

    return header;
}


/**
 * Reads a file, which should be a bmp and writes an image with the data form file
 * @param input - Opened file
 * @param image - Image to write on the read data
 * @return A read status
 */
enum read_status from_bmp(FILE* input, struct image** image){
    struct bmp_header header;

    if (fread(&header, sizeof(header), 1, input) != 1)
        return READ_INVALID_HEADER;

    if (header.bfType != HEX_SIGNATURE)
        return READ_INVALID_SIGNATURE;

    *image = create_image(header.biWidth, header.biHeight);
    if (!*image) {
        return READ_MEMORY_ALLOCATION_ERROR;
    }
    uint32_t padding = get_padding(*image);

    for (size_t i = 0; i < header.biHeight; i++) {
        if (fread(&(*image)->data[i * header.biWidth], sizeof(struct pixel), header.biWidth, input) != header.biWidth)
            return READ_INVALID_PIXEL_COUNT;
        if (fseek(input, (long)padding, SEEK_CUR) != 0)
            return READ_INVALID_BITS;
    }

    return READ_OK;

}

/**
 * Writes to a file with data from image
 * @param output - File to write on
 * @param image - Image from which data is read
 * @return A write status
 */
enum write_status to_bmp(FILE* output, struct image const* image) {
    struct bmp_header header = create_header(image);

    if (fwrite(&header, sizeof(header), 1, output) != 1)
        return WRITE_HEADER_ERROR;

    uint32_t padding = get_padding(image);

    for (size_t i = 0; i < image->height; i++) {
        if (fwrite(&image->data[i * image->width], sizeof(struct pixel), image->width, output) != image->width) {
            return WRITE_ERROR;
        }

        for (size_t p = 0; p < padding; p++) {
            if (fputc(0, output) == EOF) {
                return WRITE_ERROR;
            }
        }
    }

    return WRITE_OK;
}



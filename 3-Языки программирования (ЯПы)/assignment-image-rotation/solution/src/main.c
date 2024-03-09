#include "../include/bmp_io.h"
#include "../include/imageManager.h"
#include "../include/rotate.h"
#include <stdio.h>

int main( int argc, char** argv ) {
    (void) argc; (void) argv; // supress 'unused parameters' warning

    // check amount of arguments
    if (argc != 3) {
        fprintf(stderr,"Incorrect number of arguments\n");
        fprintf(stderr, "Write input.bmp and output.bmp, separated by 1 space\n");
        return 1;
    }

    //check if file is opened correctly
    FILE* input = fopen(argv[1], "rb");
    if (!input) {
        fprintf(stderr,"Error opening input file: %s\n", argv[1]);
        return 1;
    }

    // Read image from file
    struct image* image = NULL;
    enum read_status read_result = from_bmp(input, &image);
    fclose(input);

    if (read_result != READ_OK) {
        fprintf(stderr,"Error reading input file: %d\n", read_result);
        if (image) {
            destroy_image(image);
        }
        return 1;
    }

    // Rotate image
    struct image* rotated = rotate_right(image);
    if (!rotated) {
        fprintf(stderr,"Error rotating image\n");
        destroy_image(image);
        return 1;
    }


    // Open file for writing
    FILE* output = fopen(argv[2], "wb");
    if (!output) {
        fprintf(stderr,"Error opening output file: %s\n", argv[2]);
        destroy_image(image);
        destroy_image(rotated);
        return 1;
    }

    // Write image to file
    enum write_status write_result = to_bmp(output, rotated);
    fclose(output);

    if (write_result != WRITE_OK) {
        fprintf(stderr,"Error writing output file: %d\n", write_result);
        destroy_image(image);
        destroy_image(rotated);
        return 1;
    }

    // Free memory
    destroy_image(image);
    destroy_image(rotated);
    fprintf(stdout,"Freed memory from images\n");

    fprintf(stdout,"Success\n");
    return 0;

}

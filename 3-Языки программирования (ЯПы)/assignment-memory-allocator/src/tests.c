//
// Created by Gleb on 26/10/2023.
//

#include <stdio.h>
#include <assert.h>
#include "mem.h"
#include "mem_internals.h"
#include "tests.h"

size_t correct_count = 0;

static void print_test_name(const char* name, size_t number){
    printf("Test %zu: %s\n", number, name);
}

static void print_final_result(size_t correct, size_t total){
    printf("Correct tests: %zu/%zu\n", correct, total);
}

static void assert_memory_zero(void* ptr, size_t size) {
    for (size_t i = 0; i < size; ++i) {
        assert(((char*)ptr)[i] == 0);
    }
}

int test_basic_allocation_and_deallocation(void) {
    print_test_name("Basic allocation and deallocation", 1);

    size_t expected_size = 32;

    void* ptr = _malloc(expected_size);
    assert(ptr != NULL);

    assert_memory_zero(ptr, expected_size);

    _free(ptr);
    return 1;
}

int test_multiple_block_allocation_and_deallocation(void) {
    print_test_name("Allocation and deallocation of multiple blocks", 2);

    size_t expected_size_1 = 16;
    size_t expected_size_2 = 64;

    void* ptr1 = _malloc(expected_size_1);
    void* ptr2 = _malloc(expected_size_2);

    assert(ptr1 != NULL);
    assert(ptr2 != NULL);

    assert_memory_zero(ptr1, expected_size_1);
    assert_memory_zero(ptr2, expected_size_2);

    _free(ptr1);
    _free(ptr2);
    return 1;
}

int test_sequence_allocation_and_deallocation(void) {
    print_test_name("Allocate and deallocate in sequence", 3);

    size_t expected_size_1 = 20;
    size_t expected_size_2 = 40;
    size_t expected_size_3 = 80;

    void* ptr1 = _malloc(expected_size_1);
    void* ptr2 = _malloc(expected_size_2);
    void* ptr3 = _malloc(expected_size_3);

    assert(ptr1 != NULL);
    assert(ptr2 != NULL);
    assert(ptr3 != NULL);

    assert_memory_zero(ptr1, expected_size_1);
    assert_memory_zero(ptr2, expected_size_2);
    assert_memory_zero(ptr3, expected_size_3);

    _free(ptr1);
    _free(ptr2);
    _free(ptr3);

    return 1;
}

int test_allocate_deallocate_reallocate(void) {
    print_test_name("Allocate, deallocate, and reallocate", 4);

    size_t expected_size_1 = 30;
    size_t expected_size_2 = 50;

    void* ptr1 = _malloc(expected_size_1);
    assert(ptr1 != NULL);

    assert_memory_zero(ptr1, expected_size_1);

    _free(ptr1);

    void* ptr2 = _malloc(expected_size_2);
    assert(ptr2 != NULL);

    assert_memory_zero(ptr2, expected_size_2);

    _free(ptr2);

    return 1;
}

int test_allocate_large_block_split_deallocate(void) {
    print_test_name("Allocate large block, split, and deallocate", 5);

    size_t expected_size_1 = 100;
    size_t expected_size_2 = 50;
    size_t expected_size_3 = 50;
    size_t expected_size_4 = 40;

    void* ptr1 = _malloc(expected_size_1);
    assert(ptr1 != NULL);

    assert_memory_zero(ptr1, expected_size_1);

    _free(ptr1);

    void* ptr2 = _malloc(expected_size_2);
    assert(ptr2 != NULL);

    assert_memory_zero(ptr2, expected_size_2);

    void* ptr3 = _malloc(expected_size_3);
    assert(ptr3 != NULL);

    assert_memory_zero(ptr3, expected_size_3);

    _free(ptr2);

    void* ptr4 = _malloc(expected_size_4);
    assert(ptr4 != NULL);

    assert_memory_zero(ptr4, expected_size_4);

    _free(ptr3);
    _free(ptr4);

    return 1;
}

int test_allocate_block_larger_than_heap_init(void) {
    print_test_name("Allocate block larger than heap_init", 6);

    size_t expected_size = REGION_MIN_SIZE + 1;

    void* ptr1 = _malloc(expected_size);
    assert(ptr1 != NULL);

    assert_memory_zero(ptr1, expected_size);

    _free(ptr1);

    return 1;
}



void execute_tests(void) {
    heap_init(REGION_MIN_SIZE);

    correct_count += test_basic_allocation_and_deallocation();
    correct_count += test_multiple_block_allocation_and_deallocation();
    correct_count += test_sequence_allocation_and_deallocation();
    correct_count += test_allocate_deallocate_reallocate();
    correct_count += test_allocate_large_block_split_deallocate();
    correct_count += test_allocate_block_larger_than_heap_init();
    print_final_result(correct_count, 6);
}

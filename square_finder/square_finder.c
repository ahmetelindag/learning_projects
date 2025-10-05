// Square Number Finder
// Created by Ahmet 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to check and print square numbers in the array
void findSquares(int array[]) {
    for (int index = 0; index < 20; index++) { // Loop through each element
        for (int factor = 1; factor * factor <= array[index]; factor++) { // Check factors 
            if (array[index] == factor * factor) { // If number is a perfect square
                printf("%d. element of array %d is square of %d\n", index + 1, array[index], factor);
            }
        }
    }
}

int main() {
    srand(time(0)); // Seed the random number generator with current time

    int numbers[20]; // Array to store 20 random numbers

    // Generate 20 random numbers between 0 and 99
    for (int index = 0; index < 20; index++) {
        numbers[index] = rand() % 100;
    }

    // Print the generated array
    printf("Array: ");
    for (int index = 0; index < 20; index++) {
        printf("%d ", numbers[index]);
    }
    printf("\n");

    // Call function to find and print square numbers
    findSquares(numbers);

    return 0;
}

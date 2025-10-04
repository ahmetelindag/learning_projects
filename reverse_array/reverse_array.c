// Reverse Array Printer
// Created by Ahmet 

#include <stdio.h>

int main() {
    int n, i, arr1[15];
    int *pt;

    printf("\n\nReverse Array Printer:\n");
    printf("------------------------\n");

    printf("Enter the number of elements (maximum 15): ");
    scanf("%d", &n);
    if (n <= 0 || n > 15) {
        printf("Error: Number of elements must be between 1 and 15\n");
        return 1;
    }

    pt = &arr1[0];
    printf("Enter %d numbers:\n", n);
    for (i = 0; i < n; i++) {
        printf("Element - %d: ", i + 1);
        scanf("%d", pt);
        pt++;
    }

    pt = &arr1[n - 1];

    printf("\nArray elements in reverse order:\n");
    for (i = n; i > 0; i--) {
        printf("Element - %d: %d\n", i, *pt);
        pt--;
    }
    printf("\n");

    return 0;
}

// Triangle Calculator
// Created by Ahmet 

#include <stdio.h>

int main(void) {
    float a, b, c, height, area, perimeter;

    printf("Welcome to Triangle Calculator\n");
    printf("-----------------------------\n");

    printf("Enter the length of side a: ");
    scanf("%f", &a);
    if (a <= 0) {
        printf("Error: Side length must be positive!\n");
        return 1;
    }

    printf("Enter the length of side b: ");
    scanf("%f", &b);
    if (b <= 0) {
        printf("Error: Side length must be positive!\n");
        return 1;
    }

    printf("Enter the length of side c: ");
    scanf("%f", &c);
    if (c <= 0) {
        printf("Error: Side length must be positive!\n");
        return 1;
    }

    printf("Enter the height (perpendicular to base b): ");
    scanf("%f", &height);
    if (height <= 0) {
        printf("Error: Height must be positive!\n");
        return 1;
    }

    // Check if it can be a valid triangle
    if (a + b <= c || b + c <= a || a + c <= b) {
        printf("Error: These side lengths cannot form a triangle!\n");
        return 1;
    }

    // Calculate area using base b and height
    area = (b * height) / 2;
    // Calculate perimeter
    perimeter = a + b + c;

    printf("The area of the triangle is %.2f square units\n", area);
    printf("The perimeter of the triangle is %.2f units\n", perimeter);

    return 0;
}

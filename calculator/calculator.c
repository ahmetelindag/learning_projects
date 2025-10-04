// Calculator
// Created by Ahmet 

#include <stdio.h>

int main(void) {
    int choice;
    float number1, number2, result;

    printf("Welcome to The CALCULATOR\n");
    printf("-------------------------------\n");

    printf("Enter the first number: ");
    scanf("%f", &number1);

    printf("Enter the second number: ");
    scanf("%f", &number2);

    printf("Press 1 for addition\n");
    printf("Press 2 for multiplication\n");
    printf("Press 3 for division\n");
    printf("Press 4 for subtraction\n");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            result = number1 + number2;
            printf("Result = %.2f\n", result);
            break;
        case 2:
            result = number1 * number2;
            printf("Result = %.2f\n", result);
            break;
        case 3:
            if (number2 == 0) {
                printf("Error: Division by zero is not allowed!\n");
            } else {
                result = number1 / number2;
                printf("Result = %.2f\n", result);
            }
            break;
        case 4:
            result = number1 - number2;
            printf("Result = %.2f\n", result);
            break;
        default:
            printf("Wrong choice!!!\n");
            break;
    }

    return 0;
}

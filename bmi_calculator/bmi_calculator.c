// BMI Calculator
// Created by Ahmet

#include <stdio.h>

int main(void) {
    float height, weight, bmi;

    printf("Welcome to BMI Calculator App\n");
    printf("----------------------------\n");

    printf("Please enter your height in meters (e.g., 1.75): ");
    scanf("%f", &height);

    printf("Please enter your weight in kilograms (e.g., 70.5): ");
    scanf("%f", &weight);

    bmi = weight / (height * height);
    printf("Your Body Mass Index (BMI) is %.2f\n", bmi);

    if (bmi < 18.5) {
        printf("You are underweight\n");
    }
    else if (bmi >= 18.5 && bmi < 25.0) {
        printf("Your weight is normal\n");
    }
    else if (bmi >= 25.0 && bmi < 30.0) {
        printf("You are overweight\n");
    }
    else {
        printf("You are obese\n");
    }

    return 0;
} 

// Simple ATM Simulation
// Created by Ahmet on 24.10.2024

#include <stdio.h>

int main(void) {
    int total = 1000;
    int process, amount;

    printf("Welcome to AI Bank\n");
    printf("------------------\n");

    printf("Your money: %d\n", total);

    printf("1. Withdraw cash\n");
    printf("2. Deposit cash\n");
    printf("3. Refund card\n");
    printf("------------------\n");

    printf("Which operation do you want to perform? ");
    scanf("%d", &process);

    while (process != 3) {
        switch (process) {
            case 1:
                printf("Enter the amount you want to withdraw: ");
                scanf("%d", &amount);
                if (total < amount) {
                    printf("Amount cannot be withdrawn. Not enough balance.\n");
                } else {
                    total -= amount;
                    printf("Available money in your account: %d\n", total);
                }
                break;
            case 2:
                printf("Enter the amount you want to deposit: ");
                scanf("%d", &amount);
                total += amount;
                printf("Available money in your account: %d\n", total);
                break;
            default:
                printf("Invalid operation, please try again.\n");
                break;
        }
        printf("\nWhich operation do you want to perform next? ");
        scanf("%d", &process);
    }

    printf("** Please don't forget to take your card **\nThank you for using AI Bank\n");
    return 0;
}

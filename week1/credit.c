#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    long copy = number;

    int length = 0;
    while (copy > 0)
    {
        copy = copy / 10;
        length++;
    }

    copy = number;
    int sum = 0;
    int position = 0;

    while (copy > 0)
    {
        int digit = copy % 10;

        if (position % 2 == 1)
        {
            digit = digit * 2;
            sum += digit / 10;
            sum += digit % 10;
        }
        else
        {
            sum += digit;
        }

        copy = copy / 10;
        position++;
    }

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    long start = number;
    while (start >= 100)
    {
        start = start / 10;
    }

    if (length == 15 && (start == 34 || start == 37))
    {
        printf("AMEX\n");
    }
    else if (length == 16 && start >= 51 && start <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if ((length == 13 || length == 16) && start / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

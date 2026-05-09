#include "helpers.h"
#include <math.h>
#include <string.h>

int cap(int value)
{
    if (value > 255)
    {
        return 255;
    }

    return value;
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round(
                (image[i][j].rgbtRed +
                 image[i][j].rgbtGreen +
                 image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            image[i][j].rgbtRed = cap(sepiaRed);
            image[i][j].rgbtGreen = cap(sepiaGreen);
            image[i][j].rgbtBlue = cap(sepiaBlue);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    memcpy(copy, image, sizeof(RGBTRIPLE) * height * width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = 0;
            int green = 0;
            int blue = 0;
            int count = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        red += copy[ni][nj].rgbtRed;
                        green += copy[ni][nj].rgbtGreen;
                        blue += copy[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            image[i][j].rgbtRed = round(red / (float) count);
            image[i][j].rgbtGreen = round(green / (float) count);
            image[i][j].rgbtBlue = round(blue / (float) count);
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    memcpy(copy, image, sizeof(RGBTRIPLE) * height * width);

    int Gx[3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    int Gy[3][3] =
    {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
    };

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redX = 0, redY = 0;
            int greenX = 0, greenY = 0;
            int blueX = 0, blueY = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        int kernelX = Gx[di + 1][dj + 1];
                        int kernelY = Gy[di + 1][dj + 1];

                        redX += copy[ni][nj].rgbtRed * kernelX;
                        redY += copy[ni][nj].rgbtRed * kernelY;

                        greenX += copy[ni][nj].rgbtGreen * kernelX;
                        greenY += copy[ni][nj].rgbtGreen * kernelY;

                        blueX += copy[ni][nj].rgbtBlue * kernelX;
                        blueY += copy[ni][nj].rgbtBlue * kernelY;
                    }
                }
            }

            int finalRed = round(sqrt(redX * redX + redY * redY));
            int finalGreen = round(sqrt(greenX * greenX + greenY * greenY));
            int finalBlue = round(sqrt(blueX * blueX + blueY * blueY));

            image[i][j].rgbtRed = cap(finalRed);
            image[i][j].rgbtGreen = cap(finalGreen);
            image[i][j].rgbtBlue = cap(finalBlue);
        }
    }
}

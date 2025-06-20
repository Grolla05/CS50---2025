#include "helpers.h"
#include <math.h> // Necessário para a função round()

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Itera sobre cada linha da imagem
    for (int i = 0; i < height; i++)
    {
        // Itera sobre cada pixel da linha
        for (int j = 0; j < width; j++)
        {
            // Calcula a média dos valores de cor
            int average =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            // Define todos os canais de cor para o valor da média
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Itera sobre cada linha
    for (int i = 0; i < height; i++)
    {
        // Itera sobre cada pixel da linha
        for (int j = 0; j < width; j++)
        {
            // Armazena os valores de cor originais
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            // Calcula os novos valores de cor usando a fórmula Sépia
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            // Garante que os valores de cor não ultrapassem 255
            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Itera sobre cada linha
    for (int i = 0; i < height; i++)
    {
        // Itera sobre metade da largura da linha, trocando os pixels
        for (int j = 0; j < width / 2; j++)
        {
            // Usa uma variável temporária para guardar o pixel da esquerda
            RGBTRIPLE temp = image[i][j];
            // O pixel da esquerda se torna o da direita
            image[i][j] = image[i][width - 1 - j];
            // O pixel da direita se torna o antigo pixel da esquerda (guardado em temp)
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Cria uma cópia da imagem para ler os valores originais dos pixels
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Itera sobre cada pixel da imagem
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float totalRed = 0, totalGreen = 0, totalBlue = 0;
            int counter = 0;

            // Itera sobre a grade 3x3 de vizinhos
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int new_i = i + di;
                    int new_j = j + dj;

                    // Verifica se o pixel vizinho está dentro dos limites da imagem
                    if (new_i >= 0 && new_i < height && new_j >= 0 && new_j < width)
                    {
                        // Soma os valores de cor do pixel da cópia
                        totalRed += copy[new_i][new_j].rgbtRed;
                        totalGreen += copy[new_i][new_j].rgbtGreen;
                        totalBlue += copy[new_i][new_j].rgbtBlue;
                        counter++;
                    }
                }
            }

            // Calcula a média e atribui ao pixel da imagem original
            image[i][j].rgbtRed = round(totalRed / counter);
            image[i][j].rgbtGreen = round(totalGreen / counter);
            image[i][j].rgbtBlue = round(totalBlue / counter);
        }
    }
    return;
}

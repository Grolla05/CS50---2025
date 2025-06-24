#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have a name and a vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals for a new vote
bool vote(string name)
{
    // Percorre a lista de candidatos
    for (int i = 0; i < candidate_count; i++)
    {
        // Compara o nome do voto com o nome do candidato atual
        if (strcmp(candidates[i].name, name) == 0)
        {
            // Se encontrou, incrementa o voto e retorna sucesso (true)
            candidates[i].votes++;
            return true;
        }
    }
    // Se o loop terminar sem encontrar o candidato, o voto é inválido
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int max_votes = 0;

    // Passo 1: Encontrar o número máximo de votos
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > max_votes)
        {
            max_votes = candidates[i].votes;
        }
    }

    // Passo 2: Imprimir todos os candidatos com o número máximo de votos
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == max_votes)
        {
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}

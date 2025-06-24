#include <cs50.h>
#include <stdio.h>
#include <string.h> // Necessário para a função strcmp

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // Percorre a lista de candidatos para encontrar um com o nome correspondente
    for (int i = 0; i < candidate_count; i++)
    {
        // Se o nome do candidato for igual ao nome fornecido...
        if (strcmp(candidates[i].name, name) == 0)
        {
            // ...registra a preferência do eleitor, guardando o índice do candidato
            preferences[voter][rank] = i;
            return true; // Voto válido
        }
    }
    // Se o loop terminar e nenhum candidato com esse nome for encontrado, o voto é inválido
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // Percorre cada eleitor
    for (int i = 0; i < voter_count; i++)
    {
        // Para cada eleitor, percorre suas preferências (do rank 0 em diante)
        for (int j = 0; j < candidate_count; j++)
        {
            // Obtém o índice do candidato preferido
            int candidate_index = preferences[i][j];

            // Verifica se o candidato preferido NÃO foi eliminado
            if (!candidates[candidate_index].eliminated)
            {
                // Se não foi eliminado, adiciona um voto a ele
                candidates[candidate_index].votes++;
                // Para de verificar as preferências deste eleitor, pois seu voto já foi contado
                break;
            }
        }
    }
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // Calcula quantos votos são necessários para vencer (mais de 50%)
    int majority = voter_count / 2;

    // Percorre todos os candidatos
    for (int i = 0; i < candidate_count; i++)
    {
        // Se um candidato tiver mais votos que a maioria...
        if (candidates[i].votes > majority)
        {
            // ...imprime o nome dele como vencedor
            printf("%s\n", candidates[i].name);
            return true; // Retorna true, pois há um vencedor
        }
    }
    // Se o loop terminar e ninguém tiver a maioria, não há vencedor ainda
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // Inicia o valor mínimo com o maior número de votos possível
    int min_votes = voter_count;

    // Percorre todos os candidatos
    for (int i = 0; i < candidate_count; i++)
    {
        // Se o candidato NÃO foi eliminado E tem menos votos que o mínimo atual...
        if (!candidates[i].eliminated && candidates[i].votes < min_votes)
        {
            // ...atualiza o valor mínimo
            min_votes = candidates[i].votes;
        }
    }
    return min_votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    int remaining_candidates = 0;
    int candidates_with_min = 0;

    // Percorre todos os candidatos
    for (int i = 0; i < candidate_count; i++)
    {
        // Se o candidato NÃO foi eliminado...
        if (!candidates[i].eliminated)
        {
            // ...conta como um candidato restante
            remaining_candidates++;
            // Se ele também tiver o número mínimo de votos, conta-o
            if (candidates[i].votes == min)
            {
                candidates_with_min++;
            }
        }
    }

    // Se o número de candidatos restantes for igual ao número de candidatos com o mínimo de votos,
    // é um empate
    return remaining_candidates == candidates_with_min;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // Percorre todos os candidatos
    for (int i = 0; i < candidate_count; i++)
    {
        // Se o candidato NÃO foi eliminado E tem o número mínimo de votos...
        if (!candidates[i].eliminated && candidates[i].votes == min)
        {
            // ...ele é eliminado
            candidates[i].eliminated = true;
        }
    }
}

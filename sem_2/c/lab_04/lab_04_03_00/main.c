#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>

#define STRING_MAX_SIZE 256
#define WORD_MAX_SIZE 16

int string_input(char *s)
{
	int ch;
	size_t i = 0;

	while ((ch = getchar()) != '\n' && ch != EOF)
		if (i < STRING_MAX_SIZE)
			s[i++] = ch;
		else
			return EXIT_FAILURE;
	s[i] = '\0';

	return EXIT_SUCCESS;
}

size_t split(char *s, char arr_words[][WORD_MAX_SIZE + 1], size_t *arr_len, char *sep)
{
	size_t i = 0;
	size_t j;
	char *word = strtok(s, sep);
	
	while (word != NULL)
	{
		if (strlen(word) > 16)
			return EXIT_FAILURE;
		for (j = 0; *word != '\0'; j++)
		{
			arr_words[i][j] = *word;
			word++;
		}
		arr_words[i++][j] = '\0';
		word = strtok(NULL, sep);
	}
	if (i == 0)
		return EXIT_FAILURE;
	*arr_len = i;

	return EXIT_SUCCESS;
}

void copy_or_remove_letters(char *s, size_t *position, char *word)
{
	char first_letter = word[0];

	s[(*position)++] = first_letter;
	for (size_t i = 1; word[i] != '\0'; i++)
	{
		if (first_letter == word[i])
			continue;
		s[(*position)++] = word[i];
	}
	s[(*position)++] = ' ';	
}

void make_new_string(char *s, char arr_words[][WORD_MAX_SIZE + 1], size_t arr_len)
{
	size_t p = 0;
	
	for (size_t i = arr_len - 2; i < arr_len; i--)
		if (strcmp(arr_words[arr_len - 1], arr_words[i]) != 0)
			copy_or_remove_letters(s, &p, arr_words[i]);
	s[p] = '\0';
}



int main(void)
{
	char sep[] = " ,;:-.!?";
	char s[STRING_MAX_SIZE + 1];

	if (string_input(s) != EXIT_SUCCESS)
		return EXIT_FAILURE;

	char arr_words[STRING_MAX_SIZE / 2 + 1][WORD_MAX_SIZE + 1];
	size_t arr_len;

	if (split(s, arr_words, &arr_len, sep) != EXIT_SUCCESS)
		return EXIT_FAILURE;

	char new_s[STRING_MAX_SIZE + 1];

	make_new_string(new_s, arr_words, arr_len);

	if (strlen(new_s) == 0)
		return EXIT_FAILURE;
	
	printf("Result: %s\n", new_s);

	return EXIT_SUCCESS;
}

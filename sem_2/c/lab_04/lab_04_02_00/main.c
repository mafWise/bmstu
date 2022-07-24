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
	if (i == 0)
		return EXIT_FAILURE;
	s[i] = '\0';

	return EXIT_SUCCESS;
}

size_t split(char *s, char words[][WORD_MAX_SIZE + 1], size_t *arr_len, char *sep)
{
	size_t j = 0;
	size_t z = 0;
	int counter = 0;

	for (size_t i = 0; s[i] != '\0'; i++)
	{
		if (strchr(sep, s[i]) == NULL) 
		{
			words[j][z++] = s[i];
			counter++;
			if (counter > WORD_MAX_SIZE)
				return EXIT_FAILURE;
		}
		else
		{
			if (counter == 0)
				continue;
			words[j++][z] = '\0';
			z = 0;
			counter = 0;
		}
	}	
	if (counter != 0)
		words[j++][z] = '\0';
	if (j == 0)
		return EXIT_FAILURE;
	*arr_len = j;

	return EXIT_SUCCESS;
}

void string_output(char *s, char arr[][WORD_MAX_SIZE + 1], size_t arr_len)
{
	int count = 0;
	char *tmp;

	for (size_t i = 0; i < arr_len; i++)
	{	
		tmp = s;
		while ((tmp = strstr(tmp, arr[i])) != NULL)
			count++;
		printf("\n%s %d", arr[i], count);
	}
}

void find_unique(char arr[][WORD_MAX_SIZE + 1], size_t arr_len, 
char arr_unique[][WORD_MAX_SIZE + 1], size_t *arr_len_unique)
{
	int flag;

	for (size_t i = 0; i < arr_len; i++)
	{
		flag = 0;	
		for (size_t j = 0; j < *arr_len_unique; j++)
			if (strcmp(arr[i], arr_unique[j]) == 0)
				flag = 1;

		if (flag == 0)
			strcpy(arr_unique[(*arr_len_unique)++], arr[i]);
	}	
}	

void count_of_substring(char arr[][WORD_MAX_SIZE + 1], size_t arr_len, 
char arr_unique[][WORD_MAX_SIZE + 1], size_t arr_len_unique, int arr_count[])
{
	for (size_t i = 0; i < arr_len_unique; i++)
	{
		int counter = 0;

		for (size_t j = 0; j < arr_len; j++)
			if (strcmp(arr[j], arr_unique[i]) == 0)
				counter++;
		
		arr_count[i] = counter;
	}
}

void print_word_and_count(char arr_unique[][WORD_MAX_SIZE + 1], size_t arr_len_unique, int arr_count[])
{
	for (size_t i = 0; i < arr_len_unique; i++)
		printf("\n%s %d", arr_unique[i], arr_count[i]);
}


int main(void)
{
	char sep[] = " ,;:-.!?";
	char s[STRING_MAX_SIZE + 1];
	
	if (string_input(s) != EXIT_SUCCESS)
		return EXIT_FAILURE;

	size_t arr_len;
	char arr[STRING_MAX_SIZE / 2 + 1][WORD_MAX_SIZE + 1];

	if (split(s, arr, &arr_len, sep) != EXIT_SUCCESS)
		return EXIT_FAILURE;

	size_t arr_len_unique = 0;
	char arr_unique[STRING_MAX_SIZE / 2 + 1][WORD_MAX_SIZE + 1];

	find_unique(arr, arr_len, arr_unique, &arr_len_unique);

	int arr_count[STRING_MAX_SIZE / 2 + 1];

	count_of_substring(arr, arr_len, arr_unique, arr_len_unique, arr_count);
	printf("Result: ");
	print_word_and_count(arr_unique, arr_len_unique, arr_count);	

	return EXIT_SUCCESS;
}

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

int len(int a)
{
	int counter = 0;

	if (a == 0)
		return 1;

	while (a > 0)
	{
		a /= 10;
		counter++;
	}

	return counter;
}

int my_strlen(char *s)
{
	int counter = 0;
	int flag = 0;
	size_t i;

	for (i = 0; s[i] != '\0'; i++)
		if (s[i] != '0' || flag == 1)
		{
			flag = 1;
			counter++;
		}

	if (counter == 0 && s[i - 1] == '0')
		return 1;

	return counter;
}

int quantity_of_symbol(char *s, char symbol)
{
	int counter = 0;

	for (size_t i = 0; s[i] != 0; i++)
		if (s[i] == symbol)
			counter++;

	return counter;
}	

int is_ip(char *s, char arr[][WORD_MAX_SIZE + 1], size_t arr_len)
{
	int counter = 0;
	int temp;

	if (quantity_of_symbol(s, '.') > 3)
		return EXIT_FAILURE;

	for (size_t i = 0; i < arr_len; i++)
	{
		if (strlen(arr[i]) > 3)
			return EXIT_FAILURE;
			
		temp = atoi(arr[i]);

		//т.к. atoi возвращает ноль при нахождении иного символа раньше цифры, то проверяем ноль отдельно 
		if (temp <= 255 && (temp > 0 || arr[i][0] == '0') && len(temp) == my_strlen(arr[i]))
			counter++;
		else
			counter = 0;
		if (counter == 4)
			return EXIT_SUCCESS;
	}

	return EXIT_FAILURE;
}

void split(char *s, char arr[][WORD_MAX_SIZE + 1], size_t *arr_len, char *sep)
{
	size_t j = 0;
	size_t z = 0;
	int counter = 0;

	for (size_t i = 0; s[i] != '\0'; i++)
	{
		if (s[i] == ' ' || s[i] == '\t')
			continue;
		if (strchr(sep, s[i]) == NULL) 
		{
			arr[j][z++] = s[i];
			counter++;
		}
		else
		{
			arr[j++][z] = '\0';
			z = 0;
			counter = 0;
		}
	}	
	if (counter != 0)
		arr[j++][z] = '\0';

	*arr_len = j;
}

int main(void)
{
	char sep[] = ".";
	char s[STRING_MAX_SIZE + 1];

	if (string_input(s) != EXIT_SUCCESS)
		return EXIT_FAILURE;

	char arr[STRING_MAX_SIZE / 2 + 1][WORD_MAX_SIZE + 1];
	size_t arr_len;

	split(s, arr, &arr_len, sep);

	if (is_ip(s, arr, arr_len) != EXIT_SUCCESS)
		printf("NO");
	else	
		printf("YES");

	return EXIT_SUCCESS;
}


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t my_strcspn(char *s1, char *s2)
{
	size_t i;

	for (i = 0; s1[i] != '\0'; i++)
		for (size_t j = 0; s2[j] != '\0'; j++)
			if (s2[j] == s1[i])
				return i;
	
	return i;	
}

int test1(void)
{
	char s1[] = "Hello, world!";
	char s2[] = "abcd";

	if (my_strcspn(s1, s2) == strcspn(s1, s2))
		return EXIT_SUCCESS;
	
	return EXIT_FAILURE;
}

int test2(void)
{
	char s1[] = "Hello, world!";
	char s2[] = "e";

	if (my_strcspn(s1, s2) == strcspn(s1, s2))
		return EXIT_SUCCESS;
	
	return EXIT_FAILURE;
}

int test3(void)
{
	char s1[] = "Hello, world!";
	char s2[] = "";


	if (my_strcspn(s1, s2) == strcspn(s1, s2))
		return EXIT_SUCCESS;
	
	return EXIT_FAILURE;
}

int test4(void)
{
	char s1[] = "";
	char s2[] = "abcd";

	if (my_strcspn(s1, s2) == strcspn(s1, s2))
		return EXIT_SUCCESS;
		
	return EXIT_FAILURE;
}

int test5(void)
{
	char s1[] = "x";
	char s2[] = "y";

	if (my_strcspn(s1, s2) == strcspn(s1, s2))
		return EXIT_SUCCESS;
	
	return EXIT_FAILURE;
}

int test6(void)
{
	char s1[] = "";
	char s2[] = "";

	if (my_strcspn(s1, s2) == strcspn(s1, s2))
		return EXIT_SUCCESS;

	return EXIT_FAILURE;
}

int main(void)
{
	int falls = 0;
	
	if (test1() != EXIT_SUCCESS)
		falls++;
	if (test2() != EXIT_SUCCESS)
		falls++;
	if (test3() != EXIT_SUCCESS)
		falls++;
	if (test4() != EXIT_SUCCESS)
		falls++;
	if (test5() != EXIT_SUCCESS)
		falls++;
	if (test6() != EXIT_SUCCESS)
		falls++;

	printf("%d", falls);

	return falls;
}

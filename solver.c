#include <stdio.h>
#include <stdlib.h>

int main()
{
	int c;
	FILE *file;
	file = fopen("wordList.txt", "r");
	if (file) {
		while ((c = getc(file)) != EOF)
			putchar(c);
		fclose(file);
	}
}

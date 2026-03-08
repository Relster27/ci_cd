#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
        char buf[16];
        printf("> ");
        gets(buf);

        return EXIT_SUCCESS;
}

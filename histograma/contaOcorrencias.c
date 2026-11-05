#include <stdio.h>

//Daniel Dezerto Rimes

// stdout, stdin, stderr
 
int main(int argc, char** argv)

{

	FILE *entrada;

	int c;

	int i = 0;

    int gt[256] = {0};
 
	if(argc != 2)

	{

		fprintf(stderr,"Erro na chamada do comando.\n");

		fprintf(stderr,"Uso: %s [ARQUIVO ORIGEM].\n", argv[0]);

		return 1;

	}
 
	entrada = fopen(argv[1],"rb");

	if(!entrada)

	{

		fprintf(stderr,"Arquivo %s não pode ser aberto para leitura\n", argv[1]);

		return 1;

	}
 
	c = fgetc(entrada);

    while(c != EOF){

        gt[c]++;

        c = fgetc(entrada);

	}

	while(i<256){

        printf("\n %c se repete %d vezes", i, gt[i]);

        i++;

    }
 
	fclose(entrada);

	return 0;

}
 
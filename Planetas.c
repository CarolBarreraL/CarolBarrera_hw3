#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define G 39.4783

float get_gravedad(float masa);


/*int main(void){
	//int t = 10;
	//print_algo(t);	
	FILE *in;
	char Dataplaneta[10];
	float masa, px, py, pz, velx, vely, velz;
	int i;
	char filename[100]="coordinates.csv";
	//char *token_Dataplaneta;
	//constant char delimiter;
	//delimiter =',';
	in = fopen(filename, "r");
	for(i=0;i<10;i++){
	
		fscanf(in, " %s, %f, %f, %f, %f, %f, %f, %f\n", &Dataplaneta, &masa, &px, &py, &pz, &velx, &vely, &velz);
		printf("value = %s\n",Dataplaneta);

		//token_Dataplaneta = strtok(Dataplaneta, delimiter); 

		/*while(token_Dataplaneta != NULL)
		{
			printf("%s\n", token_Dataplaneta);
			token_Dataplaneta = strtok(NULL, delimiter);
		}*/
		
	//}
	//fclose(in);
	//return 0;
	//}*/

int main(void){
	//int t = 10;
	//print_algo(t);	
	FILE *in;
	float masa, px, py, pz, velx, vely, velz;
	int i;
	char filename[100]="coordinatesMODIFICADO.csv";
	in = fopen(filename, "r");
	for(i=0;i<10;i++){
	
		fscanf(in, " %f, %f, %f, %f, %f, %f, %f\n", &masa, &px, &py, &pz, &velx, &vely, &velz);
		printf("value = %f\n",px);

	}
	fclose(in);
	return 0;
	}









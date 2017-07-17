#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define G 39.4784176044

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
	float masa[10];
	float px[10];
	float py[10];
	float pz[10];
	float vx[10];
	float vy[10];
	float vz[10];
	int tiempo = 1000;
	//Para pedir memoria para las listas y matrices
	float *velmedx = malloc(10*sizeof(float));
	float *velmedy = malloc(10*sizeof(float));
	float *velmedz = malloc(10*sizeof(float));
	float *Posx = malloc(10*tiempo*sizeof(float));
	float *Posy = malloc(10*tiempo*sizeof(float));
	float *Posz = malloc(10*tiempo*sizeof(float));
	float *Velx = malloc(10*tiempo*sizeof(float));
	float *Vely = malloc(10*tiempo*sizeof(float));
	float *Velz = malloc(10*tiempo*sizeof(float));
	int i;
	char filename[100]="coordinatesMODIFICADO.csv";
	in = fopen(filename, "r");
	for(i=0;i<10;i++){
	
		fscanf(in, " %e, %e, %e, %e, %e, %e, %e\n", &masa[i], &Posx[i], &Posy[i], &Posz[i], &Velx[i], &Vely[i], &Velz[i]);

	}
	
	fclose(in);

	return 0;
	}


int ind(i,j)
{
	int num;
	num = 10*i + j;
	return num;
}

float Acelereadeje(i,j,m):






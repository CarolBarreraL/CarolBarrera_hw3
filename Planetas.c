#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4784176044
#define t 10000


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
	int t;
	int p;
	float dt = 0.001;
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
	
		fscanf(in, " %f, %f, %f, %f, %f, %f, %f\n", &masa[i], &Posx[i], &Posy[i], &Posz[i], &Velx[i], &Vely[i], &Velz[i]);

	}
	fclose(in);
	
	float *Ax = malloc(10*tiempo*sizeof(float));
	float *Ay = malloc(10*tiempo*sizeof(float));
	float *Az = malloc(10*tiempo*sizeof(float));

	for(p=0;p<10;p++)
	{
		Ax[ind(p,0)]= Acelereadeje(p,0,masa[ind(p,0)], Posx[ind(p,0)], Posy[ind(p,0)], Posz[ind(p,0)]);
		Ay[ind(p,0)]= Acelereadeje(p,0,masa[ind(p,0)], Posy[ind(p,0)], Posx[ind(p,0)], Posz[ind(p,0)]);
		Az[ind(p,0)]= Acelereadeje(p,0,masa[ind(p,0)], Posz[ind(p,0)], Posx[ind(p,0)], Posy[ind(p,0)]);
		printf("Aceleracion=%f\n", Ax[ind(1,0)]);
	}


	//for(t=1;t<tiempo;t++)
	//{	
		/*Iniciales*/
	//	for(p=0;p<10;p++)
	//	{
	//		Acelereadeje(p,t,masa[ind(p,t)], Posx[ind(p,t)], Posy[ind(p,t)],Posz[ind(p,t)]);
	//	}
	//	for(p=0;p<10;p++)
	//	{
			
	//	}

	//}

	return 0;
	}


int ind(i,j)
{
	int num;
	num = t*i + j;
	return num;
}


float Acelereadeje(int i, int j,float *m, float *midim, float *otra, float *ootra)
{
	int ii;
	float sum=0;
	float r;
	
	for(ii=0;ii<10;ii++){
		
		r = pow((pow((midim[ind(i,j)]-midim[ind(ii,j)]),2.0) + pow((otra[ind(i,j)]-otra[ind(ii,j)]),2.0) + pow((ootra[ind(i,j)]-ootra[ind(ii,j)]),2.0)),1.5);
		if(ii!=i){
			sum += G*m[ind(ii,j)]*(midim[ind(i,j)]-midim[ind(ii,j)])/r;
		}
	}
	return sum;
}



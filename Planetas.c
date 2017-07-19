#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4784176044
#define time 3120 /*Tiempo teniendo mi dt en meses y para calcular 260 años*/

float Acelereadeje(int i, int j,float *m, float *midim, float *otra, float *ootra);
int ind(int i, int j );

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
	FILE *in;
	int t;
	int p;
	int i;
	float dt = 0.0833333333;
	
	//Para pedir memoria para las listas y 'matrices'
	float masa[10];
	float *velmedx = malloc(10*sizeof(float));
	float *velmedy = malloc(10*sizeof(float));
	float *velmedz = malloc(10*sizeof(float));
	float *Posx = malloc(10*time*sizeof(float));
	float *Posy = malloc(10*time*sizeof(float));
	float *Posz = malloc(10*time*sizeof(float));
	float *Velx = malloc(10*time*sizeof(float));
	float *Vely = malloc(10*time*sizeof(float));
	float *Velz = malloc(10*time*sizeof(float));


	/*Lectura del archivo y guardar datos*/
	char filename[100]="coordinatesMODIFICADO.csv";
	in = fopen(filename, "r");
	for(i=0;i<10;i++){
	
		fscanf(in, " %f, %f, %f, %f, %f, %f, %f\n", &masa[i], &Posx[i], &Posy[i], &Posz[i], &Velx[i], &Vely[i], &Velz[i]);
		printf("pos=%f\n", masa[i]);

	}
	fclose(in);



	/*Cambio de unidades de la masa*/
	for(i=0;i<10;i++){
		float conv = 1.9891e30;
		masa[i]= masa[i]/conv;
	}
	
	float *Ax = malloc(10*sizeof(float));
	float *Ay = malloc(10*sizeof(float));
	float *Az = malloc(10*sizeof(float));

	for(p=0;p<10;p++){
		Ax[p]= Acelereadeje(p,0,masa, Posx, Posy, Posz);
		Ay[p]= Acelereadeje(p,0,masa, Posy, Posx, Posz);
		Az[p]= Acelereadeje(p,0,masa, Posz, Posx, Posy);
	}




	for(t=1;t<tiempo;t++)
	{	
		for(p=0;p<10;p++)
		{
			velmedx[p]= Velx[ind(p,t-1)]+ 0.5*Ax[p]*dt
		}

	}

	return 0;
	}


int ind(int i, int t ){
	int num;
	num = t*10 + i;
	return num;
}



float Acelereadeje(int i, int j,float *m, float *midim, float *otra, float *ootra){
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



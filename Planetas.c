#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
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
	int tiempo = 1000;
	int t;
	int p;
	float dt = 0.01;
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
	
	for(t=0;t<tiempo;t++)
	{
		for(p=0;p<10;p++)
		{
			
		}
	}

	return 0;
	}


int ind(i,j)
{
	int num;
	num = 10*i + j;
	return num;
}


float Acelereadex(int i, int j,float m, float *x, float *y, float *z)
{
	int ii;
	float sum=0;
	float r;
	
	for(ii=0;ii<10;ii++){
		
		r = pow((pow((x[ind(i,j)]-x[ind(ii,j)]),2.0) + pow((y[ind(i,j)]-y[ind(ii,j)]),2.0) + pow((z[ind(i,j)]-z[ind(ii,j)]),2.0)),1.5);
		if(ii!=i){
			sum += G*m[ind(ii,j)]*(x[ind(i,j)]-x[ind(ii,j)])/r;
		}
	}
	return sum;
}

float Acelereadey(int i, int j,float m, float *x, float *y, float *z)
{
	int ii;
	float sum=0;
	float r;
	
	for(ii=0;ii<10;ii++){
		
		r = pow((pow((x[ind(i,j)]-x[ind(ii,j)]),2.0) + pow((y[ind(i,j)]-y[ind(ii,j)]),2.0) + pow((z[ind(i,j)]-z[ind(ii,j)]),2.0)),1.5);
		if(ii!=i){
			sum += G*m[ind(ii,j)]*(y[ind(i,j)]-y[ind(ii,j)])/r;
		}
	}
	return sum;
}

float Acelereadez(int i, int j,float m, float *x, float *y, float *z)
{
	int ii;
	float sum=0;
	float r;
	
	for(ii=0;ii<10;ii++){
		
		r = pow((pow((x[ind(i,j)]-x[ind(ii,j)]),2.0) + pow((y[ind(i,j)]-y[ind(ii,j)]),2.0) + pow((z[ind(i,j)]-z[ind(ii,j)]),2.0)),1.5);
		if(ii!=i){
			sum += G*m[ind(ii,j)]*(z[ind(i,j)]-z[ind(ii,j)])/r;
		}
	}
	return sum;
}







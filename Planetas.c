#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4784176044
#define time 26000 /*Tiempo teniendo dependiendo de mi dt*/

float Acelereadeje(int i, int j,float *m, float *midim, float *otra, float *ootra);
int ind(int i, int j );


int main(void)
{
	FILE *in;
	int m = 0;
	int t;
	int p;
	int i;
	float dt = 0.01;
	
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
	int n = 200;
	char planetas[n];
	char *token=NULL;
	const char *delim;
	delim = ",";
	int item =0;
	float val;
	char filename[100]="coordinates.csv";
	in = fopen(filename, "r");
	while(fgets(planetas, n, in))
	{
		token = strtok(planetas, delim);
		
			while(token!=NULL)
			{
				val = atof(token);
				if(item==1){masa[m]=val;}
				else if(item==2){Posx[m]=val;}
				else if(item==3){Posy[m]=val;}	
				else if(item==4){Posz[m]=val;}
				else if(item==5){Velx[m]=val;}
				else if(item==5){Vely[m]=val;}
				else if(item==5){Velz[m]=val;}
				token = strtok(NULL,delim);
				item ++;
			}
			item=0;	
			m++;
	}
	fclose(in);


	/*Cambio de unidades de la masa*/
	for(i=0;i<10;i++){
		float conv = 1.9891E30;
		masa[i]= masa[i]/conv;
	}

	
	/*Metodo de LeapFrog*/
	for(t=1;t<time;t++)
	{	
		for(p=0;p<10;p++)
		{
			velmedx[p]= Velx[ind(p,t-1)]+ 0.5*Acelereadeje(p,t-1,masa, Posx, Posy, Posz)*dt;
			velmedy[p]= Velx[ind(p,t-1)]+ 0.5*Acelereadeje(p,t-1,masa, Posy, Posx, Posz)*dt;
			velmedz[p]= Velx[ind(p,t-1)]+ 0.5*Acelereadeje(p,t-1,masa, Posz, Posx, Posy)*dt;

			Posx[ind(p,t)]= Posx[ind(p,t-1)]+ velmedx[p]*dt;
			Posy[ind(p,t)]= Posy[ind(p,t-1)]+ velmedy[p]*dt;
			Posz[ind(p,t)]= Posz[ind(p,t-1)]+ velmedz[p]*dt;
			
		}
		for(p=0;p<10;p++)
		{
			Velx[ind(p,t)]= velmedx[p] + 0.5*Acelereadeje(p,t,masa, Posx, Posy, Posz)*dt;
			Vely[ind(p,t)]= velmedy[p] + 0.5*Acelereadeje(p,t,masa, Posy, Posx, Posz)*dt;
			Velz[ind(p,t)]= velmedz[p] + 0.5*Acelereadeje(p,t,masa, Posz, Posx, Posy)*dt;
		}

	}

	for(t=0;t<time;t++){
		printf("%f,%f,%f\n", Posx[t], Posy[t], Posz[t]);
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
	double r;
	for(ii=0;ii<10;ii++){
		
		r = pow((midim[ind(i,j)]-midim[ind(ii,j)]),2.0) + pow((otra[ind(i,j)]-otra[ind(ii,j)]),2.0) + pow((ootra[ind(i,j)]-ootra[ind(ii,j)]),2.0);

		if(ii!=i){
			sum += G*m[ii]*(midim[ind(ii,j)]-midim[ind(i,j)])/pow(r,1.5);
		}
	}
	return sum;
}



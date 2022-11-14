/*********************************************************
Escriba un programa en C donde se definan tres variables,
 x, y, z, tal que a las variables x e y se les asigne un
 valor (por ejemplo, 2 y 5) y se guarde el resultado de
 una operación en z. En pantalla se debe mostrar el
 resultado en z para las siguientes operaciones:
x + y
x - y
x * y
x / y
Ayuda: los operadores anteriores son los mismos que en python.
Repita la operación pero ahora suponga que y es siempre
el número pi.
**********************************************************/
/*
#include <stdio.h>
short x = 500, y = 500, z1, z2, z4;
int z3;
// float z4;

int main(void)
{
    z1 = x + y;
    z2 = x - y;  //-500-500
    z3 = x * y;  //500*500 =250000>32767(short)
    z4 = x / y; // 500/1
    // z4 = (float) x / y;
    printf("%hi+%hi = %hi,\
    \n%hi-%hi = %hi,\
    \n%hi*%hi = %i,\
    \n%hi/%hi = %hi\n",\
    x, y, z1, x, y, z2, x, y, z3, x, y, z4);
    return 0;
}
*/
/**************************EJ2**************************
Escriba un programa en C que utilice el código del ejercicio anterior 
para decidir qué operación quiere mostrarse en pantalla. Esto requiere 
que se defina una variable op a la cual se le debe asignar un valor 
que permita elegir la operación deseada. Se sugieren las opciones 
0, 1, 2 y 3.
El programa debe seguir la siguiente lógica:
Asignaciones de op, x e y
Elegir tipo de operación según op y mostrar el contenido de la 
variable z
**********************************************************/
/*
#include <stdio.h>
#define PI 3.141516

int main(void){
    short x = 500, y = 500;
    // float y = PI;
    int z;
    char c = '/', opc = 2;

    if(opc == 1){
    z = x + y;
    c = '+';
    }
    else if(opc == 2){
    z = x - y;
    c = '-';
    }
    else if (opc == 3){
    z = x * y;
    c = '*';
    }
    else{
    z = x / y;
    }    
    printf("%hi %c %hi = %i\n",x,c,y,z);
    return 0;
}
*/

/**************************EJ3**************************
Escriba un programa que convierta un caracter de minusculas 
a mayusculas o viceversa  y lo imprima en pantalla. Para 
ello suponga que el caracter se guarda en la variable a 
previamente. En caso que el caracter no corresponda a un 
símbolo alfabético, debe imprimir el mismo sin modificaciones.
**********************************************************/
/*
#include <stdio.h>
#define OFFSET 32
#define A 65  //'A'
#define Z 90  // 'Z'

int main(void){
    char c = 'a';

    if(A <= c && c <= Z){ //mayusculas
        c += OFFSET;
    }
    else if(A + OFFSET <= c && c <= Z + OFFSET){ //minusculas
        c -= OFFSET;
    }
    printf("%c\n",c);
    return 0;
}
*/
/**************************EJ4**************************
Sean dos puntos que se encuentran en las posiciones de 
coordenadas (x1,y1) y (x2,y2), como se muestra en la 
figura. Escriba un programa que defina cada posición 
con un array de largo 2 (primer elemento x, segundo 
elemento y) y determine la distancia entre ambos puntos.
Luego debe mostrarse en pantalla cual punto es el mas cercano y 
la distancia resultante.
Ayuda: d = raiz( (x1-x2)^2 + (y1-y2)^2 ) 
  
  
EN ESTE EJERCICIO HAY QUE AGREGAR AL FINAL: -lm
gcc -Wall -std=c1x -o clasesC27 claseC27.c -lm
**********************************************************/
#include <stdio.h>
#include <math.h>

int main(void){
    double dist1 = 0, dist2 = 0;
    double p0[] = {0,0}, p1[] = {1,0}, p2[] = {0,2};
    
    dist1 = sqrt(pow(p0[0]-p1[0],2) + pow(p0[1]-p1[1],2));
    dist2 = sqrt(pow(p0[0]-p2[0],2) + pow(p0[1]-p2[1],2));

    if(dist1<dist2){
        printf("La distancia mas corta es al punto (%.2f,%.2f) y es de %.2f m\n",p1[0],p1[1],dist1);
    }
    else{
        printf("La distancia mas corta es al punto (%.2f,%.2f) y es de %.2f m\n",p2[0],p2[1],dist2);
    }
    return 0;
}

/*
int main(void){
    double dist1 = 0, dist2 = 0;
    double p0x = 0,p0y = 0;
    double p1x = 3,p1y= 0;
    double p2x = 0,p2y = 2;

    dist1 = sqrt(pow(p0x-p1x,2) + pow(p0y-p1y,2));
    dist2 = sqrt(pow(p0x-p2x,2) + pow(p0y-p2y,2));

    if(dist1<dist2){
        printf("La distancia mas corta es al punto (%.2f,%.2f) y es de %.2f m\n",p1x,p1y,dist1);
    }
    else{
        printf("La distancia mas corta es al punto (%.2f,%.2f) y es de %.2f m\n",p2x,p2y,dist2);
    }
    return 0;
}
*/
/*
// 1 ******************************
#include <stdio.h>
#include <math.h>

int main()
{

float v1[] = {1,2,3,4};
 float v2[] = {5,6,7,8};
 float p;
 p = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]+v1[3]*v2[3];
 printf("v1=[%.2f, %.2f, %.2f, %.2f]\n", v1[0],v1[1],v1[2],v1[3] );
 printf("v2=[%.2f, %.2f, %.2f, %.2f]\n", v2[0],v2[1],v2[2],v2[3] );
 printf("Producto interno: p=<v1,v2>=%.2f\n", p);
 return 0;

}

// 2 *******************************************

#include <stdio.h>
#include <math.h>

int main()
{
 float v[] = {5,6,7,8};
 float nor = 0, p=0;
 p = v[0]*v[0]+v[1]*v[1]+v[2]*v[2]+v[3]*v[3];
 nor = sqrt(p);
 printf("v=[%.2f, %.2f, %.2f, %.2f]\n", v[0],v[1],v[2],v[3] );
 printf("Norma de v: ||v||=%.2f\n", nor);
 return 0;
}


// 3 *********************************************
#include <stdio.h>
#include <math.h>

int main()
{
 float v[] = {5,6,7,8}, vn[4];
 float nor = 0, p=0;
 p = v[0]*v[0]+v[1]*v[1]+v[2]*v[2]+v[3]*v[3];
 nor = sqrt(p);
 vn[0]=v[0]/nor;
 vn[1]=v[1]/nor;
 vn[2]=v[2]/nor;
 vn[3]=v[3]/nor;
 printf("Vector original:\nv=[%.2f, %.2f, %.2f, %.2f]\n", v[0],v[1],v[2],v[3] );
 printf("Vector normalizado:\nvn=[%.2f, %.2f, %.2f, %.2f]\n", vn[0],vn[1],vn[2],vn[3] );

 return 0;
 
}
*/
//***********************************************************************************
/*
#include <stdio.h>
#include <math.h>
#define PI 3.141592653
int main()
{
float r = 3, h = 4, res;
int opc=1;
 
float d = 2 * r; // diametro
float c = PI*d; // circunsferencua
float a = PI*pow(r,2); // area base
float v = a*h; // volumen
float ac = a + c*h; // area cil

if (opc==0){ 
    res = d;
 }
 else if (opc==1){
   res = c;   
 }
  else if (opc==2){
res = a;
 }
  else if (opc==3){
     res = v;
 }
  else if (opc==4){
     res = ac;
 }
 else {
 printf("La opción no es válida\n");
 return 0;
 }
 printf("Resultado: %.2f\n", res);
 return 0;
 
}
*/

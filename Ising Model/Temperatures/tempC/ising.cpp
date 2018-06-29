#include<iostream>
#include<vector>
#include<cmath>
#include<fstream>
#include<cstdlib>
const int Nx=100;
const int Ny=100;
const int N=1000;
const double J=1.;
const double h=0.1;
typedef std::vector<std::vector<double> > matrix;
void get_mem(matrix & m);
void print(matrix & m);
void Time_Step(matrix & m,const double kbT);
void print_file(const char * NameArch, matrix & M);
double calculate_Mag(const matrix & m);
int main(int argc, char * argv[]){
  const double kbT=atof(argv[1]);
  srand(1);
  matrix ising;
  get_mem(ising);
  int Number=Nx*Ny;
  
  std::ofstream File(argv[1]);
  File.precision(16);
  
  for (int t=0;t<N*Number;t++){
    Time_Step(ising,kbT);
    if(t%Number==0){
      File<<calculate_Mag(ising)<<std::endl;
    }
  }
  File.close();
  //print_file(argv[1],ising);
  return 0;
}
double calculate_Mag(const matrix & m){
double mag=0;
  for(int x=0;x<Nx;x++){
    for(int y=0;y<Ny;y++){
	mag+=m[x][y];
	}
}
return mag/(Nx*Ny);
}


void get_mem(matrix & m){
  m.resize(Nx);
  for(int i=0;i<Nx;i++){
    m[i].resize(Ny);
    for(int j=0;j<Ny;j++){
      m[i][j]=2*(rand() % 2)-1;
    }
  }
}

void print(matrix & m){
 for(int i=0;i<Nx;i++){
    for(int j=0;j<Ny;j++){
      std::cout<<m[i][j]<<' ';
    }
    std::cout<<std::endl;
  }

}
void print_file(const char * NameArch, matrix & M)
{
  std::ofstream File(NameArch);
  File.precision(16);
  for( int x = 0; x < Nx; ++x )
    {
      for( int y = 0; y < Ny; ++y )
	{
	  File<<M[x][y]<<'\t';
	}
      File<<"\n";
    }
  File.close();
}

void Time_Step(matrix & m,const double kbT){

  double x=rand()%Nx;  double y=rand()%Ny;
  int xp,xl,yp,yl;
  double E,Eold,Enew,dE,r;
  xp=x+1;xl=x-1; yp=y+1;yl=y-1;
  if(x==0){xl=Nx-1;}
  if(x==Nx-1){xp=0;}
  if(y==0){yl=Ny-1;}
  if(y==Ny-1){yp=0;}
  E=J*(m[xl][y]+m[xp][y]+m[x][yl]+m[x][yp]);
  
  Eold=m[x][y]*E+h*m[x][y];
  Enew=-m[x][y]*E-h*m[x][y];
  dE=Eold-Enew;
  if(dE<0){
    m[x][y]=-m[x][y];
  }else{
    r=drand48();
    if(r<exp(-dE/kbT)){
      m[x][y]=-m[x][y];
    }
  }
}



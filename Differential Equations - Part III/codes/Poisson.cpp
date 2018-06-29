#include<iostream>
#include<vector>
const int Nx=100;
const int Ny=100;
const int N=10000;
const double T=0.1;
typedef std::vector<std::vector<double> > matrix;
void get_mem(matrix & m);
void print(matrix & m);
void Time_Step(matrix & m,matrix & aux);
bool boundary(int x,int y,matrix & m);
int main(){
  srand(1);
  matrix Laplace,Aux;
  get_mem(Laplace);
   get_mem(Aux);
  for (int t=0;t<N;t++){
    Time_Step(Laplace,Aux);
  }
  print(Laplace);
 
  return 0;
}

void get_mem(matrix & m){
  m.resize(Nx);
  for(int i=0;i<Nx;i++){
    m[i].resize(Ny);
    for(int j=0;j<Ny;j++){
      m[i][j]=drand48();
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


void Time_Step(matrix & m,matrix & m2){
  for(int x=0;x<Nx;x++){
    for(int y=0;y<Ny;y++){
      if(!boundary(x,y,m2)){
	double xp,xl,yp,yl;
	xp=x+1;xl=x-1; yp=y+1;yl=y-1;
	m2[x][y]=(m[xl][y]+m[xp][y]+m[x][yl]+m[x][yp])/4.;
      }
    }
  }
  
  for(int x=0;x<Nx;x++){
    for(int y=0;y<Ny;y++){
      m[x][y]=m2[x][y];
    }
  }
}

bool boundary(int x,int y,matrix & m){

  if(x==0 || x==Nx-1){m[x][y]=0;return true;}
  if(y==0 || y==Nx-1){m[x][y]=0;return true;}
  if((x>Nx/4. && x<3.*Nx/4.) && y==Ny/4.){m[x][y]=1;return true;}
  if((x>Nx/4. && x<3.*Nx/4.) && y==3.*Ny/4.){m[x][y]=-1;return true;}
  return false;
  
}

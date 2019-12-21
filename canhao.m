format short
clear all
clc


P=344738; %Pascal
Area=pi*(16*10^(-3))^2;%metro^2
m=0.5;   %kg
Ltotal=1.5 ; %metros
g=9.81;  %metros/s^2
W=g*m;   %Newton
a=0;     %metros/s^2
Alfa=0*(pi/180); %rad
Wy=0;           %Newtons
vlancamento=0;  %metros/s
Lsaida=0.9;     %metros
voy=0;      %metros/s
vox=0;      %metros/s
t=0;        %Segundos
x1=0;       %metros
x2=0;       %metros
xt=0;       %metros
h1=0;       %metros
h2=0;       %metros
vy=0;       %metros/s
t2=0;       %s
i=90*(pi/180);
graus=0;
Maior=0;
MelhorP=0;
MelhorAlfa=0;
P2=0;

while P<=827371
    
    F=P*Area;
    
    while Alfa<=i
       %corrida%
       Wy=W*sin(Alfa); 
       a=(F-Wy)/m;
       vlancamento=sqrt(2*a*Lsaida);
       %lancamento%
       h1=Ltotal*sin(Alfa);
       voy=vlancamento*sin(Alfa);
       vox=vlancamento*cos(Alfa);
       %Subida%
       t=voy/g;
       x1=vox*t;
       h2=(voy^2)/(2*g);
       %Descida%
       vy=sqrt(2*g*(h1+h2));
       t2=vy/g;
       x2=vox*t2;
       xt=x1+x2;
       P2=P*0.000145038;
       graus=Alfa*(180/pi);
       fprintf('Pressao=%d  ,  Alfa=%d  ,   DistanciaTotal=%d \n\n',P2,graus,xt);
       
       if xt>Maior
           Maior=xt;
           MelhorP=P*0.000145038;
           MelhorAlfa=graus;
           fprintf('MAXIMA DISTANCIA=%d  ,  Pressao=%d  ,  Alfa=%d   \n\n',Maior,MelhorP,MelhorAlfa)
       end
       
       
       Alfa=Alfa+0.087;
      
    end
    
    P=P+68947;
    
    Alfa=0;
  
end

fprintf('MAXIMA DISTANCIA=%d  ,  Pressao=%d  ,  Alfa=%d   \n\n',Maior,MelhorP,MelhorAlfa)


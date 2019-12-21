
function Decola=DECOLAGEM()
    Decola=false;
    %Integracao Corrida de decolagem
    x=0;
    v=0;
    t=0;
    deltaT=0.05;
    
    while x<57 
        forcas=CalculaAtritoTremDePousoEBequilha(PesoAeronave,MomentoAsa,SustentacaoEmpenagem,SustentacaoAsa,DistanciaEmpenagem,DistanciaCG,DistanciaAsa,DistanciaBequilha,DistanciaTDP);
        AtritoBequilha=forcas(2);
        AtritoTDP=forcas(1);
        NormalTremDePouso=forcas(3);
        NormalBequilha=forcas(4);
        Tracao=TracaoMotor(v);
        Arrasto=ForcasAerodinamicas(Sw,Cd,Dens,V);
        SustentacaoAsa=ForcasAerodinamcias(Sw,Cl,Dens,V);
        
        Fx = Tracao - Arrasto - AtritoBequilha - AtritoTDP;
        Fz = SustentacaoAsa + NormalTremDePouso + NormalBequilha - PesoAviao - SustentacaoEmpenagem;
        t=t+deltaT;
        a=Fx/Massa;
        v=v+a*deltaT;
        x=x+v*deltaT;
        
        vd = VelocidadeDecolagem(Dens,PesoAviao,Sw,CLmax);
        if Fz > PesoAviao && v > vd
            x=57;
            Decola=true;
        end
        if x>56 
        
        end
    end
end

   
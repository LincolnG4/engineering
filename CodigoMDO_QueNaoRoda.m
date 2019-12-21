
function Decola=CorridaDeDecolagem(MTOW)
    Decola=false;
    [CL,CD]=BancoDeDadosAerodinamico();
    %Integracao Corrida de decolagem
    x=0;
    v=0;
    a=0;
    t=0;
    deltaT=0.05;
    
    while x<61 && ~Decola
        Fx = TracaoMotor(v) - CalculaForcaAerodinamica(CD,v,'ASA');
        Fz = - MTOW*g + CalculaForcaAerodinamica(CL,v,'ASA');
        t=t+deltaT;
        x=x+v*deltaT;
        v=v+a*deltaT;
        a=Fx/MTOW;
        if Fz > MTOW*g
            Decola = true;
        end
        if x>55
            alfa = alfa + pitchrate() * deltaT;
        end
    end
end

   
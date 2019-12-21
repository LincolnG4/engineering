function Fx = Corrida()
    x=0;
    t=0;
    a=0;
    v=0;
    deltaT = 0.05
    Fx = TracaoMotor(v) - ArrastoAsa() - ArrastoFuselagem() - ArrastoLeme() - ArrastoEmpenagem() - AtritoBequilha() - AtritoTremDePouso();  
    
end

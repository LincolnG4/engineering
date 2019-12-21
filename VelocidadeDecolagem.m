function Vd = VelocidadeDecolagem(Dens,PesoAviao,Sw,CLmax)
    
    Vd = 1.1*sqrt(2*PesoAviao/Sw*Dens*CLmax)^2;  

end
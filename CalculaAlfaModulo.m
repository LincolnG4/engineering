function AlfaModuloAsa  = CalculaAlfaModulo(PesoAeronave,MomentoAsa,SustentacaoEmpenagem,SustentacaoAsa,DistanciaEmpenagem,DistanciaCG,DistanciaAsa,DistanciaTDP, NormalTremDePouso,Inercia)
   
    AlfaModuloAsa = ( SustentacaoAsa*DistanciaAsa + NormalTremDePouso*DistanciaTDP + MomentoAsa - DistanciaCG*PesoAeronave - SustentacaoEmpenagem*DistanciaEmpenagem )/(Inercia);
    
end

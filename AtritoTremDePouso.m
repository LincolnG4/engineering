
function AtritoTDP = CalculaAtritoTremDePousoEBequilha(PesoAeronave,MomentoAsa,SustentacaoEmpenagem,SustentacaoAsa,DistanciaEmpenagem,DistanciaCG,DistanciaAsa,DistanciaBequilha,DistanciaTDP)
    NormalTremDePouso = (SustentacaoEmpenagem*DistanciaEmpenagem + PesoAeronave*DistanciaCG - MomentoAsa - SustentacaoAsa*DistanciaAsa - (PesoAeronave + SustentacaoEmpenagem - SustentacaoAsa)*DistanciaBequilha)/(DistanciaTDP - DistanciaBequilha)
    AtritoTDP = NormalTremDePouso*0.03  %coeficiente de atrito asfalto/concreto   
    AtritoBequilha = (PesoAeronave + SustentacaoEmpenagem - NormalTremDePouso - SustentacaoAsa)*0.03 %coeficiente de atrito asfalto/concreto 
end
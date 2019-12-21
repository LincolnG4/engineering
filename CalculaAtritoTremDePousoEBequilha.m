
function [AtritoTDP,AtritoBequilha,NormalTremDePouso,NormalBequilha] = CalculaAtritoTremDePousoEBequilha(PesoAeronave,MomentoAsa,SustentacaoEmpenagem,SustentacaoAsa,DistanciaEmpenagem,DistanciaCG,DistanciaAsa,DistanciaBequilha,DistanciaTDP)
    NormalTremDePouso = (SustentacaoEmpenagem*DistanciaEmpenagem + PesoAeronave*DistanciaCG - MomentoAsa - SustentacaoAsa*DistanciaAsa - (PesoAeronave + SustentacaoEmpenagem - SustentacaoAsa)*DistanciaBequilha)/(DistanciaTDP - DistanciaBequilha);
    NormalBequilha = PesoAeronave + SustentacaoEmpenagem - NormalTremDePouso - SustentacaoAsa
    AtritoTDP = NormalTremDePouso*0.03;  %coeficiente de atrito asfalto/concreto   
    AtritoBequilha = (NormalBequilha)*0.03; %coeficiente de atrito asfalto/concreto 

end
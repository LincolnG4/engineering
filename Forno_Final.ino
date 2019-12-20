/***************************************************************************
Criador: Gabriel Espinola
Email: g97santos@gmail.com
****************************************************************************/
#include <LiquidCrystal.h>
#include "max6675.h"
#include <SD.h>
#include <SPI.h>

/*Configurações de */// pino SD e Arquivo de dados SD
File myFile;
int pinCS = 53; // PINO DO ARDUINO MEGA 
/*-------------------------------------*/
/* TIMER*/
float Te=0;                        // tempo salvo no SD
unsigned long timer = 0;           //Armazena os segundos transcorridos e inicia no 0 
/*-------------------------------------*/
/*Configurações do  */// Botao START
const int botao = 44;
int var=0;       // valor instantaneo enviado pelo botão
int var2=0;     // valor guardado
int estado=0;
/*-------------------------------------*/
/*Configurações de  */// pino LED
int led=45;         // led no pino 45
int piscaLed=0;
int ligasd=0;
/*-------------------------------------*/
/*Configurações dos Pinos para o  */ //Módulo de Temperatura
int ktcSO = 34  ;
int ktcCS = 35;
int ktcCLK = 33;
MAX6675 ktc(ktcCLK, ktcCS, ktcSO);
/*-------------------------------------*/
/*Configurações dos pinos para o  */ //LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
/*-------------------------------------*/
void setup() {
Serial.begin(9600);
/*Inicialização do*/// LED VERDE
  pinMode(led,OUTPUT);
/*-------------------------------------*/
/*Inicialização do*/// Botao START
pinMode(botao, INPUT);
/*-------------------------------------*/
 /*Configurações para o*/// LCD 
lcd.begin(16, 2);
/*-------------------------------------*/
/*Inicialização do*///  SD
  pinMode(pinCS, OUTPUT);
  
  if (SD.begin())
  {
    Serial.println("Cartão SD conectado");            //Reconhecimento do cartao
    piscaLed=1;
    ligasd=1;
  } else
  {
    Serial.println("Cartão SD nao encontrado");       
    lcd.print("Cartao SD Não Encontrado");
    return;
  }
/*-------------------------------------*/
  delay(500);               
 /*-------------------------------------*/ 
}

void loop() {
    
    /*-------------------------------------*/
//COMANDO PARA PISCAR DE ACORDO COM A CODICAO
  if (piscaLed==0)                                     //ARQUIVO SENDO SALVO dentro do SD, LED PISCANDO
  {                                               //Sim...
    digitalWrite(led, LOW);                       // liga o led
  } //end if
  else                                            //Não...
  {                            
    }
  if (piscaLed==1)                                     //SD ESTA CONECTADO, LED LIGADO CONSTANTE
  {                                               //Sim...
    digitalWrite(led, HIGH);                      // liga o led
  } //end if
  else                                            //Não...
  {
  }
  if (piscaLed==2)                                     //ARQUIVO SENDO SALVO dentro do SD, LED PISCANDO
  {                                               //Sim...
    digitalWrite(led, HIGH);                      // liga o led
    delay(150);
    digitalWrite(led, LOW);                       // desliga o led
    delay(10);

  } //end if
  else                                            
  {                              
    }
/*-------------------------------------*/

/*Inicialização do*///  COMANDO DO BOTAO LIGA/DELISGA

 var=digitalRead(botao);                             // ler o valor enviado pelo botão: "HIGH" ou "LOW"
  if ((var == HIGH) && (var2 == LOW)) {             //Basicamente um "toda vez que o botao for apertado :...
    estado = 1 - estado;
    delay(500); // de-bouncing
    lcd.clear();                                     // A tela do LCD vai ser limpa 
    timer = 0;
         if (ligasd==1)                                                 //ARQUIVO SENDO SALVO dentro do SD, LED PISCANDO
                {                                                          //Sim...
                  piscaLed=1;                                   // liga o led
                 } //end if
                 else                                                         //Não...
                 {  
                                                            
                 }                                  
    myFile = SD.open("Dados.csv", FILE_WRITE);      // Abre o arquivo de dados e escreve "Fim de Dados"
    myFile.println("");
    myFile.close();
    
  }
  
  var2=var;
  if (estado == 1) {                                // ENCERRA

    lcd.setCursor(0,0); 
    lcd.print("Esperando START");
 
  }                                                 // START 
  else {
  
/*-------------------------------------*/

  //Incrementa os segundos
 timer++;
 Te=Te+0.5;
 delay(500);   //Tempo de 1/2 Segundo
 /*-------------------------------------*/ 
/*-------------------------------------*/
    
    lcd.setCursor(0,0);              //Caracter 0 , Linha 1
    lcd.print("Tempo(s)");           // Escreve no lcd "Tempo(S)" 
    lcd.setCursor(0,1);             //Caracter 0, Linha 2
    lcd.print("Temp (C)");

    /*Inicialização da Escrita*/                               //Abre o arquivo no SD para salvar os dados
  myFile = SD.open("Dados.csv", FILE_WRITE);                  //Abre arquivo para escrita
    //Cria string de dados para armazenar no cartão SD
  //Utilizando arquivo do tipo Comma Separete Value (.CSV)
  String dataString = String(Te) + ", " + ktc.readCelsius() ;
  /*-------------------------------------*/ 
  
  if (myFile)                                     //Arquivo aberto com sucesso?
  {                                               //Sim...
    myFile.println(dataString);
    myFile.close();
    Serial.println(dataString);
     piscaLed=2;
  } //end if
  else                                            //Não...
  {
    Serial.println("Gravacao Pausada");      //Informa que há algum erro
  
  }
/*-------------------------------------*/
/*Dados que aparecem na tela do LCD*/  

 /*-------------------------------------*/ 

 
 lcd.setCursor(10,0);                   // Lcd.SetCursos(Coluna,Linha)
 lcd.print(String(timer));
 
 lcd.setCursor(10,1);             
 lcd.print(ktc.readCelsius());





  } //FECHA ELSE START 

} 

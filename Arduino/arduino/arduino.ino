const int light_kitchen = 4;
const int light_bathroom = 5;
const int light_bedroom = 6;
const int light_livingroom = 7;
char opt;

void setup() {

  pinMode(light_kitchen,OUTPUT);
  pinMode(light_bathroom,OUTPUT);
  pinMode(light_bedroom,OUTPUT);
  pinMode(light_livingroom,OUTPUT);

 //digital write apaagr o prender
  
  digitalWrite (light_kitchen,LOW);
  digitalWrite (light_bathroom,LOW);
  digitalWrite (light_bedroom,LOW);
  digitalWrite (light_livingroom,LOW);

  Serial.begin(9600); //Baud, serial comunicaion con la placa
  Serial.print("¡¡¡Welcome to my SmartHome!!!"); //Mnesaje reflejado en pantalla

}
void mainMenu() {
  
  Serial.println(":::MAIN MENU:::");
  Serial.println("[1]. Turn on light kitchen");
  Serial.println("[2]. Turn off light kitchen");
  Serial.println("[3]. Turn on light bedroom");
  Serial.println("[4]. Turn off light livingroom");
  //complete here all menu options
  Serial.println("[9]. Turn on all");
  Serial.println("[10]. Turn off all");
}
void loop(){
  mainMenu();

}

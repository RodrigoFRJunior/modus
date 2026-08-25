const int botao1 = 2;
const int botao2 = 3;
const int botao3 = 4;
const int botao4 = 5;

bool estadoAnterior1 = HIGH;
bool estadoAnterior2 = HIGH;
bool estadoAnterior3 = HIGH;
bool estadoAnterior4 = HIGH;

void setup() {

  Serial.begin(115200);

  pinMode(botao1, INPUT_PULLUP);
  pinMode(botao2, INPUT_PULLUP);
  pinMode(botao3, INPUT_PULLUP);
  pinMode(botao4, INPUT_PULLUP);

}

void loop() {

  bool estado1 = digitalRead(botao1);
  bool estado2 = digitalRead(botao2);
  bool estado3 = digitalRead(botao3);
  bool estado4 = digitalRead(botao4);

  if (estado1 == LOW && estadoAnterior1 == HIGH) {
    Serial.println("A5:1");
    delay(50);
  }

  if (estado2 == LOW && estadoAnterior2 == HIGH) {
    Serial.println("A5:2");
    delay(50);
  }

  if (estado3 == LOW && estadoAnterior3 == HIGH) {
    Serial.println("A5:3");
    delay(50);
  }

  if (estado4 == LOW && estadoAnterior4 == HIGH) {
    Serial.println("A5:4");
    delay(50);
  }

  estadoAnterior1 = estado1;
  estadoAnterior2 = estado2;
  estadoAnterior3 = estado3;
  estadoAnterior4 = estado4;

}
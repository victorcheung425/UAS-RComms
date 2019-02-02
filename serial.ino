void setup() {
  Serial.begin(9600);
}

void loop() {
  int incomingByte;
  int motornum;
  int bytecount;
  char angle[3];
  int i;
  
  if(Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

  if(incomingByte == 1 || incomingByte == 2){
    motornum = incomingByte;
    Serial.print(motornum);
    Serial.println();
    

  for(bytecount = 0; bytecount < 3; bytecount++){
    incomingByte = Serial.read();
    angle[bytecount] = incomingByte;
    }
  sscanf(angle,"%d",&i);
  Serial.print(i);
  Serial.println();
  }
  }

   // echo
   // Serial.write(incomingByte);


  }

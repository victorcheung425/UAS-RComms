/*******************************************************************************
FUSION HAHAHAHAHA
i hope this works

*******************************************************************************/


#include <DynamixelWorkbench.h>

#if defined(__OPENCM904__)
  #define DEVICE_NAME "3" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
  #define DEVICE_NAME ""
#endif   

#define BAUDRATE  57600
#define DXL_ID1    1
#define DXL_ID2    2
#define DXL_ID3    3

DynamixelWorkbench dxl_wb;

String inString = "";    // string to hold input

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(57600);
  pinMode(19, OUTPUT);
  
  const char *log1;
  const char *log2;
  bool result1 = false;
  bool result2 = false;

  uint8_t dxl_id1 = DXL_ID1;
  uint8_t dxl_id2 = DXL_ID2;

  uint16_t model_number = 0;

  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

 result1 = dxl_wb.init(DEVICE_NAME, BAUDRATE, &log1);
  if (result1 == false)
  {
    Serial.println(log1);
    Serial.println("Failed to init");
  }
  else
  {
    Serial.print("Succeeded to init : ");
    Serial.println(BAUDRATE);  
  }

  result1 = dxl_wb.ping(dxl_id1, &model_number, &log1);
  if (result1 == false)
  {
    Serial.println(log1);
    Serial.println("Failed to ping");
  }
  else
  {
    Serial.println("Succeeded to ping");
    Serial.print("id : ");
    Serial.print(dxl_id1);
    Serial.print(" model_number : ");
    Serial.println(model_number);
  }

  result1 = dxl_wb.jointMode(dxl_id1, 0, 0, &log1);
  
  
  result2 = dxl_wb.init(DEVICE_NAME, BAUDRATE, &log2);
  if (result2 == false)
  {
    Serial.println(log2);
    Serial.println("Failed to init");
  }
  else
  {
    Serial.print("Succeeded to init : ");
    Serial.println(BAUDRATE);  
  }

  result2 = dxl_wb.ping(dxl_id2, &model_number, &log2);
  if (result2 == false)
  {
    Serial.println(log2);
    Serial.println("Failed to ping");
  }
  else
  {
    Serial.println("Succeeded to ping");
    Serial.print("id : ");
    Serial.print(dxl_id2);
    Serial.print(" model_number : ");
    Serial.println(model_number);
  }

  result2 = dxl_wb.jointMode(dxl_id2, 0, 0, &log2);
  if (result2 == false || result1 == false)
  {
    Serial.println(log2);
    Serial.println(log1);
    Serial.println("Failed to change joint mode for either 1 or 2");
  }
  else
  {
    Serial.println("Succeed to change joint mode");
    Serial.println("Dynamixel is moving...");
  }
  
  // send an intro:
  Serial.println();
}

void loop() {
  // Read serial input:
  while(Serial.available() > 0 ){
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string, then the string's value:
    if (inChar == '\n') {
      //Serial.println(inString.toInt());
      Serial.println(inString);
      dxl_wb.goalPosition(1, inString.toInt()); //moves motor 1
      dxl_wb.goalPosition(2, inString.toInt()); //moves motor 2
      
      // clear the string for new input:
      inString = "";

    }
    
    
  }
}

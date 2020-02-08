/*******************************************************************************
* Copyright 2016 ROBOTIS CO., LTD.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*******************************************************************************/

/* Authors: Taehun Lim (Darby) */

#include <DynamixelWorkbench.h>

#if defined(__OPENCM904__)
  #define DEVICE_NAME "1" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
  #define DEVICE_NAME ""
#endif   

#define BAUDRATE  1000000
#define DXL_ID    2

DynamixelWorkbench dxl_wb;

unsigned int Kalman_filter_for_SEN_1(signed int ADC_Value)
{
       static unsigned char counter = 0;
       static float A,H,Q,R,X,P;
       float XP,PP;
       static float value_return=0;
       float K;
       float temp_float;
 
       if(counter<1)
          counter++;
 
       if(counter==1)
       {
             A = 1;
             H = 1;   //1
             Q = 0.005;     //earlier 0.92,0.02
             R = 0.5;     //
             X = 1023;
             P = 1000;
             counter = 2;
 
           XP = A*X;
           PP = A*P*A + Q;
 
           K = PP*H;
           K /=(H*H*PP)+R;
 
           temp_float = (float)(ADC_Value-H*XP);
           value_return = XP + K*temp_float;
 
           temp_float = H*PP;
           P = PP-K*temp_float;
           return (unsigned int)value_return;
       }
       else
       {
           XP = A*value_return;
           PP = A*P*A + Q;
 
           K = PP*H;
           K /=(H*H*PP)+R;
 
           temp_float = (float)(ADC_Value-H*XP);
           value_return = XP + K*temp_float;
 
           temp_float = (float)H*PP;
           P = PP-K*temp_float;
           return (unsigned int)value_return;
 
       }
 }


void setup() 
{
  Serial.begin(57600);
  // while(!Serial); // Wait for Opening Serial Monitor

  const char *log;
  bool result = false;

  uint8_t dxl_id = DXL_ID;
  uint16_t model_number = 0;

  result = dxl_wb.init(DEVICE_NAME, BAUDRATE, &log);
  if (result == false)
  {
    Serial.println(log);
    Serial.println("Failed to init");
  }
  else
  {
    Serial.print("Succeeded to init : ");
    Serial.println(BAUDRATE);  
  }

  result = dxl_wb.ping(dxl_id, &model_number, &log);
  if (result == false)
  {
    Serial.println(log);
    Serial.println("Failed to ping");
  }
  else
  {
    Serial.println("Succeeded to ping");
    Serial.print("id : ");
    Serial.print(dxl_id);
    Serial.print(" model_number : ");
    Serial.println(model_number);
  }

  result = dxl_wb.wheelMode(dxl_id, 0, &log);
  if (result == false)
  {
    Serial.println(log);
    Serial.println("Failed to change wheel mode");
  }
  else
  {
    Serial.println("Succeed to change wheel mode");
    Serial.println("Dynamixel is moving...");

    for (int count = 0; count < 3; count++)
    {
      dxl_wb.goalVelocity(dxl_id, (int32_t)-5);
      delay(3000);

      dxl_wb.goalVelocity(dxl_id, (int32_t)5);
      delay(3000);
    }

    dxl_wb.goalVelocity(dxl_id, (int32_t)0);
  }
}


int Direction = 0;

void loop() {
  const char *log;
  bool result = false;

  uint8_t dxl_id = DXL_ID;
  uint16_t model_number = 0;
  
  int AdcData =
  Serial.print("A0 = ");
  Serial.print(analogRead(A0)*(3300/1023));
  Serial.print("\t");

  int phase = analogRead(A1)*(3300/1023);

  Serial.print("A1 = ");
  Serial.print(phase);
  Serial.print("\t");

  int filtered_phase = Kalman_filter_for_SEN_1(phase);

  Serial.print("FA1 = ");
  Serial.print(filtered_phase);
  Serial.print("\t");

  /*
  if (filtered_phase >= 1075)
  {
    Direction = 1;
  }
  else if (filtered_phase <= 900)
  {
    Direction = -1;
  }
  else
  {
    Direction = 0;
  }
*/
  float P = 0.3;
  
  Serial.print(Direction);
  Serial.print("\n");
  //dxl_wb.goalVelocity(dxl_id, Direction*(30));

  dxl_wb.goalVelocity(dxl_id, P*(filtered_phase - 950));
  
  delay(100);
}

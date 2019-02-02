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
  #define DEVICE_NAME "3" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
  #define DEVICE_NAME ""
#endif   

#define BAUDRATE  57600
#define DXL_ID1    1
#define DXL_ID2    2
#define DXL_ID3    3

DynamixelWorkbench dxl_wb;

void setup() 
{
  Serial.begin(57600);
  // while(!Serial); // Wait for Opening Serial Monitor

  const char *log1;
  const char *log2;
  const char *log3;
  bool result1 = false;
  bool result2 = false;
  bool result3 = false;

  uint8_t dxl_id1 = DXL_ID1;
  uint8_t dxl_id2 = DXL_ID2;
  uint8_t dxl_id3 = DXL_ID3;

  uint16_t model_number = 0;

/*motor id 1*/
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
  if (result1 == false)
  {
    Serial.println(log1);
    Serial.println("Failed to change joint mode");
  }
  else
  {
    Serial.println("Succeed to change joint mode");
    Serial.println("Dynamixel is moving...");

    for (int count = 0; count < 3; count++)
    {
      dxl_wb.goalPosition(dxl_id1, (int32_t)0);
      delay(3000);

      dxl_wb.goalPosition(dxl_id1, (int32_t)1023);
      delay(3000);
    }
  }

  /* motor id 2 */

  
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
  if (result2 == false)
  {
    Serial.println(log2);
    Serial.println("Failed to change joint mode");
  }
  else
  {
    Serial.println("Succeed to change joint mode");
    Serial.println("Dynamixel is moving...");

    for (int count = 0; count < 3; count++)
    {
      dxl_wb.goalPosition(dxl_id2, (int32_t)0);
      delay(3000);

      dxl_wb.goalPosition(dxl_id2, (int32_t)1023);
      delay(3000);
    }
  }

  /* motor id 3 */
  
  result3 = dxl_wb.init(DEVICE_NAME, BAUDRATE, &log3);
  if (result3 == false)
  {
    Serial.println(log3);
    Serial.println("Failed to init");
  }
  else
  {
    Serial.print("Succeeded to init : ");
    Serial.println(BAUDRATE);  
  }

  result3 = dxl_wb.ping(dxl_id3, &model_number, &log3);
  if (result3 == false)
  {
    Serial.println(log3);
    Serial.println("Failed to ping");
  }
  else
  {
    Serial.println("Succeeded to ping");
    Serial.print("id : ");
    Serial.print(dxl_id3);
    Serial.print(" model_number : ");
    Serial.println(model_number);
  }

  result3 = dxl_wb.jointMode(dxl_id3, 0, 0, &log3);
  if (result3 == false)
  {
    Serial.println(log3);
    Serial.println("Failed to change joint mode");
  }
  else
  {
    Serial.println("Succeed to change joint mode");
    Serial.println("Dynamixel is moving...");

    for (int count = 0; count < 3; count++)
    {
      dxl_wb.goalPosition(dxl_id3, (int32_t)0);
      delay(3000);

      dxl_wb.goalPosition(dxl_id3, (int32_t)1023);
      delay(3000);
    }
  }
}

void loop() 
{

}

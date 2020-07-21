/*
  Bafang controller simulator (Arduino Nano Every)

  This is a bafang controller simulator that I made to test my Bafang Tuner.

  This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

#define READ 0x11
#define WRITE 0x16
#define CONNECT 0x51
#define BASIC 0x52
#define PEDAL 0x53
#define THROTTLE 0x54

#define COMMAND_LENGTH 2
#define INFO_LENGTH 3 // payload length of get info packet
#define BASIC_LENGTH 26 // payload length of set basic packet


unsigned char infoMessage[19] = {0x51, 0x10, 0x48, 0x5a, 0x58, 0x54, 0x53, 0x5a, 0x5a, 0x36, 0x32, 0x32, 0x32, 0x30, 0x31, 0x31, 0x01, 0x14, 0x1b};
unsigned char basicMessage[27] = {0x52, 0x18, 0x1F, 0x0F, 0x00, 0x1C, 0x25, 0x2E, 0x37, 0x40, 0x49, 0x52, 0x5B, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x34, 0x01, 0xDF};
unsigned char pedalMessage[14] = {0x53, 0x0B, 0x03, 0xFF, 0xFF, 0x64, 0x06, 0x14, 0x0A, 0x19, 0x08, 0x14, 0x14, 0x27};
unsigned char databuffer[40];
unsigned char commandbuffer[2];
unsigned char setBasicReceived[2] = {0x52, 0x24};
unsigned char setPedalReceived[2] = {0x53, 0x24};
unsigned char setThrottleReceived[2] = {0x53, 0x24}; // correct??

typedef enum app_states
{
    READ_COMMAND,
    READ_DATA,
    OTHER    
} State_t;

State_t state;

uint8_t bytes_read = 0;

void print_packet(){

        Serial.println("read bytes:  " + String(bytes_read));
        for(int i = 0; i < bytes_read; i++)
        {
            Serial.print(databuffer[i], HEX);
            Serial.print(" ");
        }
        Serial.println();
}

bool read_bytes(int length){ 
    while(Serial1.available() < length) Serial.println("bytes available : " + String(Serial.available()));   
    if (Serial1.available() > length - 1)
    {
        bytes_read = Serial1.readBytes(databuffer, length);
        Serial.println(bytes_read);
        state = READ_COMMAND;
        print_packet();

        return true;
    }
    return false;
}

void read_command(){
    if (Serial1.available() > 1){
        Serial1.readBytes(commandbuffer, COMMAND_LENGTH);
        Serial.println("Command is: Ox" + String(commandbuffer[0], HEX) + " 0x" + String(commandbuffer[1], HEX));
        state = READ_DATA;
    }
}

void get_data(){
    if (commandbuffer[0] == READ){
        switch (commandbuffer[1])
        {   
        case CONNECT:
            if(read_bytes(INFO_LENGTH))
                Serial1.write(infoMessage, 19);
            break;
        case BASIC:
            Serial1.write(basicMessage, 27);
            state = READ_COMMAND;
            break;
        case PEDAL:
            Serial1.write(pedalMessage, 14);
            state = READ_COMMAND;
            break;
        default:
            break;
        }
    } else if (commandbuffer[0] == WRITE){
      //Serial.println("write command");
        switch (commandbuffer[1])
        { 
            case BASIC:
                read_bytes(BASIC_LENGTH);
                Serial1.write(setBasicReceived, 2);
                Serial.println("basic write command");
                break;
            default:
                break;
        }
    }
    
}


void setup() {
    Serial1.begin(1200); //rx tx
    Serial.begin(9600);  //usb
    while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
    }

    Serial.println("Starting");
  
    state = READ_COMMAND;
}

void loop() {

    switch (state)
    {
    case READ_COMMAND:
        read_command();
        break;
    case READ_DATA:
        get_data();
        break;
    default:
        break;
    }
}

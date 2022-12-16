<!--- Copyright 2022 Aaron Metsch (https://github.com/ametsch) --->
<style type="text/css">
   @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');

   * {
      font-family: default;
   }
   code {
      font-family: 'Source Code Pro', monospace;
   }
   ul {
      list-style-type: square;
   }
   ol {
      list-style-type: decimal;
   }
   a:hover, a:active {
      color: #A600FF;
   }
   a:link, a:visited {
      color: #002AFF;
   }
   
</style>

# Arduino temperature, humidity, and light level monitor: How to
### By Aaron Metsch ([https://github.com/ametsch](https://github.com/ametsch))
## Required Materials:
 - [DHT11 temperature and humidity sensor](https://amzn.to/3iOsgHY)
 - [Arduino Uno compatible development board](https://amzn.to/3uAJ6N5)
 - Computer running **Windows 10, Windows 11, MACOS, or GNU/Linux** with [Arduino IDE **1.8**](https://www.arduino.cc/en/software) installed
 - [Male to male jumper wires](https://amzn.to/3i9girW)
 - [Solderless breadboard](https://amzn.to/3EU85Rx)
 - USB cable to connect your board to your computer
 - [Photoresistor](https://www.adafruit.com/product/161)
 - [10kΩ resistor](https://www.adafruit.com/product/2784)
 - Project code found at: [https://bit.ly/3VB2Iwz](https://bit.ly/3VB2Iwz)
___
## Background Knowledge:
 - [Resistors](https://www.explainthatstuff.com/resistors.html)
 - [Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)
___
## Steps:
 1. Install the neccesary Arduino libraries ([How to install Arduino libraries](https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries)): 
    1. [Adafruit Unified Sensor](https://github.com/adafruit/Adafruit_Sensor)
    2. [DHT sensor library](https://github.com/adafruit/DHT-sensor-library)
 2. Assemble everything as shown: 
[![fritzing-layout.png](https://bit.ly/3Fu1DRE)](https://postimg.cc/sGdXMj2S)

 3. Downloading the code:
    1. Download the code from the link in the beginning of this document
    2. Open the Arduino IDE on your computer
    3. Click in the Arduino IDE window
    4. Click 'File' on the navigation bar
    5. Click 'Open'
    6. Navigate to the 'arduinoDHT.ino' file you just downloaded
    7. Click 'open' then click 'ok'

<div class="page"></div>

 4. Code explanation:
    1. Start by including the neccesary libraries at the top of the file:
         ```arduino cpp
            #include "DHT.h" // Include DHT library
            #include "DHT_U.h" // Include DHT library
            #include "string.h" // Include arduino string library
         ```
    2. Next we define some constants (if you are not using a DHT11 replace it with the type of DHT you are using):
         ```arduino cpp
            #define DHTTYPE DHT11 // Define DHT type
            #define DHTPIN 5 // The arduino pin which is connected to the DHT data pin
            const int lightSensorPin = A0; // Define the arduino pin that the light sensor is connected to
         ```
    3. Next we create the `setup` function to intialize everything:
         ```arduino cpp
            void setup() {
               Serial.begin(9600); // initialize the serial communication protocol
               dht.begin(); // initialize the DHT
            }
         ```

      <div class="page"></div>

    4. Now we add the `loop` function to tell the arduino to constantly check the temperature, humidity, and light level and print it to the serial monitor:
         ```arduino cpp
            void loop() {
               double f = dht.readTemperature(true);
               double h = dht.readHumidity();
               double l = analogRead(lightSensorPin) / 5.0;
               String str = String("");
               str.concat(String(f));
               str.concat(", ");
               str.concat(String(h));
               str.concat(", ");
               str.concat(String(l));
               Serial.println(str);
            }
         ```

 5. Uploading the program to the Arduino
    1. Connect the arduino to your computer over USB
    2. In the Arduino IDE window click 'Tools' on the top navigation bar, then click 'Board', then click 'Arduino Uno'
    3. Now click 'Tools' then 'Port' and select the option that appears
    4. Click 'Sketch' on the top navigation bar, then click 'Upload' and wait until it says 'Done Uploading' on the bottom of the screen
    5. Click 'Tools', then click 'Serial Monitor'
    6. You should see data that looks like this:
         
         ```
            75.02, 25.00, 40.80
            75.02, 25.00, 40.80
            75.02, 25.00, 40.80
            75.02, 25.00, 40.00
            75.02, 25.00, 40.20
            75.02, 25.00, 40.00      
         ```

      <div class="page"></div>

 6.  (**OPTIONAL**) Graphing the data:
      1. Install [Python 3 **(>=3.9)**](https://www.python.org/downloads/)
      2. Move the `requirements.txt` and `read2file.py` into a new folder
      3. Open your computer's command line and run the corrosponding commands:
         - Powershell on Windows:
            1. `python -m pip install --upgrade pip`
            2. `pip install -r {path}` {path} = the path to the requirements.txt file from the github repository listed at the beginning of this document.
            3. `python -m serial.tools.list_ports` to list available ports
            4. `python {path}` {path} = the path to the read2file.py file from the github repository listed at the beginning of this document.
         - Terminal on GNU/Linux or MacOS:
            1. `python3 -m pip install --upgrade pip`
            2. `python3 -m pip install -r {path}` {path} = the path to the requirements.txt file from the github repository listed at the beginning of this document.
            3. `python3 -m serial.tools.list_ports` to list available ports
            4. `python3 {path}` {path} = the path to the read2file.py file from the github repository listed at the beginning of this document.
       4.  Enter the port your Arduino is on (from the Arduino IDE) e.g. `COM3`, then press <kbd>Enter</kbd>
       5.  Enter how many reads you want it to perform in between the reads it saves a reading as a data point e.g. `100`, then press <kbd>Enter</kbd>
       6.  Enter how many data points you want it to save e.g. `25`, then press <kbd>Enter</kbd>
       7.  After it gathers all the data requested it will show you a graph of the data and output it to a csv and image of the graph. 
            Example Graph:
            <a href="https://postimg.cc/tYwdkyL1">
               <img src="https://i.postimg.cc/kgXjngsy/graph.png" width="75%" alt="https://postimg.cc/tYwdkyL1" />
            </a>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
Copyright 2022 Aaron Metsch (<a href="https://github.com/ametsch">https://github.com/ametsch</a>)
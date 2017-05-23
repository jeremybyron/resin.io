# SMS to Speech Project with Raspberry Pi 3

This Raspberry Pi 3 project is intended for Embedded System (2016) and Wireless and Mobile Networks (2017). This project involves the conversion of text messages (SMS) sent to a Twilio number into audible speech, using one of Raspberry Pi's Speech Synthesis package called eSpeak.

## Step 1: What You Will Need

- A Raspberry Pi 3 model B
- A 4GB or larger microSD card. The speed class of the card also matters - class 10 card or above is the way to go.
- An Ethernet cable
- A 2A USB micro power supply
- Headphones or speakers

Most of these items come with your Raspberry Pi, except for the Ethernet cable and speakers.


## Step 2: Create Accounts

To begin with, you will need to sign up on Resin.io and Twilio.


### RESIN.IO

Resin.io provides many useful features which aid us in this project. We will need their operating system (resinOS) and application terminal to get to work. Create an account on Resin.io and follow the instructions provided on their documentations to create an application. Please refer to their documentations as they provide more detailed guides on how to use Resin.io.

The basic things that we need to highlight on working with Resin.io is to sign up an account, create an application (e.g. SMS to Speech), select device type (in this case, Raspberry Pi 3) and download resinOS disk image. After you download and write the disk image on your microSD card, insert the microSD card to your Raspberry Pi and your device will appear on Resin.io’s dashboard in about 10 minutes after you switch it on. Make sure that the Ethernet cable is plugged in as we need the Raspberry Pi to go online. Next, select your device by clicking on it and go to “Actions” tab. Select “Enable public URL for this device”. We will use the generated URL for Twilio later.

### TWILIO

Once again, it is a great start to spend a couple of minutes reading Twilio’s documentations in order to get familiar with it. What we will need from Twilio in this project is a real phone number. Yes, a phone number which we can send text messages to. Twilio may be rather difficult to understand but what’s important is that you sign up on Twilio, and get a phone number. Usually, we are given a choice to select the numbers and the services that it can provide such as SMS.
Click on the number and you should find a category called “messaging”. Then, copy and paste the Resin.io public URL on “a message comes in” box (the link with the 80 port) and select the “HTTP GET method”. Leave everything else as default and click Save. Thus, we can get notified if a text message is sent to our Twilio number.

## Step 3: Connect the Parts

Download and install Git Bash, along with all other things that is necessary for its environment, such as Python 3, etc. If you are using Windows, launch Git Bash shell and clone this repository. You can do so by entering the command

```
git clone https://github.com/jeremybyron/resin.io.git
```

After that, go to the local directory which you have created

```
cd resin.io
```

Add the Resin git remote endpoint by running the command git remote add shown in the top-right corner of your application page, such as

```
git remote add resin frostheart26@git.resin.io:frostheart/smstospeech3.git
```

Finally, add the push Resin command

```
git push resin master
```

You'll know your code has been successfully compiled and built when our friendly unicorn mascot appears in your terminal. This means your code is safely built and stored on Resin’s image registry. It should only take about 2 minutes to build your code and subsequent builds will be quicker because of build caching. Your application will now be downloaded and executed by all the devices you have connected in your application fleet. You may have to wait about 6 minutes for the first push... So time for more tea, but don't worry, all subsequent pushes are much, much faster due to Docker layer sharing. You can see the progress of the device code updates on the device dashboard.

## Step 4: Install Packages and Run

This step is rather complicated because we might not know what exactly are the packages needed to make eSpeak and other functions in the resinOS to work perfectly. However, I have made a shortcut which saves you from the troubles of a sleepless night Googling on how to make it work. These are the command lines I have entered in the Resin terminal of my device

```
sudo apt-get update
sudo modprobe snd_bcm2835
sudo apt-get install alsa-libs mplayer espeak
sudo apt-get upgrade
sudo apt-get install alsa-utils
sudo apt-get install mpg321
sudo apt-get install python-pip
sudo apt-get install python3-pip
sudo pip3 install num2words
```

Finally, launch the server

```
Python server.py
```

Turn up your speakers and send an SMS to your Twilio number. You will hear a robotic, monotonous and old lady reading your text for you.







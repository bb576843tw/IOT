from machine import Pin,PWM
import time, network, urequests

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("LULUiPhone", "aaaaaaaa")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

shock = Pin(16, Pin.IN)
button=Pin(13,Pin.IN,Pin.PULL_UP)
led=Pin(12,Pin.OUT)
led.value(0)

#beeper=PWM(Pin(0),freq=440,duty=512)
def alarmClockBeep(pwm):
     for i in range(1,10):        #4 次迴圈 (1~4)
        beeper=PWM(Pin(0),freq=200,duty=800)
        time.sleep(0.3)
        beeper=PWM(Pin(0),freq=800,duty=800)
        time.sleep(0.3)
        beeper=PWM(Pin(0),freq=200,duty=800)
        time.sleep(0.3)
        beeper=PWM(Pin(0),freq=800,duty=800)
        time.sleep(0.3)
pwm=PWM(Pin(0))

while True:

    if shock.value() == 1:
        print("感應到振動!")
        led.value(1)
        alarmClockBeep(pwm)

        while True:
            
            if not button.value():
                led.value(not led.value())
                time.sleep_ms(300)
                pwm.deinit() 
                while not button.value():
                    pass
        
        # 連線 IFTTT 服務發送簡訊通知
        urequests.get("http://maker.ifttt.com/trigger/therf2/with/key/t_i9dOKO1ciH57JFd4ASE")    
        
        # 暫停 60 秒, 避免短時間內一直收到重複的警報c
        time.sleep(60)



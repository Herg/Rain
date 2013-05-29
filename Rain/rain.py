
import sys
from services.forecast_service import forecast_service
from services.led_service import led_service

fs = forecast_service()
ls = led_service()

if __name__ == "__main__":
    while(True):
        temp = raw_input("\n\nGimme a temperature: ")
        if temp.lower() == "exit":
            break
        try:
            temp_int = int(temp)
        except:
            print "Input must be a number!"
        if temp_int >= 100:
            print "\n\n\nThat shit is HOT\n\n\n"
            ls.light_em_up(10)
        elif temp_int >= 60:
            print "\n\n\nThat's pretty warm\n\n\n"
            ls.light_em_up(3)
        else:
            print "\n\n\nNothing to see here\n\n\n"
        

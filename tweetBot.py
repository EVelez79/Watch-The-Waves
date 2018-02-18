import apiHandler, time, logging

logging.basicConfig(filename="api.log",filemode="a",LEVEL=logging.INFO)

counter = 0

logger = open("apiLog-{}.log".format(time.time()),"w")

splitter = "(!@!)"

while counter <= 1000 :
    #apiHandler.constructMessage()
    apiData = str(apiHandler.getForecast())
    logger.write(apiData + "\n\n" + splitter + str(time.time()) + "\n\n")
    print "Api Call #{}\n".format(counter)
    counter += 1
    time.sleep(1800)#30 Mins

logger.close()
print "Done"

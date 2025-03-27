import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download()/(10**6) , "Mbps")
print("Wifi Upload Speed is ", wifi.upload()/(10**6) , "Mbps")
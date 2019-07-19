# Synchronizing the RTC (NTS, Network Time Synchronization)

For IoT application, it is crutial to synchronize your internal RTC before to send or receive packets over the internet. 

The Raspberry embedded system have the network time synchronization service enabled by default as shown in the picture below: 


The RTC_Internal_update.py python program forces the Network Time Synchronization (NTS) to synchronize the internal RTC as shown in the picture below: 




This could be really handy in many application, specially in IoT application, where before sending data packets, we ensure that the RTC is indeed synchronized.



NTP: Network Time Protocol is a networking protocol for clock synchronization between computer systems.




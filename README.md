# Synchronizing the RTC (NTS Network Time Synchronization)

For IoT application, it is crutial to synchronize your internal RTC before sending or receiving packets over the internet. 

Our Raspberry embedded system with the Raspbian GNU/Linux has the network time synchronization service enabled by default as shown in the picture below: 

![nts image](/photos/remote_time_server_nts_status.jpg)



The RTC_Internal_update.py python program forces the NTS service to synchronize the internal RTC as shown in the picture below: 

![programOutput image](/photos/Sync_Internal_RTC_From_Internet_explained.jpg)



This could be really handy in many application, specially in IoT application, where before sending data packets, we ensure that the RTC is indeed synchronized.

Once we have synchronized the internal RTC with the remote time server, we could forward this information further to other devices. 


Glossary:

NTP: Network Time Protocol is a networking protocol for clock synchronization between computer systems.

NTS: Network Time Synchronization

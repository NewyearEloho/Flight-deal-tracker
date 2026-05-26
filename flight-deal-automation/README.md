#  Flight Deal Tracker (Python Automation Project)

##  Project Overview

This is a Python automation project that tracks real-time flight prices and sends email notifications when cheaper flight deals are found.

The system eliminates the need to manually check flight prices daily by automating the entire process from data retrieval to notification.

---

## How It Works

1. Destination cities and target prices are stored in Google Sheets  
2. A Python script reads this data using the Sheety API  
3. The script connects to a flight search API (SerpAPI - Google Flights) to fetch real-time flight prices  
4. The live prices are compared with the stored target prices  
5. If a cheaper flight is found:
   - The Google Sheet is automatically updated  
   - An email notification is sent to all users with flight details  
6. If no cheaper flight is found, the system continues monitoring

---

##  Key Features

- Real-time flight price tracking  
- Google Sheets integration as a lightweight database  
- Automated email notifications  
- Stopover flight fallback logic  
- Error handling for missing or incomplete API data  
- Multi-user email notification system  

---

## Tech Stack

- Python  
- Requests  
- Sheety API  
- SerpAPI (Google Flights API)  
- SMTP (Email automation)  
- dotenv (Environment variables)

---

##  Future Improvements

- SMS notifications  
- WhatsApp integration  
- User-specific destination selection  
- Web interface using Flask/Django  
- Deployment to cloud (AWS / Render)

---

## 💡 What I Learned

- Working with REST APIs in Python  
- Data handling from external sources  
- Automation workflows  
- Error handling and debugging API responses  
- Email automation using SMTP  
- Structuring multi-module Python projects  

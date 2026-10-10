# Docker Deep Dive & Docker Compose Lab 🐳

### Core Concepts Learned:
1. **Image vs Container:** Image ek blueprint hai, Container us blueprint ka running instance hai.
2. **Container vs VM:** VM ko apna pura OS chahiye hota hai (heavy), Container host ka OS share karta hai (lightweight aur fast).
3. **Port Mapping:** `5000:5000` ka matlab laptop (localhost) ke port 5000 ko container ke port 5000 se connect karna.
4. **Volume:** Container delete hone par data ud jata hai. Data ko safe (persistent) rakhne ke liye hum volume use karte hain.
5. **Docker Compose:** Multiple containers (App + Database) ko ek sath run, manage aur connect karne ka tool.
   - `docker compose up -d`: Saari services background mein start karta hai.
   - `docker compose down`: Saari services, network aur containers ko stop aur remove karta hai.
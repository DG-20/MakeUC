# 🧠 What was The Inspiration Behind BlockPortal?
Our inspiration behind BlockPortal is two-fold. One of the reasons is that technology is ever-evolving, with new languages, frameworks, and cryptocurrencies being developed every single day. As such, it is important to develop applications ready for the future. With this in mind, we decided to use the Hedera blockchain along with the hbar cryptocurrency to create a digital ledger of each student's transactions. Another large reason for selecting Hedera was due to its carbon negative nature as compared to other leading decentralized ledgers. The second source of inspiration is our experience as students. A very crucial aspect of students' academic experiences is course registration. Often, this is a pain point for students as the UI is outdated and the means of payment are archaic. We wanted to create an easy-to-use student registration portal which allowed for the use of the currency of the future - crypto.

# 💻 What is BlockPortal?
BlockPortal is a student portal service that integrates blockchain technology with a seamless student experience. It allows for secure, decentralized transactions which can be tracked and easily viewed within BlockPortal. Our application communicates with a database which stores available classes along with key information such as professor names, locations, sections, costs, and more. Once the student has completed the hbar transaction (tuition) successfully, they will be registered for the class.

# 🔧 How did we build it?
The backbone of BlockPortal is created with Python Django, which handles the communication between the front-end, the database, and the blockchain. In Django, we use API calls to a MongoDB database using PyMongo to retrieve class information of a specific university, as well as store course registration information for students. We utilized the Hedera SDK to integrate the blockchain technology within our prototype, along with making transactions using hbar. This was possible using a Python wrapper that converted the native Hedera Java SDK functions into Python versions. The front-end UI of the web application was created using HTML, CSS, and JavaScript by dynamically passing in data through Django views and API calls.

# ⚙️ What Technologies Did We Use?
- Python
- Django
- Blockchain APIs and SDKs (Hedera)
- MongoDB
- PyMongo
- HTML/CSS/JS

# Check Out Our Demo and Presentation Here:
https://youtu.be/xckR5hK_6rg

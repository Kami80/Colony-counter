# **Colony Counter & DNA Primer Suggestion**

**Short Description:**  
**Colony Counter & DNA Primer Suggestion** is a Django web application for microbiology projects. It allows users to upload bacterial plate images for automatic colony counting and provides DNA primer suggestions using the ChatGPT API. The dashboard is interactive and responsive, built with Bootstrap.  

---

## **✨ Features**

- **Colony Counter**  
  - 🧫 Upload bacterial plate images  
  - 🔢 Automatic counting of colonies  
  - 📊 Display results with charts and images on the dashboard  

- **DNA Primer Suggestion**  
  - 🧬 Enter DNA sequences in a form  
  - 💡 Get forward and reverse primer suggestions via OpenAI's ChatGPT API  
  - 🌡️ Includes melting temperature (Tm) and GC content  

- **Interactive Dashboard**  
  - 📱 Responsive design using Bootstrap 5  
  - 🎚️ Range slider filters and data visualization charts  

---

## **⚡ Installation**

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/colony-counter-dna.git
cd colony-counter-dna
```
2. **Create a virtual environment and install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. **Set up environment variables**
Create a .env file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run Django migrations**
```bash
python manage.py migrate
```

5. **Start the server**
```bash
python manage.py runserver
```

6. **Access the app**
Open your browser and navigate to:
```bash
http://127.0.0.1:8000/
```

## **🛠️ Usage***

**Colony Counter**

  - Upload an image of a bacterial plate to automatically count colonies

  - DNA Primer Suggestion

  - Enter a DNA sequence in the form and click Suggest Primer to receive primer recommendations

## **🧰 Technologies Used**

  - Django

  - Python (skimage, imageio, matplotlib, numpy)

  - OpenAI API (ChatGPT)

  - Bootstrap 5

  - HTML/CSS/JavaScript



## **🚀 Future Improvements**

  - Implement AI-based image processing for more accurate colony detection

  - Add export options for primer suggestions (CSV/Excel)

  - Add user authentication and history tracking

## **📄 License**

This project is licensed under the MIT License.

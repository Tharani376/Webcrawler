# 🔍 Mini Search Engine (Milestone 4 Project)

A simple yet powerful **Search Engine** built using **Python & FastAPI**, implementing core Information Retrieval concepts like **Inverted Indexing** and **TF-IDF Ranking**.

---

## 🚀 Features

✅ Fast search using inverted index
✅ TF-IDF based ranking system
✅ Clean and simple web interface
✅ Real-time search results
✅ Lightweight and easy to run

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Concepts Used:**

  * Inverted Index
  * TF-IDF Scoring
  * Information Retrieval

---

## 📂 Project Structure

```
Milestone4_SearchEngine/
│
├── api.py
├── search_engine.py
├── inverted_index.json
├── idf.json
│
├── templates/
│   └── index.html
│
└── pages/
    ├── page_1.html
    ├── page_2.html
    └── ...
```

---

## ⚙️ How to Run

1️⃣ Install dependencies

```
pip install fastapi uvicorn
```

2️⃣ Run the server

```
uvicorn api:app --reload
```

3️⃣ Open browser

```
http://127.0.0.1:8000
```

4️⃣ Enter a search query and view results 🎯

---

## 🔄 Workflow

1. Crawl web pages
2. Build inverted index
3. Compute TF-IDF scores
4. Store data in JSON files
5. FastAPI serves search API
6. Frontend fetches and displays results

---

## 📊 Sample Output

```
page_1.html - Score: 36.84
page_3.html - Score: 21.45
page_5.html - Score: 18.12
```

---

## 🎯 Learning Outcome

* Understood how search engines work
* Implemented ranking algorithms
* Built API using FastAPI
* Connected frontend with backend

---

## 💡 Future Improvements

* Add autocomplete suggestions
* Improve UI (Google-like design)
* Add snippet preview for results
* Deploy project online

---

## 👨‍💻 Author

**Tharani Thirupathi**
B.Tech Student | Aspiring Software Developer

---

⭐ If you like this project, give it a star!

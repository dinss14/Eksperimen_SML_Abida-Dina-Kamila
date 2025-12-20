# Eksperimen_SML_Abida-Dina-Kamila

Repository ini berisi **eksperimen dan otomatisasi data preprocessing** untuk dataset  
**Online Shoppers Purchasing Intention Dataset** sebagai bagian dari **Kriteria 1**  
submission kelas *Membangun Sistem Machine Learning (MSML)*.

Tahapan dalam repository ini mencakup:
- Eksplorasi dataset secara manual (EDA)
- Preprocessing data pada notebook eksperimen
- Konversi preprocessing menjadi script otomatis
- Otomatisasi preprocessing menggunakan **GitHub Actions (CI)**

---

## Dataset

**Nama Dataset**  
Online Shoppers Purchasing Intention Dataset

**Sumber**  
UCI Machine Learning Repository  
https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

**Tujuan**  
Memprediksi apakah seorang pengguna akan melakukan pembelian (`Revenue = True/1`)  
berdasarkan perilaku navigasi pada website e-commerce.

---

## Struktur Repository

Eksperimen_SML_Abida-Dina-Kamila
├── .github/workflows
│ └── preprocessing.yml
├── preprocessing
│ ├── Eksperimen_Abida-Dina-Kamila.ipynb
│ ├── automate_Abida-Dina-Kamila.py
│ └── online_shoppers_intention_preprocessing.csv
├── online_shoppers_intention_raw.csv
├── .gitignore
└── README.md


**Penjelasan folder/file utama:**
- `online_shoppers_intention_raw.csv`  
  Dataset mentah (raw) sebagai input preprocessing
- `preprocessing/Eksperimen_Abida-Dina-Kamila.ipynb`  
  Notebook eksperimen berisi:
  - Data loading
  - Exploratory Data Analysis (EDA)
  - Preprocessing manual
- `preprocessing/automate_Abida-Dina-Kamila.py`  
  Script Python untuk preprocessing otomatis
- `.github/workflows/preprocessing.yml`  
  Workflow GitHub Actions untuk menjalankan preprocessing secara otomatis
- `online_shoppers_intention_preprocessing.csv`  
  Dataset hasil preprocessing (train & test)

---

## Tahapan Eksperimen (Notebook)

Pada notebook `Eksperimen_Abida-Dina-Kamila.ipynb`, dilakukan tahapan berikut:
1. Memuat dataset
2. Exploratory Data Analysis (EDA)
3. Analisis distribusi target (`Revenue`)
4. Analisis fitur numerik dan kategorikal
5. Preprocessing:
   - Konversi tipe data
   - Train-test split (stratified)
   - StandardScaler untuk fitur numerik
   - OneHotEncoder untuk fitur kategorikal
6. Penggabungan dataset train dan test

---

## Otomatisasi Preprocessing

File `automate_Abida-Dina-Kamila.py` merupakan hasil konversi dari notebook eksperimen,
dengan tahapan preprocessing yang **identik**, namun dijalankan secara otomatis.

Output preprocessing:
- Dataset siap digunakan untuk tahap modeling
- Memiliki kolom:
  - Fitur hasil transformasi
  - `Revenue` sebagai target
  - `dataset_split` (`train` / `test`)

---

## Workflow CI (GitHub Actions)

Workflow `preprocessing.yml` akan berjalan ketika:
- Terjadi perubahan pada dataset raw
- Terjadi perubahan pada script preprocessing
- Workflow dijalankan secara manual (`workflow_dispatch`)

Tahapan workflow:
1. Checkout repository
2. Setup Python environment
3. Install dependencies
4. Menjalankan preprocessing otomatis
5. Verifikasi output dataset
6. Mengunggah dataset hasil preprocessing sebagai artefak

Workflow ini memastikan preprocessing selalu **reproducible dan otomatis**.

---

## Status Kriteria 1

✔ Data loading  
✔ Exploratory Data Analysis (EDA)  
✔ Preprocessing manual di notebook  
✔ Preprocessing otomatis melalui script  
✔ Workflow CI menggunakan GitHub Actions  

**Kriteria 1 – Advance (4 Poin)**

---

## Author

**Abida – Dina – Kamila**  
Submission Kelas: *Membangun Sistem Machine Learning*  

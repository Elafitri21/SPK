# UAS spk_web

## Install requirements

    pip install -r requirements.txt

## Run the app
to run the web app simply  use

    python main.py

## Usage
Install postman 
https://www.postman.com/downloads/

get buah list
<img src='img/get_buah.png' alt='buah list'/>

get recommendations saw
<img src='img/post_saw.png' alt='recommendations saw'/>

get recommendations wp
<img src='img/post_wp.png' alt='recommendations wp'/>

### TUGAS UAS
Implementasikan model yang sudah anda buat ke dalam web api dengan http method `POST`

INPUT:
{
    "Kualitas_Buah": 10, 
    "Harga": 5, 
    "Pelayanan": 5, 
    "Suasana": 5, 
    "Jarak": 5
}

OUTPUT (diurutkan / sort dari yang terbesar ke yang terkecil):

post recommendations saw
<img src='img/post_saw.png' alt='recommendations saw'/>

post recommendations wp
<img src='img/post_wp.png' alt='recommendations wp'/>
PGDMP  :                    {            tokobuah    16.0    16.0 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24857    tokobuah    DATABASE        CREATE DATABASE tokobuah WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE tokobuah;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    24858    tokobuahterbaik    TABLE       CREATE TABLE public.tokobuahterbaik (
    "No" character varying NOT NULL,
    "Nama_Toko" character varying NOT NULL,
    "Kualitas_Buah" integer NOT NULL,
    "Harga" integer NOT NULL,
    "Pelayanan" integer NOT NULL,
    "Suasana" integer NOT NULL,
    "Jarak" integer NOT NULL
);
 #   DROP TABLE public.tokobuahterbaik;
       public         heap    postgres    false    4            �          0    24858    tokobuahterbaik 
   TABLE DATA           w   COPY public.tokobuahterbaik ("No", "Nama_Toko", "Kualitas_Buah", "Harga", "Pelayanan", "Suasana", "Jarak") FROM stdin;
    public          postgres    false    215   �       P           2606    24898 $   tokobuahterbaik tokobuahterbaik_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.tokobuahterbaik
    ADD CONSTRAINT tokobuahterbaik_pkey PRIMARY KEY ("No");
 N   ALTER TABLE ONLY public.tokobuahterbaik DROP CONSTRAINT tokobuahterbaik_pkey;
       public            postgres    false    215            �   �   x�]���0Dg�+��i(#E!ec1��� '�{�Z�G���YdP�h�V��dAd��8 A�b"�}C�3^m\�Au�Ê�7|M��5�Ugd2嗚,B	R}ђI�Z~#U@�
j�p�7x}G4��i���p�ך%m�zl�_8�`��)�X������4W4ZA_:McodGV     
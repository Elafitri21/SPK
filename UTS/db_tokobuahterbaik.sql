PGDMP                  	    {            db_tokobuahterbaik    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397    db_tokobuahterbaik    DATABASE     �   CREATE DATABASE db_tokobuahterbaik WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Indonesian_Indonesia.1252';
 "   DROP DATABASE db_tokobuahterbaik;
                postgres    false            �            1259    16398    tokobuahterbaik    TABLE       CREATE TABLE public.tokobuahterbaik (
    "No" integer NOT NULL,
    "Nama_Toko" text NOT NULL,
    "Kualitas_Buah" text NOT NULL,
    "Harga_Rata_Rata_Buah" text NOT NULL,
    "Pelayanan" text NOT NULL,
    "Suasana" text NOT NULL,
    "Jarak" text NOT NULL
);
 #   DROP TABLE public.tokobuahterbaik;
       public         heap    postgres    false            �          0    16398    tokobuahterbaik 
   TABLE DATA           �   COPY public.tokobuahterbaik ("No", "Nama_Toko", "Kualitas_Buah", "Harga_Rata_Rata_Buah", "Pelayanan", "Suasana", "Jarak") FROM stdin;
    public          postgres    false    215   �                  2606    16404 $   tokobuahterbaik tokobuahterbaik_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.tokobuahterbaik
    ADD CONSTRAINT tokobuahterbaik_pkey PRIMARY KEY ("No");
 N   ALTER TABLE ONLY public.tokobuahterbaik DROP CONSTRAINT tokobuahterbaik_pkey;
       public            postgres    false    215            �   �   x����N�0E�㯘 ��Cj�H�$��L�UCR��E��`�T)ei[sϹ㉄;VN�=7o��PP�&�9��<�R��	e���rK�T�"ذ���΋+�i\(6�=��,N�1v1���"���P)�2e�_��|�`�4Y�_@���S綠b�ͳQ�G
Z�'r��Ƹ��G4�)h՞Z���n���~��#t��i��C�������7ϒ��r����þ�$�jM�7+��S&���D���ƃ     
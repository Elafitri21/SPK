from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Buah(Base):
    __tablename__ = 'tokobuahterbaik'
    No: Mapped[str] = mapped_column(primary_key=True)
    Nama_Toko: Mapped[str] = mapped_column()
    Kualitas_Buah: Mapped[int] = mapped_column()
    Harga: Mapped[int] = mapped_column()
    Pelayanan: Mapped[int] = mapped_column()
    Suasana: Mapped[int] = mapped_column()
    Jarak: Mapped[int] = mapped_column()  
    
    def __repr__(self) -> str:
        return f"Buah(No={self.No!r}, Harga={self.Harga!r})"

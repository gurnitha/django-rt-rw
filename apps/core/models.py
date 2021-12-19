# apps/rt09/models.py

# Django modules
from django.db import models

# Locals
from apps.desa.models import Desa
from apps.rw14.models import RW14  

# Create your models here.
  
  
class AbstractWargaModel(models.Model):  # COMM0N

    class Meta:
        abstract = True
        verbose_name = "Warga"
        verbose_name_plural = "Warga"

    # note:
    # 1. yatim/ yatim-piatu    
    # 2. pekerjaan
    # 3. data inheritance

    #> KTP ELEKTRONIK
    # Set the attributes
    PUNYA_E_EKP = 'P'
    TIDAK_PUNYA_E_EKP = 'TP'

    e_ktp_choices = [
        (PUNYA_E_EKP, 'Punya'), # <- 'Punya' Humans readable
        (TIDAK_PUNYA_E_EKP, 'Tidak punya'),
    ]

    # AGAMA
    # Set the attributes
    ISLAM     = 'Isl'
    KRISTEN = 'Kris'
    KATOLIK = 'Kat'
    HINDU   = 'Hin'
    KONGHUCU= 'Kong'
    LAINNYA = 'Lain'

    agama_choices = [
        (ISLAM, 'Islam'), # <- 'Islam' Humans readable
        (KRISTEN, 'Kristen'),
        (KATOLIK, 'Katolik'),
        (HINDU, 'Hindu'),
        (KONGHUCU, 'Konghucu'),
        (LAINNYA, 'Lainnya'),
    ]

    # GENDER
    # Set the attributes
    LAKI_LAKI = 'L'
    PEREMPUAN = 'P'
    LAIN = 'Lain'

    gender_choices = [
        (LAKI_LAKI, 'Laki'),
        (PEREMPUAN, 'Perempuan'),
        (LAIN, 'Lainnya')
    ]

    # PENDIDIKAN
    # Set the attributes
    TIDAK_DIKETAHUI = '-'
    SD     = 'SD'
    SMP = 'SMP/SETARA'
    SMU = 'SMU/SETARA'
    SMK = 'SMK'
    SARAJANA = 'S1'
    MASTER      = 'S2'
    DOKTOR   = 'S3'
    PROFESOR = 'PROF'

    pendidikan_choices = [
        (TIDAK_DIKETAHUI, 'Tidak diketahui'),
        (SD, 'SD'),
        (SMP, 'SMP/SETARA'),
        (SMU, 'SMU/SETARA'),
        (SMK, 'SMK'),
        (SARAJANA, 'Strata 1'),
        (MASTER, 'Strata 2'),
        (DOKTOR, 'Strata 3'),
        (PROFESOR, 'Prof')
    ]

    # STATUS PERKAWINAN
    # Set the attributes
    BELUM_MENIKAH = 'BM'
    SUDAH_MENIKAH = 'SM'
    JANDA           = 'JD'
    DUDA           = 'DD'

    status_perkawinan_choices = [
        (BELUM_MENIKAH, 'Belum menikah'),
        (SUDAH_MENIKAH, 'Menikah'),
        (JANDA, 'Janda'),
        (DUDA,'Duda')
    ]

    # STATUS HUB DALAM KELUARGA
    # Set the attributes
    KEPALA_KELUARGA = 'KK'
    SUAMI             = 'SU'
    ISTRI             = 'IS'
    ANAK_KANDUNG     = 'AK'
    ANAK_ANGKAT     = 'AA'
    ANAK_TIRI        = 'AI'

    status_hub_dlm_kel_choices = [
        (KEPALA_KELUARGA, 'Kepala Keluarga'),
        (SUAMI, 'Suami'),
        (ISTRI, 'Istri'),
        (ANAK_KANDUNG, 'Anak Kandung'),
        (ANAK_ANGKAT, 'Anak Angkat'),
        (ANAK_TIRI, 'Anak Tiri')
    ]


    # STATUS TEMPAT TINGGAL
    # Set the attributes
    RUMAH_SENDIRI = 'MILIK'
    RUMAH_ORANG_TUA = 'ORTU'
    SEWA       = 'SEWA'

    status_tempat_tinggal_choices = [
        (RUMAH_SENDIRI, 'Rumah milik'),
        (RUMAH_ORANG_TUA, 'Rumah orang tua'),
        (SEWA, 'Sewa')
    ]

    # STATUS KESEHATAN
    ## Kondisi Kesehatan Umum 
    # Set the attributes
    SANGAT_BAIK = 'SB'
    BAIK         = 'B'
    KURANG_BAIK = 'KB'

    kondisi_kesehatan_choices = [
        (SANGAT_BAIK, 'Sangat baik'),
        (BAIK, 'Baik'),
        (KURANG_BAIK, 'Kurang baik')
    ]

    ## Penyakit khusus
    # Set the attributes
    TIDAK_ADA     = 'TDK ADA'
    JANTUNG     = 'JTG'
    DIABITES     = 'DIABET'
    ASMA         = 'ASMA'
    PARU_PARU     = 'PARU'
    HIV_AIDS     = 'HIV'
    GINJAL         = 'GINJAL'

    penyakit_khusus_choices = [
        (TIDAK_ADA, 'Tidak ada'),
        (JANTUNG, 'Jantung'),
        (DIABITES, 'Diabet'),
        (ASMA, 'Asma'),
        (PARU_PARU, 'Paru'),
        (HIV_AIDS, 'Hiv'),
        (GINJAL, 'Ginjal'),
    ]

    # COVID

    #> Vaksinasi
    BELUM_DIVAKSIN = '0X'
    SUDAH_DIVAKSIN_1_KALI = '1X'
    SUDAH_DIVAKSIN_2_KALI = '2X'
    SUDAH_DIVAKSIN_BOSTER = 'BOSTER 1X'
    SUDAH_DIVAKSIN_BOSTER = 'BOSTER 2X'

    vaksin_choices = [
        (BELUM_DIVAKSIN, '0 kali'),
        (SUDAH_DIVAKSIN_1_KALI, '1 kali'),
        (SUDAH_DIVAKSIN_2_KALI, '2 kali'),
        (SUDAH_DIVAKSIN_BOSTER, 'Boster 1 kali'),
        (SUDAH_DIVAKSIN_BOSTER, 'Boster 2 kali'),
    ]

    # Set the attributes
    TIDAK_TERPAPAR         = 'TDK T'
    TERPAPAR_COVID_19   = 'TC19'
    TERPAPAR_VARIAN_DELTA= 'TVD'
    TERPAPAR_VARIAN_OMICRON= 'TVO'
    TERPAPAR_VARIAN_LAINNYA= 'TV Lainya'

    covid_choices = [
        (TIDAK_TERPAPAR, 'Tidak terpapar'),
        (TERPAPAR_COVID_19, 'Terpapar Covid-19'),
        (TERPAPAR_VARIAN_DELTA, 'Terpapar varian Delta'),
        (TERPAPAR_VARIAN_OMICRON, 'Terpapar varian Omicron'),
        (TERPAPAR_VARIAN_LAINNYA, 'Terpapar varian Lainnya'),
    ]

    # KONDISI STLH TERPAPAR COVID
    # Set the attributes
    TIDAK_TERPAPAR = '-'
    ISOLASI_MANDIRI = 'ISOMAN'
    ISOLASI_TERPUSAT = 'ISOTER'
    DIRAWAT_DI_RS     = 'DIRAWAT'
    PULIH_NORMAL     = 'PULIH'
    MENINGGAL          = 'MENINGGAL'

    kondisi_setelah_terpapar_choices = [
        (TIDAK_TERPAPAR, 'Tidak terpapar'),
        (ISOLASI_MANDIRI, 'Isolasi mandiri'),
        (ISOLASI_TERPUSAT, 'Isolasi terpusat'),
        (DIRAWAT_DI_RS, 'Dirawat di RS'),
        (PULIH_NORMAL, 'Pulih normal'),
        (MENINGGAL, 'Meninggal'),
    ]


    # KONDISI EKONOMI WARGA
    ## 1. Profesi
    # Set the attributes
    PEMULUNG     = 'Pemulung'
    TUKANG         = 'Tukang'
    OJEK         = 'Ojek'
    SOPIR         = 'Sopir'
    PETANI         = 'Petani'
    PEDAGANG_K5 = 'K5'
    PEDAGANG_WARUNG = 'Pedagang Warung'
    ART         = 'ART'
    ASN         = 'ASN'
    TNI         = 'TNI'
    POLISI         = 'Polisi'
    GURU         = 'Guru'
    DOSEN         = 'Dosen'
    PROFESIONAL = 'Profesional'
    WIRA_SWASTA = 'Wira Swasta'
    CONTENT_CREATOR = 'Content creator'
    CREATIVE     = 'Creative'
    PENSIUNAN     = 'Pensiunan'
    PEGAWAI_HONORER = 'Honorer'
    LAIN_LAIN     = 'Lain Lain'    
    
    profesi_choices = [    
        (PEMULUNG     , 'Pemulung'),
        (TUKANG     , 'Tukang'),
        (OJEK         , 'Ojek'),
        (SOPIR         , 'Sopir'),
        (PETANI     , 'Petani'),
        (PEDAGANG_K5 , 'K5'),
        (PEDAGANG_WARUNG , 'Pedagang warung'),
        (ART         , 'AST'),
        (ASN         , 'ASN'),
        (TNI         , 'TNI'),
        (POLISI     , 'Polisi'),
        (GURU         , 'Guru'),
        (DOSEN         , 'Dosen'),
        (PROFESIONAL , 'Profesional'),
        (WIRA_SWASTA , 'Wira Swasta'),
        (CONTENT_CREATOR , 'Content creator'),
        (CREATIVE , 'Creative'),
        (PENSIUNAN     , 'Pensiunan'),
        (PEGAWAI_HONORER , 'Honorer'),
        (LAIN_LAIN     , 'Lain lain')
    ]

    ## 2. Penghasilan per bulan 
    # Set the attributes
    KURANG_DARI_SATU_JUTA             = 'Kurang dari 1 Juta'
    KURANG_DARI_SATU_SETENGAH_JUTA     = 'Kurang dari 1,5 Juta'
    KURANG_DARI_DUA_JUTA             = 'Kurang dari 2 Juta'
    KURANG_DARI_DUA_SETENGAH_JUTA    = 'Kurang dari 2,5 Juta'
    KURANG_DARI_TIGA_JUTA             = 'Kurang dari 3 Juta'
    KURANG_DARI_TIGA_SETENGAH_JUTA    = 'Kurang dari 3,5 Juta'
    KURANG_DARI_EMPAT_JUTA             = 'Kurang dari 4 Juta'
    KURANG_DARI_LIMA_JUTA             = 'Kurang dari 5 Juta'
    KURANG_DARI_TUJUH_JUTA             = 'Kurang dari 7 Juta'
    KURAND_DARI_SEPULUH_JUTA         = 'Kurang dari 10 Juta'
    LEBIH_DARI_SEPULUH_JUTA         = 'Lebih dari 10 Juta'

    penghasilan_per_bulan_choices = [
        (KURANG_DARI_SATU_JUTA             , 'Kurang dari 1 juta'),
        (KURANG_DARI_SATU_SETENGAH_JUTA , ' Kurang dari 1,5 juta'),
        (KURANG_DARI_DUA_JUTA             , 'Kurang dari 2 juta'),
        (KURANG_DARI_DUA_SETENGAH_JUTA    , 'Kurang dari 2,5 juta'),
        (KURANG_DARI_TIGA_JUTA             , 'Kurang dari 3 juta'),
        (KURANG_DARI_TIGA_SETENGAH_JUTA    , 'Kurang dari 3,5 juta'),
        (KURANG_DARI_EMPAT_JUTA         , 'Kurang dari 4 juta'),
        (KURANG_DARI_LIMA_JUTA             , 'Kurang dari 5 juta'),
        (KURANG_DARI_TUJUH_JUTA         , 'Kurang dari 7 juta'),
        (KURAND_DARI_SEPULUH_JUTA         , 'Kurang dari 10 juta'),
        (LEBIH_DARI_SEPULUH_JUTA         , 'Lebih dari 10 juta')
    ]    

    ## 3. Jumlah anggota keluarga
    # Set the attributes
    SATU_ORANG         = '1 Orang'
    DUA_ORANG         = '2 Orang'
    TIGA_ORANG         = '3 Orang'
    EMPAT_ORANG     = '4 Orang'
    LIMA_ORANG         = '5 Orang'
    ENAM_ORANG         = '6 Orang'
    TUJUH_ORANG     = '7 Orang'
    DELAPAN_ORANG     = '8 Orang'
    SEMBILAN_ORANG     = '9 Orang'
    SEPULUH_ORANG     = '10 Orang'
    LEBIH_DARI_SEPULUH_ORANG = 'Lebih Dari 10 Orang'
    TIDAK_ADA         = 'Tidak ada'

    jumlah_angota_keluarga_choices = [
        (SATU_ORANG     , '1 orang'),
        (DUA_ORANG         , '2 orang'),
        (TIGA_ORANG     , '3 orang'),
        (EMPAT_ORANG     , '4 orang'),
        (LIMA_ORANG     , '5 orang'),
        (ENAM_ORANG     , '6 orang'),
        (TUJUH_ORANG     , '7 orang'),
        (DELAPAN_ORANG     , '8 orang'),
        (SEMBILAN_ORANG , '9 orang'),
        (SEPULUH_ORANG     , '10 orang'),
        (LEBIH_DARI_SEPULUH_ORANG , 'Lebih Dari 10 orang'),
        (TIDAK_ADA, 'Tidak ada')
    ]

    ## 4. Yatim 
    # Set the attributes
    YATIM_IBU     = 'Yatim Ibu'    
    YATIM_AYAH     = 'Yatim Ayah'    
    YATIM_PIATU = 'Yatim '
    BUKAN_YATIM         = 'Bukan'        

    yatim_choices = [
        (YATIM_IBU     , 'Yatim tanpa Ibu'),
        (YATIM_AYAH , 'Yatim tanpa Ayah'),
        (YATIM_PIATU, 'Yatim piatu'),
        (BUKAN_YATIM, 'Bukan yatim'),
    ]


    ## 4. Jenis rumah tempat tinggal
    # Set the attributes
    PETAKAN_LANTAI_TANAH     = 'Petakan Lantai Tanah'
    PETAKAN_LANTAI_SEMEN    = 'Petakan Lantai Semen'
    PETAKAN_LANTAI_KERAMIK     = 'Petakan Lantai Keramik'
    RUMAH_SEMI_PERMANEN     = 'Rumah Semi Permanen'
    RUMAH_PERMANEN             = 'Rumah Permanen' 

    jenis_rumah_tempat_tingal_choices = [
        (PETAKAN_LANTAI_TANAH     , 'Petakan Lantai Tanah'),
        (PETAKAN_LANTAI_SEMEN    , 'Petakan Lantai Semen'),
        (PETAKAN_LANTAI_KERAMIK , 'Petakan Lantai Keramik'),
        (RUMAH_SEMI_PERMANEN     , 'Rumah Semi Permanen'),
        (RUMAH_PERMANEN         , 'Rumah Permanen') 
    ]


    ## 5. Status rumah tempat tinggal
    # Set the attributes
    SEWA             = 'Sewa'
    MILIK_ORANG_TUA = 'Milik Orang Tua'
    MILIK_SENDIRI     = 'Milik Sendiri'

    status_rumah_tempat_tinggal_choices = [
        (SEWA             , 'Sewa'),
        (MILIK_ORANG_TUA , 'Milik Orang Tua'),
        (MILIK_SENDIRI     , 'Milik Sendiri')
    ]        

    #6 Status ekonomi
    SANGAT_SEJAHTERA = 'SS'
    SEJAHTERA          = 'S'
    PRA_SEJAHTERA      = 'PS'
    TDK_SEJAHTERA      = 'TS'

    status_ekonomi_choices = [
        (SANGAT_SEJAHTERA, 'Sangat sejahtera'),
        (SEJAHTERA, 'Sejahtera'),
        (PRA_SEJAHTERA, 'Pra sejahtera'),
        (TDK_SEJAHTERA, 'Tidak sejahtera')
    ]


    """---------------KOLOM TABEL---------------------"""

    """IDENTITAS UTAMA WARGA"""
    nama_lengkap       = models.CharField(
                        max_length=100,
                        help_text='Harus diisi.')
    nama_panggilan     = models.CharField(
                        max_length=30,
                        help_text='Harus diisi.')
    e_ktp     = models.CharField(
                        max_length=10,
                        choices=e_ktp_choices,
                        default=PUNYA_E_EKP,
                        help_text='Klik tanda panah.')
    nik                = models.CharField(
                        max_length=20,
                        help_text='Harus diisi.')
    hp                = models.CharField(
                        max_length=20, 
                        blank=True,
                        help_text='Boleh dikosongkan.')
    
    
    """IDENTITAS TAMBAHAN WARGA"""
    gender      = models.CharField(
                        max_length=10,
                        choices=gender_choices,
                        default=LAKI_LAKI,
                        help_text='Klik tanda panah.')
    tempat_lahir       = models.CharField(
                        max_length=50, 
                        blank=True,
                        help_text='Contoh: Denpasar, Bali atau Boleh dikosongkan.')
    tanggal_lahir   = models.CharField(
                        max_length=12, 
                        blank=True,
                        help_text='Contoh: 01/01/2001 atau Boleh dikosongkan.')
    agama              = models.CharField(
                        max_length=10,
                        choices=agama_choices,
                        default=ISLAM,
                        help_text='Klik tanda panah.')
    pendidikan     = models.CharField(
                        max_length=10,
                        choices=pendidikan_choices,
                        default=SMU,
                        help_text='Klik tanda panah.')
    # jenis_pekerjaan = models.CharField(
    #                     max_length=20,
    #                     choices=jenis_pekerjaan_choices,
    #                     help_text='Klik tanda panah.')
    status_perkawinan     = models.CharField(
                        max_length=10,
                        choices=status_perkawinan_choices,
                        default=SUDAH_MENIKAH,
                        help_text='Klik tanda panah.')
    status_hub_dlm_kel     = models.CharField(
                        max_length=30,
                        choices=status_hub_dlm_kel_choices,
                        default=KEPALA_KELUARGA,
                        help_text='Klik tanda panah.')
    nama_ibu         = models.CharField(
                        max_length=50, 
                        blank=True,
                        help_text='Boleh dikosongkan.')
    nama_ayah         = models.CharField(
                        max_length=50, 
                        blank=True,
                        help_text='Boleh dikosongkan.')
    yatim     = models.CharField(
                        max_length=30,
                        choices=yatim_choices,
                        default=BUKAN_YATIM,
                        blank=True, null=True,
                        help_text='Klik tanda panah.')

    """TEMPAT TINGGAL WARGA"""
    alamat_tempat_tinggal     = models.TextField(
                                help_text='Tidak boleh dikosongkan.')

    """KESEHATAN UMUM"""
    kondisi_kesehatan     = models.CharField(
                            max_length=30,
                            choices=kondisi_kesehatan_choices, 
                            default=BAIK,
                            help_text='Klik tanda panah.')
    penyakit_khusus     = models.CharField(
                            max_length=30,
                            choices=penyakit_khusus_choices,
                            default=TIDAK_ADA,
                            help_text='Klik tanda panah.')


    # KHUSUS COVID
    vaksin                  = models.CharField(
                            max_length=30,
                            choices=vaksin_choices,
                            default=SUDAH_DIVAKSIN_2_KALI,
                            help_text='Klik tanda panah.')
    covid                  = models.CharField(
                            max_length=30,
                            choices=covid_choices,
                            default=TIDAK_TERPAPAR,
                            help_text='Klik tanda panah.')
    tgl_terpapar         = models.CharField(
                            max_length=30,
                            blank=True, null=True,
                            help_text='Terpapar tulis mis: 01/05/2021, Tdk terpapar tulis: -')
    gejala_saat_terpapar= models.TextField(
                            blank=True,
                            help_text='Boleh dikosongkan.')
    status_perawatan = models.CharField(
                            max_length=30,
                            choices=kondisi_setelah_terpapar_choices,
                            default=PULIH_NORMAL,
                            help_text='Klik tanda panah.')


    # KONDISI EKONOMI WARGA
    profesi             = models.CharField(
                            max_length=30,
                            choices=profesi_choices,
                            default=WIRA_SWASTA,
                            help_text='Klik tanda panah.')    

    penghasilan_per_bulan     = models.CharField(
                            max_length=30,
                            choices=penghasilan_per_bulan_choices,
                            default=KURANG_DARI_SATU_SETENGAH_JUTA,
                            help_text='Klik tanda panah.')    

    jumlah_anggota_keluarga = models.CharField(
                            max_length=30,
                            choices=jumlah_angota_keluarga_choices,
                            default=EMPAT_ORANG,
                            help_text='Klik tanda panah.')    
    
    jenis_rumah_tempat_tingal = models.CharField(
                            max_length=30,
                            choices=jenis_rumah_tempat_tingal_choices,
                            default=PETAKAN_LANTAI_SEMEN,
                            help_text='Klik tanda panah.')    

    status_rumah_tempat_tinggal = models.CharField(
                            max_length=30,
                            choices=status_rumah_tempat_tinggal_choices,
                            default=MILIK_ORANG_TUA,
                            help_text='Klik tanda panah.')    

    status_ekonomi = models.CharField(
                            max_length=50,
                            choices=status_ekonomi_choices,
                            default=SEJAHTERA,
                            help_text='Tdk sejahtera jika: 1. Rp < 1.5 jt p/bln; 2. Tanggungan 4 orang; dan 3. Rumah bkn milik sendiri. Klik tanda panah.')

    saat_dibuat = models.DateTimeField(auto_now_add=True)
    saat_diubah = models.DateTimeField(auto_now=True)

    """KEWARGAAN DESA/RW/RT"""
    desa = models.ForeignKey(
                        Desa, 
                        on_delete=models.CASCADE,
                        help_text='Klik tanda panah.')
    rw = models.ForeignKey(
                        RW14, 
                        on_delete=models.CASCADE,
                        help_text='Klik tanda panah.')
    # rt = models.ForeignKey(
    #                     RT09, 
    #                     on_delete=models.CASCADE,
    #                     help_text='Klik tanda panah.')
    def __str__(self):
        return self.nama_lengkap

  

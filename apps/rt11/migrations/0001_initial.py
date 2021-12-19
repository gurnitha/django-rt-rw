# Generated by Django 3.2 on 2021-12-19 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desa', '0001_initial'),
        ('rw14', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RT11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_rt', models.CharField(max_length=50)),
                ('nama_ketua', models.CharField(max_length=50)),
                ('alamat_rt', models.CharField(max_length=100)),
                ('hp', models.CharField(blank=True, max_length=20, null=True)),
                ('telpon', models.CharField(blank=True, max_length=20, null=True)),
                ('desa', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='desa.desa')),
                ('rw', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='rw14.rw14')),
            ],
            options={
                'verbose_name': 'RT 11',
                'verbose_name_plural': 'RT 11',
            },
        ),
        migrations.CreateModel(
            name='Wargart11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(help_text='Harus diisi.', max_length=100)),
                ('nama_panggilan', models.CharField(help_text='Harus diisi.', max_length=30)),
                ('e_ktp', models.CharField(choices=[('P', 'Punya'), ('TP', 'Tidak punya')], default='P', help_text='Klik tanda panah.', max_length=10)),
                ('nik', models.CharField(help_text='Harus diisi.', max_length=20)),
                ('hp', models.CharField(blank=True, help_text='Boleh dikosongkan.', max_length=20)),
                ('gender', models.CharField(choices=[('L', 'Laki'), ('P', 'Perempuan'), ('Lain', 'Lainnya')], default='L', help_text='Klik tanda panah.', max_length=10)),
                ('tempat_lahir', models.CharField(blank=True, help_text='Contoh: Denpasar, Bali atau Boleh dikosongkan.', max_length=50)),
                ('tanggal_lahir', models.CharField(blank=True, help_text='Contoh: 01/01/2001 atau Boleh dikosongkan.', max_length=12)),
                ('agama', models.CharField(choices=[('Isl', 'Islam'), ('Kris', 'Kristen'), ('Kat', 'Katolik'), ('Hin', 'Hindu'), ('Kong', 'Konghucu'), ('Lain', 'Lainnya')], default='Isl', help_text='Klik tanda panah.', max_length=10)),
                ('pendidikan', models.CharField(choices=[('-', 'Tidak diketahui'), ('SD', 'SD'), ('SMP/SETARA', 'SMP/SETARA'), ('SMU/SETARA', 'SMU/SETARA'), ('SMK', 'SMK'), ('S1', 'Strata 1'), ('S2', 'Strata 2'), ('S3', 'Strata 3'), ('PROF', 'Prof')], default='SMU/SETARA', help_text='Klik tanda panah.', max_length=10)),
                ('status_perkawinan', models.CharField(choices=[('BM', 'Belum menikah'), ('SM', 'Menikah'), ('JD', 'Janda'), ('DD', 'Duda')], default='SM', help_text='Klik tanda panah.', max_length=10)),
                ('status_hub_dlm_kel', models.CharField(choices=[('KK', 'Kepala Keluarga'), ('SU', 'Suami'), ('IS', 'Istri'), ('AK', 'Anak Kandung'), ('AA', 'Anak Angkat'), ('AI', 'Anak Tiri')], default='KK', help_text='Klik tanda panah.', max_length=30)),
                ('nama_ibu', models.CharField(blank=True, help_text='Boleh dikosongkan.', max_length=50)),
                ('nama_ayah', models.CharField(blank=True, help_text='Boleh dikosongkan.', max_length=50)),
                ('yatim', models.CharField(blank=True, choices=[('Yatim Ibu', 'Yatim tanpa Ibu'), ('Yatim Ayah', 'Yatim tanpa Ayah'), ('Yatim ', 'Yatim piatu'), ('Bukan', 'Bukan yatim')], default='Bukan', help_text='Klik tanda panah.', max_length=30, null=True)),
                ('alamat_tempat_tinggal', models.TextField(help_text='Tidak boleh dikosongkan.')),
                ('kondisi_kesehatan', models.CharField(choices=[('SB', 'Sangat baik'), ('B', 'Baik'), ('KB', 'Kurang baik')], default='B', help_text='Klik tanda panah.', max_length=30)),
                ('penyakit_khusus', models.CharField(choices=[('TDK ADA', 'Tidak ada'), ('JTG', 'Jantung'), ('DIABET', 'Diabet'), ('ASMA', 'Asma'), ('PARU', 'Paru'), ('HIV', 'Hiv'), ('GINJAL', 'Ginjal')], default='Tidak ada', help_text='Klik tanda panah.', max_length=30)),
                ('vaksin', models.CharField(choices=[('0X', '0 kali'), ('1X', '1 kali'), ('2X', '2 kali'), ('BOSTER 2X', 'Boster 1 kali'), ('BOSTER 2X', 'Boster 2 kali')], default='2X', help_text='Klik tanda panah.', max_length=30)),
                ('covid', models.CharField(choices=[('TDK T', 'Tidak terpapar'), ('TC19', 'Terpapar Covid-19'), ('TVD', 'Terpapar varian Delta'), ('TVO', 'Terpapar varian Omicron'), ('TV Lainya', 'Terpapar varian Lainnya')], default='-', help_text='Klik tanda panah.', max_length=30)),
                ('tgl_terpapar', models.CharField(blank=True, help_text='Terpapar tulis mis: 01/05/2021, Tdk terpapar tulis: -', max_length=30, null=True)),
                ('gejala_saat_terpapar', models.TextField(blank=True, help_text='Boleh dikosongkan.')),
                ('status_perawatan', models.CharField(choices=[('-', 'Tidak terpapar'), ('ISOMAN', 'Isolasi mandiri'), ('ISOTER', 'Isolasi terpusat'), ('DIRAWAT', 'Dirawat di RS'), ('PULIH', 'Pulih normal'), ('MENINGGAL', 'Meninggal')], default='PULIH', help_text='Klik tanda panah.', max_length=30)),
                ('profesi', models.CharField(choices=[('Pemulung', 'Pemulung'), ('Tukang', 'Tukang'), ('Ojek', 'Ojek'), ('Sopir', 'Sopir'), ('Petani', 'Petani'), ('K5', 'K5'), ('Pedagang Warung', 'Pedagang warung'), ('ART', 'AST'), ('ASN', 'ASN'), ('TNI', 'TNI'), ('Polisi', 'Polisi'), ('Guru', 'Guru'), ('Dosen', 'Dosen'), ('Profesional', 'Profesional'), ('Wira Swasta', 'Wira Swasta'), ('Content creator', 'Content creator'), ('Creative', 'Creative'), ('Pensiunan', 'Pensiunan'), ('Honorer', 'Honorer'), ('Lain Lain', 'Lain lain')], default='Wira Swasta', help_text='Klik tanda panah.', max_length=30)),
                ('penghasilan_per_bulan', models.CharField(choices=[('Kurang dari 1 Juta', 'Kurang dari 1 juta'), ('Kurang dari 1,5 Juta', ' Kurang dari 1,5 juta'), ('Kurang dari 2 Juta', 'Kurang dari 2 juta'), ('Kurang dari 2,5 Juta', 'Kurang dari 2,5 juta'), ('Kurang dari 3 Juta', 'Kurang dari 3 juta'), ('Kurang dari 3,5 Juta', 'Kurang dari 3,5 juta'), ('Kurang dari 4 Juta', 'Kurang dari 4 juta'), ('Kurang dari 5 Juta', 'Kurang dari 5 juta'), ('Kurang dari 7 Juta', 'Kurang dari 7 juta'), ('Kurang dari 10 Juta', 'Kurang dari 10 juta'), ('Lebih dari 10 Juta', 'Lebih dari 10 juta')], default='Kurang dari 1,5 Juta', help_text='Klik tanda panah.', max_length=30)),
                ('jumlah_anggota_keluarga', models.CharField(choices=[('1 Orang', '1 orang'), ('2 Orang', '2 orang'), ('3 Orang', '3 orang'), ('4 Orang', '4 orang'), ('5 Orang', '5 orang'), ('6 Orang', '6 orang'), ('7 Orang', '7 orang'), ('8 Orang', '8 orang'), ('9 Orang', '9 orang'), ('10 Orang', '10 orang'), ('Lebih Dari 10 Orang', 'Lebih Dari 10 orang'), ('Tidak ada', 'Tidak ada')], default='4 Orang', help_text='Klik tanda panah.', max_length=30)),
                ('jenis_rumah_tempat_tingal', models.CharField(choices=[('Petakan Lantai Tanah', 'Petakan Lantai Tanah'), ('Petakan Lantai Semen', 'Petakan Lantai Semen'), ('Petakan Lantai Keramik', 'Petakan Lantai Keramik'), ('Rumah Semi Permanen', 'Rumah Semi Permanen'), ('Rumah Permanen', 'Rumah Permanen')], default='Petakan Lantai Semen', help_text='Klik tanda panah.', max_length=30)),
                ('status_rumah_tempat_tinggal', models.CharField(choices=[('Sewa', 'Sewa'), ('Milik Orang Tua', 'Milik Orang Tua'), ('Milik Sendiri', 'Milik Sendiri')], default='Milik Orang Tua', help_text='Klik tanda panah.', max_length=30)),
                ('status_ekonomi', models.CharField(choices=[('SS', 'Sangat sejahtera'), ('S', 'Sejahtera'), ('PS', 'Pra sejahtera'), ('TS', 'Tidak sejahtera')], default='S', help_text='Tdk sejahtera jika: 1. Rp < 1.5 jt p/bln; 2. Tanggungan 4 orang; dan 3. Rumah bkn milik sendiri. Klik tanda panah.', max_length=50)),
                ('saat_dibuat', models.DateTimeField(auto_now_add=True)),
                ('saat_diubah', models.DateTimeField(auto_now=True)),
                ('desa', models.ForeignKey(help_text='Klik tanda panah.', on_delete=django.db.models.deletion.CASCADE, to='desa.desa')),
                ('rt', models.ForeignKey(help_text='Klik tanda panah.', on_delete=django.db.models.deletion.CASCADE, to='rt11.rt11')),
                ('rw', models.ForeignKey(help_text='Klik tanda panah.', on_delete=django.db.models.deletion.CASCADE, to='rw14.rw14')),
            ],
            options={
                'verbose_name': 'Warga',
                'verbose_name_plural': 'Warga',
                'abstract': False,
            },
        ),
    ]
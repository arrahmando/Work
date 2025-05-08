#ifndef datasetV3L_H
#define datasetV3L_H
#include <Arduino.h>

class dataset{
    public:
        int baris,kolom;
        byte wajah[39] [59];
        kanan_atas1();
        kanan_atas2();
        kanan_atas3();
        kanan_atas4();
        kanan_atas5();

        kanan_tengah1();
        kanan_tengah2();
        kanan_tengah3();
        kanan_tengah4();
        kanan_tengah5();

        kanan_bawah1();
        kanan_bawah2();
        kanan_bawah3();
        kanan_bawah4();
        kanan_bawah5();

        kiri_atas1();
        kiri_atas2();
        kiri_atas3();
        kiri_atas4();
        kiri_atas5();

        kiri_tengah1();
        kiri_tengah2();
        kiri_tengah3();
        kiri_tengah4();
        kiri_tengah5();

        kiri_bawah1();
        kiri_bawah2();
        kiri_bawah3();
        kiri_bawah4();
        kiri_bawah5();

        tengah_atas1();
        tengah_atas2();
        tengah_atas3();
        tengah_atas4();
        tengah_atas5();

        tengah_tengah1();
        tengah_tengah2();
        tengah_tengah3();
        tengah_tengah4();
        tengah_tengah5();

        tengah_bawah1();
        tengah_bawah2();
        tengah_bawah3();
        tengah_bawah4();
        tengah_bawah5();
};
#endif
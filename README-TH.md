# Exploring COVID-19 Data in US Counties

[![Quality Gate Status][Quality Gate badge]][Quality Gate url]
[![Code Smells][Code Smells badge]][Code Smells url]
[![codecov][codecov badge]][codecov url]


> **For `README.md` in English, please see [README.md](.github/README.md)**

ข้อมูล [Coronavirus Covid-19](https://www.kaggle.com/datasets/yasirabdaali/corona-virus-covid19-us-counties)
เป็นชุดข้อมูลที่รวบรวมข้อมูลการติดเชื้อโควิด-19 ในประเทศสหรัฐอเมริกา โดยมีข้อมูลดังนี้

- วันที่บันทึกข้อมูล
- FIPS (Federal Information Processing Standards) รหัสที่ใช้ระบุเมือง / รัฐ
- จำนวนผู้ติดเชื้อยืนยัน
- จำนวนผู้เสียชีวิต
- เมือง / รัฐที่ทำการบันทึกข้อมูล
- ตำแหน่งที่ตั้ง (`Latitude (ละติจูด)` , `Longitude (ลองจิจูด)`)


## สามาชิก

- นาย กังวานทรัพย์ แซ่ลี้ (ก้อง)
    - files ที่รับผิดชอบ [here](docs/job/KonGKerDvD)
- นาย ปองภพ เชื้อประเสริฐศักดิ์ (พัตเตอร์)
    - files ที่รับผิดชอบ [here](docs/job/PutterTh)
- นาย ชัยภัทร ใจน่าน (ไอซ์)
    - files ที่รับผิดชอบ [here](docs/job/AppleBoiy)

## Acknowledgements

การใช้ชุดข้อมูล `yasirabdaali/corona-virus-covid19-us-counties`
ในโปรเจคนี้ขึ้นอยู่กับข้อกำหนดและเงื่อนไขของการอนุญาตของชุดข้อมูลเอง
ตามที่ระบุใน [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

การใช้งานโค้ดในโปรเจคนี้เพื่อวัตถุประสงค์การศึกษา สามารถนำไปใช้งาน แก้ไข
และแจกจ่ายต่อได้โดยไม่มีข้อจำกัด `แต่กรุณาให้เครดิตแก่ผู้เขียนโค้ดด้วยนะครับ`

### Disclaimer:

ผู้เขียนโปรเจค (Covid-19US-CS203) ต้องการให้ความสำคัญกับการอ้างอิงแหล่งข้อมูล และไม่รับผิดชอบใดๆ ทั้งสิ้น
ในกรณีที่เกิดข้อพิพาทหรือปัญหาใดๆ จากการใช้งานข้อมูล ผู้ใช้งานควรปฏิบัติตามข้อกำหนดและเงื่อนไขการใช้งานของแหล่งข้อมูล
และให้ความเคารพต่อผู้สร้างข้อมูลเสมอ

แหล่งข้อมูล: [Kaggle: yasirabdaali/corona-virus-covid19-us-counties](https://www.kaggle.com/datasets/yasirabdaali/corona-virus-covid19-us-counties).

---
Get help: [Post in our discussion board](https://github.com/AppleBoiy/Covid-19US-CS203/discussions)

&copy; 2023 AppleBoiy &bull; [Code of Conduct](.github/CODE_OF_CONDUCT.md) &bull; [CC-BY-SA-4.0](LICENSE)


<!-- external links -->

[CMU url]: https://www.cmu.ac.th/en/

[CSCMU url]: http://cs.science.cmu.ac.th/en/

[Dataset url]: https://www.kaggle.com/datasets/yasirabdaali/corona-virus-covid19-us-counties

[Yasir Kaggle]: https://www.kaggle.com/yasirabd

[Kaggle]: https://www.kaggle.com/

[CC0: Public Domain]: https://creativecommons.org/publicdomain/zero/1.0/

<!-- badges -->

[Quality Gate badge]: https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_Covid-19US-CS203&metric=alert_status

[Quality Gate url]: https://sonarcloud.io/summary/new_code?id=AppleBoiy_Covid-19US-CS203

[Code Smells badge]: https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_Covid-19US-CS203&metric=code_smells

[Code Smells url]: https://sonarcloud.io/summary/new_code?id=AppleBoiy_Covid-19US-CS203

[codecov badge]: https://codecov.io/gh/AppleBoiy/cs203-covid19-analysis-2023/branch/main/graph/badge.svg

[codecov url]: https://codecov.io/gh/AppleBoiy/cs203-covid19-analysis-2023

[Testing and Linting badge]: https://github.com/AppleBoiy/cs203-covid19-analysis-2023/actions/workflows/testing-linting.yml/badge.svg

[Testing and Linting url]: https://github.com/AppleBoiy/cs203-covid19-analysis-2023/actions/workflows/testing-linting.yml

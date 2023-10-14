# Exploring COVID-19 Data in US Counties

[![Quality Gate Status][Quality Gate badge]][Quality Gate url]
[![Code Smells][Code Smells badge]][Code Smells url]
[![codecov][codecov badge]][codecov url]

[//]: # (![The ranking of US counties &#40;sorted by total confirmed cases&#41; from 2020 to 2022]&#40;../resource/etc/sort_by_total_confirm.png&#41;)

[//]: # (> The graph above shows the ranking of US counties &#40;sorted by total confirmed cases&#41; from 2020 to 2022.)

> For my teacher, please see [thai version][thai version].

## Introduction

This project is a part of CS203[^1], designed for computer science students, including the project authors[^2].
Its primary objective is to provide a comprehensive learning experience,
with a specific focus on mastering the foundational principles of data science.

## Dataset Overview

[Corona Virus Covid-19 US Counties dataset][Dataset url][^3] contains essential information related to the COVID-19
pandemic in various administrative regions.
The data was collected between 2020 and 2022 (and not updated since then).

### Data Fields

- **Admin 2 FIPS Code**: A unique identifier for the administrative region.
- **Province/State**: The name of the province or state where the data was recorded.
- **Admin 2 Level**: The administrative level, which could refer to a city, county, borough, or region.
- **Date**: The date of the recorded data.
- **Total Death**: The total number of COVID-19-related deaths reported on the specified date.
- **Total Confirmed**: The total number of confirmed COVID-19 cases reported on the specified date.
- **Location**: Geographical coordinates (longitude and latitude) representing the location of the administrative
  region.

## Contributors

- **Kungwansup Saelee** [`KonGKerDvD`](https://github.com/KonGKerDvD)
- **Pongpop Chueprasertsak** [`PutterTh`](https://github.com/PutterTh)
- **Chaipat Jainan** [`AppleBoiy`](https://github.com/AppleBoiy)

## Disclaimer

[The authors of this project](#contributors)[^2] wish to make it clear that they do not claim ownership of the
dataset[^3].    
They[^2] assume no responsibility for any disputes or issues that may arise from its usage.
Users are strongly encouraged to adhere to the licensing terms of the dataset and,
when necessary, provide appropriate attribution to the dataset creators.

### Additional Resources

For additional references and resources, please check the [refs.md](../docs/refs.md) file.

- [FAQ](../code/Z_playground/docs/FAQ.md): Frequently asked questions and answers.
- [Discussion Board](https://github.com/AppleBoiy/Covid-19US-CS203/discussions): Get help and engage with the project
  community.

&copy; AppleBoiy &bull; [Code of Conduct](../.github/CODE_OF_CONDUCT.md) &bull; [MIT](../LICENSE)



<!-- footnotes -->

[^1]: CS203 is a course offered within
the [Department of Computer Science, Faculty of Science at Chiang Mai University][CSCMU url].
[^2]: The individuals who made significant contributions pivotal to the development and success of this project are
acknowledged as authors. For a comprehensive and detailed list of all contributors, please refer to the
dedicated [Contributors](#contributors) section.
[^3]: The dataset used in this project, titled ["Corona Virus Covid-19 US Counties"][Dataset url],
is open-source and provided by [Yasir Raza][Yasir Kaggle] via [Kaggle][Kaggle].
It is distributed under the [CC0: Public Domain][CC0: Public Domain] license.


<!-- external links -->

[CMU url]: https://www.cmu.ac.th/en/

[CSCMU url]: http://cs.science.cmu.ac.th/en/

[Dataset url]: https://www.kaggle.com/datasets/yasirabdaali/corona-virus-covid19-us-counties

[Yasir Kaggle]: https://www.kaggle.com/yasirabd

[Kaggle]: https://www.kaggle.com/

[CC0: Public Domain]: https://creativecommons.org/publicdomain/zero/1.0/

[thai version]: https://github.com/AppleBoiy/cs203-c19-analysis/blob/main/readme.md

<!-- badges -->

[Quality Gate badge]: https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_Covid-19US-CS203&metric=alert_status

[Quality Gate url]: https://sonarcloud.io/summary/new_code?id=AppleBoiy_Covid-19US-CS203

[Code Smells badge]: https://sonarcloud.io/api/project_badges/measure?project=AppleBoiy_Covid-19US-CS203&metric=code_smells

[Code Smells url]: https://sonarcloud.io/summary/new_code?id=AppleBoiy_Covid-19US-CS203

[codecov badge]: https://codecov.io/gh/AppleBoiy/cs203-covid19-analysis-2023/branch/main/graph/badge.svg

[codecov url]: https://codecov.io/gh/AppleBoiy/cs203-covid19-analysis-2023

[Testing and Linting badge]: https://github.com/AppleBoiy/cs203-covid19-analysis-2023/actions/workflows/testing-linting.yml/badge.svg

[Testing and Linting url]: https://github.com/AppleBoiy/cs203-covid19-analysis-2023/actions/workflows/testing-linting.yml

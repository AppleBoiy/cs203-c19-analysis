# Exploring COVID-19 Data in US Counties

[![Testing and Linting][Testing and Linting badge]][Testing and Linting url]
[![Quality Gate Status][Quality Gate badge]][Quality Gate url]
[![Code Smells][Code Smells badge]][Code Smells url]
[![codecov][codecov badge]][codecov url]

[//]: # (![The ranking of US counties &#40;sorted by total confirmed cases&#41; from 2020 to 2022]&#40;../resource/etc/sort_by_total_confirm.png&#41;)

[//]: # (> The graph above shows the ranking of US counties &#40;sorted by total confirmed cases&#41; from 2020 to 2022.)

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
- **Location**: Geographical coordinates (latitude and longitude) representing the location of the administrative
  region.

## Prerequisites

Before utilizing this dataset[^3], ensure you have the necessary prerequisites in place.
Detailed instructions for setup can be found in the [prerequisites.md](../docs/prerequisites.md).
These prerequisites are essential to efficiently work with the data and leverage the project effectively.

## Thai Language README

For Thai speakers, we provide a dedicated README in the Thai language.
Please refer to [README-TH.md](README-TH.md) for the Thai version of this documentation.

## Contributors

- **Kungwansup Saelee** [`KonGKerDvD`](https://github.com/KonGKerDvD)
- **Pongpop Chueprasertsak** [`PutterTh`](https://github.com/PutterTh)
- **Chaipat Jainan** [`AppleBoiy`](https://github.com/AppleBoiy)

## Disclaimer

[The authors of this project](#contributors)[^2] wish to make it clear that they do not claim ownership of the
dataset[^3].    
They[^2] assume no responsibility for any disputes or issues that may arise from its usage.
Users are strongly encouraged to adhere to the licensing terms of the dataset and,
when necessary, provide appropriate attribution to the dataset creators[^4].

### Additional Resources

For additional references and resources, please check the [refs.md](../docs/refs.md) file.

- [FAQ](../docs/FAQ.md): Frequently asked questions and answers.
- [Discussion Board](https://github.com/AppleBoiy/Covid-19US-CS203/discussions): Get help and engage with the project
  community.

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
  © 2023
  <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/AppleBoiy">
  AppleBoiy 
  </a> &bull; 
  <a href="https://github.com/AppleBoiy/cs203-covid19-analysis-2023/blob/main/.github/CODE_OF_CONDUCT.md" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">
  Code of Conduct
  </a> &bull;
  <a href="http://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">
  CC-BY-SA 4.0
  </a>
</p>



<!-- footnotes -->

[^1]: CS203 is a course offered within
the [Department of Computer Science, Faculty of Science at Chiang Mai University][CSCMU url].
[^2]: The individuals who made significant contributions pivotal to the development and success of this project are
acknowledged as authors. For a comprehensive and detailed list of all contributors, please refer to the
dedicated [Contributors](#contributors) section.
[^3]: The dataset used in this project, titled ["Corona Virus Covid-19 US Counties"][Dataset url],
is open-source and provided by [Yasir Raza][Yasir Kaggle][^4] via [Kaggle][Kaggle].
It is distributed under the [CC0: Public Domain][CC0: Public Domain][^6] license.
[^4]: [Yasir Raza][Yasir Kaggle], an expert on [Kaggle][Kaggle][^5], is the original dataset creator.
[^5]: [Kaggle][Kaggle] is a data science competition platform and online community of data scientists and machine
learning practitioners
under [Google LLC](https://en.wikipedia.org/wiki/Google).
[^6]: The [CC0: Public Domain][CC0: Public Domain] license signifies a generous dedication by the authors to the public
domain.
It allows creators to relinquish all rights to their works, making them freely available for any purpose, including
commercial use,
without any encumbrances.

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

# SKN011-4th-1Team

## 1. Team Members
### 팀명 : ♨️남탕♨️

|Name|Github Link|
|---|---|
|배정수|bail4877@gmail.com|
|이상준|haides1998@gmail.com|
|이선호|dkdlatjsh@gmail.com|
|정민호|[@Minor1862](https://github.com/Minor1862)|
|김정원|[@Kimjeongwon12](https://github.com/Kimjeongwon12)|

## 2. 프로젝트 개요
### 프로젝트 명
✅ 친환경 자동차 관련 정보 제공 시스템
### 프로젝트 소개
✅ 전국 자동차 등록 현황 대비 친환경차의 비율을 도출하고, 전기,수소 충전소 인프라 확충과 관련하여 충전소 설치 현황을 시각화, 기업의 faq를 조회하여 사용자에게 보여줄 수 있는 시스템을 구축하는 프로젝트
### 프로젝트 필요성(배경)
✅ 지구온난화 등 환경오염에 대한 인류의 경각심이 점점 올라감에 따라 화석연료를 사용하는 기존의 내연기관 자동차를 대체하고자 하는 친환경적인 연료를 사용하는 자동차에 대한 관심이 높아졌다. 그로 인해 현재 개발된 대표적인 연료가 전기와 수소이다. 
   친환경 자동차의 구매 비율은 초기에 대비하여 상승하였지만 충전인프라는 빠르게 확충되지 않는 것이 오랜 문제로 여겨지고 있음. 지역별로 등록된 친환경 자동차의 대수에 비하여 충전기의 설치 대수를 한 눈에 시각화하여 사용자에게 보여주고, 전기차 구매 관련이나 충전관련 기업의 faq를 사용자가 한 번에 볼 수 있는 플랫폼이 필요하다.

   
   ![image3](https://cdn.imweb.me/upload/S201903265c99a2aabdcfe/ed30a20d8a555.png)
   ![image1](https://magazine.hankyung.com/magazinedata/images/raw/201808/4c9e447ec35560019ff9413862d2e16c.jpg)
   ![image2](https://img.khan.co.kr/news/2024/05/26/news-p.v1.20240526.b785a76a031b40fe99d34b47c99fec8a_P1.jpg)
### 프로젝트 목표
✅ 우리나라의 전체 자동차 등록 현황에 대비하여 친환경차의 비율이 어느정도인지 산출하고,
   전기, 수소 충전소의 인프라가 얼마나 구축되어있는지 설치 현황을 지도에 시각화

## 3. 기술 스택
<p align="center">
  <img src="https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white">
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
  <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=vscode&logoColor=white">
<!--   <img src="https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white"> -->
</p>

<br/><br/>

## 4. WBS
| 작업 명                | 시작일 | 종료일 | 담당자                   | 산출물                   | 의존작업            |
|----------------------|-------|-------|-------------------------|-------------------------|---------------------|
| 프로젝트 주제 선정       | 02-24 | 02-25 | ALL                     | 없음                    | 없음                |
| Streamlit 화면 설계      | 02-25 | 02-26 | 김정원, 정민호             | 설계파일, WEB 화면         | 없음                |
| Streamlit-DB연동       | 02-25 | 02-26 | 이상준                   | DB table                | Streamlit 화면       |
| FAQ 크롤링             | 02-25 | 02-26 | 정민호                     | csv, .xlsx, json         | Streamlit 작업       |
| 웹 크롤링             | 02-25 | 02-26 | 이상준,이선호                     | csv, .xlsx, json         | Streamlit 작업       |
| 데이터 수집       | 02-25 | 02-26 | 배정수,이선호,김정원                     | csv, .xlsx, json         | Streamlit 작업       |
| ERD 작성               | 02-25 | 02-26 | 배정수, 이선호       | ERD 다이어그램            | 없음                |
| 데이터-DB연동          | 02-25 | 02-26 | 이선호,김정원,배정수                     | DB 데이터               | 크롤링, 데이터수집     |
| Streamlit 화면 구현      | 02-25 | 02-26 | 김정원,정민호,이상준                     | Streamlit 화면           | 크롤링, 데이터수집     |
| 코드 취합              | 02-26 | 02-26 | ALL                     | Web 페이지, DB 데이터     | 크롤링, 데이터수집     |
| 최종 점검              | 02-26 | 02-26 | ALL                     | Web 페이지              | 없음                |




## 5. 요구사항 명세서

|**RQ-ID**|회원명|요구사항명|요구사항 내용|날짜|
|------|---|---|---|---|
|RQ-01|공통|DB 수집|시스템은 전국 자동차 등록 현황과 친환경 자동차 등록 현황을 수집한다. 시스템은 제조사와 충전기 관련 FAQ 데이터를 수집한다. 시스템은 자동으로 데이터를 업데이트하고 관리한다.|02/25|
|RQ-02|공통|DB 서버 구축|시스템은 수집된 데이터를 자동으로 DB 서버에 등록한다.|02/25|
|RQ-03|공통|Streamlit - 페이지|Streamlit 화면 구성 : 홈 화면, 차량등록현황, 충전소 현황 지도, FAQ 페이지를 구축한다. |02/25|
|RQ-04|공통|Streamlit - 페이지|홈 화면 구축 : 시스템은 프로젝트 개요 및 간략화 된 정보를 제공한다.|02/25|
|RQ-05|공통|Streamlit - 페이지|등록현황 화면 구축 : 시스템은 자동차 등록현황 데이터를 불러와서 친환경 자동차에 대한 내용을 시각화 한다.|02/25|
|RQ-06|공통|Streamlit - 페이지|차량수요 화면 구축 : 시스템은 프로젝트 개요 및 간략화 된 정보를 제공한다.|02/25|
|RQ-07|공통|Streamlit - 페이지|메뉴바 생성 : 사용자는 좌측의 메뉴바를 통해 각 페이지에 접근할 수 있다.|02/25|
|RQ-08|공통|등록현황 시각화|시스템은 지도 기반 지역별 등록 현황 및 막대 그래프를 통해 연료별 등록현황을 제공한다.|02/25|
|RQ-09|공통|수요현황 시각화|시스템은 월별 수요 데이터에 대한 파이 그래프를 통해 제공한다.|02/25|
|RQ-10|공통|Filter 기능|사용자는 키워드 검색을 통해 FAQ에 접근할 수 있다.  사용자는 브랜드 선택을 통해 FAQ에 접근할 수 있다. 사용자는 카테고리 선택을 통해 FAQ에 접근할 수 있다.|02/25|
|RQ-11|공통|통합 FAQ 기능|시스템은 제조사와 충전서비스 제공회사의 faq를 제공한다.|02/25|

## 6. ERD
![Image](https://github.com/user-attachments/assets/ea1ac281-cda9-4330-ba19-94652fe3f07f)




## 7. 수행결과(테스트/시연 페이지)

충전소 설치 현황
![Image](https://github.com/user-attachments/assets/93820f69-9eb5-4428-a7ef-3749186f1dab)

친환경 차량 등록 현황 조회기능

![Image](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN011-1st-4Team/blob/e39b2ba05892dc3cd43ca423778f5c60d0385bc8/screenshot1.png)
![Image](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN011-1st-4Team/blob/e014dfad8d84f87ee295a83dd5dcd80f82e943dc/screenshot2.png)

|FAQ 시연|
![Image](https://github.com/user-attachments/assets/d2ebdd13-efc2-49f7-8f9e-b3ac64db80b5)

## 8. 회고
|Name| 한 줄 |
|---|---|
|배정수|수집한 데이터를 사전에 만든 ERD에 맞춰 mySQL로 데이터베이스에 연동시키는 작업을 진행했지만, 아직 학습하지 않은 작업들이 필요해 스스로 학습하며 진행하느라 시간이 오래 걸렸을 뿐만 아니라 ERD가 잘못 짜여있어 시간이 촉박했습니다. 이를 해결하기 위해서 함께 협업하는 팀원들에게 문제점을 이야기하고 함께 조언을 구했거나 후속조치를 했어야 하는데 혼자 잡고 하려는 생각에 그러지 못했습니다. 개개인의 능력을 떠나 프로젝트는 혼자 하는 것이 아니라는 것을 크게 느꼈습니다.|
|이상준|팀원들을 별로 생각하지 못하고 있었던 것을 반성합니다.|
|이선호|ERD 작성부터 웹 크롤링, DB까지 프로젝트를 통해 활용방법을 잘 터득할 수 있었습니다😁 |
|정민호|첫 프로젝트라 어려움이 많았지만, Crawling, DB 등 배운 내용들을 응용해볼 수 있어 좋았습니다😎|
|김정원|첫 프로젝트이고 데이터베이스를 다루는 것이 처음이다 보니 진행하면서 어려운 점이 많이 있었으나, 프로젝트를 통해서 DB에 대해서 좀 더 확실하게 알아갈 수 있다는 것이 좋았습니다. 아직은 모르는 것이 많지만 추후의 프로젝트와 개인 공부를 통해서 더 많은 것을 가져가보고자 합니다.|

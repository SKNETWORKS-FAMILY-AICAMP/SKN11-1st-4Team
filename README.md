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
✅ 친환경 자동차 관련 정보 제공 시스템템
### 프로젝트 소개
✅ 전국 자동차 등록 현황 대비 친환경차의 비율을 도출하고, 전기,수소 충전소 인프라 확충과 관련하여 충전소 설치 현황을 시각화, 기업의 faq를 조회하여 사용자에게 보여줄 수 있는 시스템을 구축하는 프로젝트
### 프로젝트 필요성(배경)
✅ 지구온난화 등 환경오염에 대한 인류의 경각심이 점점 올라감에 따라 화석연료를 사용하는 기존의 내연기관 자동차를 대체하고자 하는 친환경적인 연료를 사용하는 자동차에 대한 관심이 높아졌다. 그로 인해 현재 개발된 대표적인 연료가 전기와 수소이다. 
   친환경 자동차의 구매 비율은 초기에 대비하여 상승하였지만 충전인프라는 빠르게 확충되지 않는 것이 오랜 문제로 여겨지고 있음. 지역별로 등록된 친환경 자동차의 대수에 비하여 충전기의 설치 대수를 한 눈에 시각화하여 사용자에게 보여주고, 전기차 구매 관련이나 충전관련 기업의 faq를 사용자가 한 번에 볼 수 있는 플랫폼이 필요하다.
### 프로젝트 목표
✅ 우리나라의 전체 자동차 등록 현황에 대비하여 친환경차의 비율이 어느정도인지 산출하고,
   전기, 수소 충전소의 인프라가 얼마나 구축되어있는지 설치 현황을 지도에 시각화

## 3. 기술 스택
<p align="center">
  <img src="https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white">
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=vscode&logoColor=white">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
  <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white">
  <img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white">
<!--   <img src="https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white"> -->
</p>

<br/><br/>

## 4. WBS




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





## 7. 수행결과(테스트/시연 페이지)




## 8. 회고
|Name| 한 줄 |
|---|---|
|배정수|안다고 생각하고 있던 것들이 사실은 반의 반도 모르는 상태였습니다. 조금 더 열심히 해야겠네요|
|이상준|---|
|이선호|ERD 작성부터 웹 크롤링, DB까지 프로젝트를 통해 활용방법을 잘 터들할 수 있었습니다😁 |
|정민호|첫 프로젝트라 어려움이 많았지만, Crawling, DB 등 배운 내용들을 응용해볼 수 있어 좋았습니다😎|
|김정원|---|

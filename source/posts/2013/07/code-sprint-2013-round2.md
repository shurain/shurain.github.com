Date: 2013-07-20
Title: Code Sprint 2013 Round 2
Slug: code-sprint-2013-round-2
Category: Blog
Tags: code sprint, forecasting
Status: draft


## Introduction

SK planet에서 정기적으로 Code Sprint라는 프로그래밍 경진 대회를 주최한다. 얼마 전에 Code Sprint 2013의 라운드 2 결과가 나왔는데 운이 좋게도 내가 1위를 할 수 있었다. 이번 대회의 목표는 교통정보 데이터를 사용하여 미래의 교통정보를 예측하는 것이었다.

대회 페이지의 설명을 그대로 옮겨보면, 
> 코드스프린트 Round2 문제에서는 2013년 4월부터 6월까지 3개월간의 T map 경부고속도로 교통정보를 제공하고 개발자는 이를 분석하여 7월 16일 24시간의 교통정보를 예측합니다.

자세한 내용은 [공식 페이지](http://codesprint.skplanet.com/2013/intro/round_02.htm)를 방문하면 확인할 수 있다.

## Approach

이런식의 문제를 접하면 우선적으로 해야 하는 것이 몇 가지 있다. 가장 중요한 것 중 하나가 데이터를 살펴보는 것이다. 흔히 [exploratory data analysis](http://en.wikipedia.org/wiki/Exploratory_data_analysis)라고 하는데, 데이터를 살펴보고 이를 토대로 적절한 가설을 세우거나 앞으로의 진행 방향 등을 결정하기 위해서 반드시 필요한 작업이다.

<center>
![1번 도로의 일별 데이터를 시간축으로 자른 차트](/static/images/codesprint_015.jpg)

1번 도로의 일별 데이터를 시간축으로 자른 차트. 01:15의 데이터로, x축은 날짜를 y축은 평균 시속을 의미한다.
</center>


base model을 만드는 것이 
데이터를 살펴보는 것


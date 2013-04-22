Date: 2013-04-22
Title: Text Segmentation
Slug: text-segmentation
Category: Blog
Tags: crf, text segmentation
Status: draft


## Introduction

모든 기계학습 기법이 그렇듯 CRF도 주어진 데이터에 따라 체감할 수 있는 성능 차이가 크다.
기계학습은 데이터를 바탕으로 어떤 모델을 만들어내는 방법이라고 생각할 수 있는데, 주어진 데이터가 우리가 원하는 모델을 만들어 내는데 필요한 정보를 갖고 있지 않으면 이는 불가능하다.

[Pedro Domingos](http://homes.cs.washington.edu/~pedrod/)는 기계학습을 정원을 가꾸는 것에 비유했다. [<span id="ref1">[1]</span>](#footnote1)

- Seeds = Algorithms
- Nutrients = Data
- Gradener = You
- Plants = Program

기계학습의 엄청난 강점은 굉장히 많은 일을 데이터가 대신 해준다는 것이다. 
기존의 프로그래밍을 생각해보면 프로그래머가 모든 프로그램을 작성해야 했다.
그러나 기계학습에서는 어떤 특정한 일을 하는 프로그램을 만들기 위해서 기본적인 기계학습 알고리즘에 데이터를 잔뜩 부어넣어서 목표로 하는 프로그램을 만들어낸다.
이는 마치 정원사가 정원에 씨앗을 심고 약간만 신경을 써주면 거의 대부분의 일을 자연이 해주는 것과 유사하다.
하지만 이를 잘 생각해보면 결국 데이터가 아주아주 중요하다는 것을 알 수 있다.
쓰레기 데이터를 넣으면 쓰레기가 나올 수 밖에 없다. [<span id="ref2">[2]</span>](#footnote2)

## Text Segmentation

[지난 글](http://blog.shurain.net/2013/04/crf.html)에서 CRF를 개략적으로 살펴보고 이를 한국어 띄어쓰기에 적용한 예를 살펴보았다.
지난 예에서는 한국어 위키백과의 데이터를 사용하여 띄어쓰기를 위한 CRF를 학습하였다. 
이 모델은 표준어를 띄어 쓰는 것은 꽤 잘한다.
그러나 구어체 혹은 비속어 및 비문, 오타 등을 마주치게 되면 잘 처리하지 못하는 모습을 보여준다.

> 아마싯는거먹고시퍼
아마싯는 거먹고 시퍼

이는 당연한 현상인데, 한국어 위키백과에 구어체, 비속어 비문 등은 거의 없을 것이기 때문이다.
데이터가 힘든 일을 대신 해줘야 하는데, 데이터가 이를 못하는 상황인 것이다.
이를 해결하기 위해서 구어체 등을 포함한 데이터를 넣어줄 필요가 있다.

지난 글에서 각주에 언급했지만 사실 좋은 데이터를 구하는 것은 어려운 일이다.
대규모 서비스를 운영하는 입장에서는 그런 데이터가 충분히 있겠지만 재미삼아 하는 입장에서는 데이터 획득이 만만한 일이 아니다. 
지난 번에는 한국어 위키백과 자료를 활용했는데, 이번에는 엔하위키의 데이터를 추가하였다. [<span id="ref3">[3]</span>](#footnote3) 
엔하위키는 위키백과에 비해 상대적으로 덜 딱딱하고 구어체에 가까운 문법을 사용하는 것을 볼 수 있으며, 많은 종류의 인터넷 용어도 포함하고 있다.



<span id="footnote1">
[[1]](#ref1): [Machine Learning by Pedro Domingos](https://www.coursera.org/course/machlearning)
</span>

<span id="footnote2">
[[2]](#ref2): [Garbage in, garbage out](http://en.wikipedia.org/wiki/Garbage_in,_garbage_out)
</span>

<span id="footnote3">
[[3]](#ref3): [엔하위키](http://ko.wikipedia.org/wiki/%EC%97%94%ED%95%98%EC%9C%84%ED%82%A4)
</span>


Date: 2013-10-31
Title: Naive Bayes Classifier
Slug: naive-bayes-classifier
Category: Blog

## Introduction

스팸 문서 판별에 가장 쉽게 사용할 수 있는 기계 학습 기법으로 [나이브 베이즈 분류기](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)가 있다.
최근에 이와 관련된 간단한 발표를 할 일이 있어서 [관련 자료](http://cl.ly/0s2U3L0Y2Q0L)를 만들어 보았다.
대부분의 내용은 Mathematicalmonk의 [Naive Bayes classification 영상](https://www.youtube.com/watch?v=8yvBqhm92xA&list=PLD0F06AA0D2E8FFBA&index=46)을 참고하였다.

## Naive Bayes

자세한 이야기는 발표 자료를 참고하기로 하고, 몇 가지 언급하고 싶은 것들만 짚어보도록 하겠다.

### Conditional Independence

나이브 베이즈에서 "나이브"라는 이름이 붙은 이유는 레이블이 이미 주어졌다고 가정하면 (conditional), 피쳐들이 서로 독립이라는 (independence) 가정 때문이다.
이는 패러미터를 유추하는 작업을 쉽게 만들기 위해서 도입되었다고 생각되는데, 다행히도 문서를 다룰 때에는 이러한 독립성 가정이 잘 동작하는 편이다.

### Bayes Theorem & Bayesian Inference

나이브 베이즈의 "베이즈"는 베이즈 정리를 사용한 부분에서 나온 것이다.
그저 베이즈 정리를 사용할 뿐이지 딱히 베이지안 추론 기법은 아니라는 점을 이해하는 것이 중요하다.
베이지안 추론 기법은 모델의 패러미터를 전부 고려하여 이를 적분해버리는 것이 골자이지 베이즈 정리를 사용하는 것이 핵심이 아니다.
대부분의 나이브 베이즈 구현은 모델 패러미터를 maximum likelihood estimate을 사용하여 추정하는데, 이는 point estimate에 불과하고 진정한 의미의 베이지안은 아니다.
베이지안에 대해 더 알고 싶다면 이를 잘 정리한 [WHAT IS BAYESIAN/FREQUENTIST INFERENCE?](http://normaldeviate.wordpress.com/2012/11/17/what-is-bayesianfrequentist-inference/)를 참고하기 바란다.
위의 글에서 Nate Silver의 책 Signal and the Noise 혹은 Sharon McGrayne의 책 The Theory That Would Not Die 등에서 행하는 흔한 실수에 대해 논한다.[<span id="ref">[1]</span>](#footnote1)


<span id="footnote1">
[[1]](#ref1): 이에 대한 더 자세한 글로 동일 저자의 글인 [Nate Silver Is A Frequentist](http://normaldeviate.wordpress.com/2012/12/04/nate-silver-is-a-frequentist-review-of-the-signal-and-the-noise/)도 있다.
</span>

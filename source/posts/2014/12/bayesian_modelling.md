Date: 2014-12-02
Title: 베이지안 모델링
Slug: bayesian-modelling
Category: Blog

## Introduction

많은 기계 학습 기법은 확률 기반의 방법론으로 설명할 수 있다.
확률 기반으로 표현된 문제를 다루는 방법 중 베이지안 방법론이 있다.
어떤 문제를 접하면, 확률론의 언어를 사용해서 문제에 포함된 불확실성을 표현하고 베이즈 정리를 사용해서 알고 싶은 것들에 대한 추론을 수행하게 된다.

## Bayes Theorem and Inference

$p(가설|데이터) = \frac{p(데이터|가설)p(가설)}{p(데이터)}$

베이즈 정리는 무척 간단한 수식이다.
위의 식은 확률론에서 흔히 sum rule이라고 불리는 규칙과 product rule이라고 불리는 두 개의 규칙으로 유도할 수 있다.

$p(x) = \sum_y p(x, y)$
$p(x, y) = p(x)p(y|x)$

베이즈 정리에서 가설을 $\theta$로 놓고 데이터를 $D$로 표현하면, $p(D|\theta)$ 를 likelihood라 부르며 $p(\theta)$는 prior probability, $p(\theta|D)$를 posterior probability라 한다.

위의 식에 따라 모델을 확률론의 언어로 표현할 수 있다면 위의 식을 사용해서 데이터로부터 가설에 대한 추론을 할 수 있다.

이 식은 여러 용도로 사용되는데, 문제의 패러미터를 추론하거나 예측 문제를 푸는 등에 사용하게 된다.



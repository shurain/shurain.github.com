Date: 2015-01-16
Title: Regression and Model Interpretation
Slug: regression-model-interpretation
Category: Blog

> $m = b_0 + b_1 x_1 + b_2 x_2 + \ldots + b_p x_p$
>
> Do you see? We model the $m$; we say the $m$ is a function of various things, the $x$'s. Maybe one of the $x$'s is age, another is sex, a third is income, a fourth is BMI, a fifth is height, a sixth is presence of some gene, a seventh is whether the individual is a science major, an eighth is whether the individual is Caucasian, a ninth is high school GPA, a tenth is SAT score, an eleventh, a twelfth, thirteenth, and on and on and so on some more. You'd never make it as a sociologist unless you can think of at least two dozen entries.
> 
> Consider that the $x$ which represents whether the individual is Caucasian increases m. That does not therefore mean whites have higher GPAs than non-whites. No no no no no. No. It says, very indirectly and after manipulation most people forget to or don’t do, that given this model and these $x$'s, the probability whites have higher GPAs than non-whites is greater than 50%. (The exact probability can be calculated.)[^regression-not-what-you-think]

흔히 선형 모델을 만들고 각 요소의 regression weight로 현실을 해석하려 한다. 위의 인용에서 사용된 예를 살펴보자. 만약 코카시언의 여부가 GPA의 선형 모델의 피쳐로 들어가고 그 weight가 양수라고 하자. 이를 백인이, 백인이 아닌 사람보다 GPA가 높다고 해석해서는 안 된다. 위의 인용에서 볼 수 있다시피 이는 무척 많은 가정을 깔고 들어간 후에야 백인의 GPA가 백인이 아닌 사람의 GPA보다 높을 확률이 50% 이상이라는 설명을 할 수 있다.

Bayesian의 관점에서 생각해보면 regularization은 우리가 세상에 대해 갖고 있는 prior knowledge를 반영한 것이다. 단순히 predictive accuracy를 높이기 위해 다양한 방법으로 이런 prior를 검증을 해보고 이를 바탕으로 예측을 하는 것은 괜찮을 수 있다. 하지만 모델로부터 세상을 해석하려고 할 때의 문제를 살펴보자. Sparse linear model을 생각해보면 아예 subset selection 문제로 접근하는 것도 가능하고 ridge나 lasso 등의 regularization 문제로 모델링 하는 것도 가능하다.

![Sparse Model](https://www.evernote.com/shard/s25/sh/b3e173a3-3d91-4076-8b9f-5b0288cc76f5/be92f6f5a4ab2e6dddfb38407d5c163b/deep/0/Murphy---2012---Machine-Learning-A-Probabilistic-Perspective.pdf-(page-467-of-1098).png)

위의 예에서는 Lasso가 가장 좋은 predictive accuracy를 내지만 이는 문제의 특성에 따라 달라질 수 있다. 가령 위의 예에서 best subset과 ridge만 비교한다면 best subset이 더 예측력이 높기 때문에 이게 현실을 해석하는 용도로 사용되어도 괜찮은 것일까? 그렇다면 svi는 암 발병에 영향을 전혀 주지 않는 요소라고 말해도 괜찮은 것일까? 반대로 best subset과 lasso를 비교해보면 svi가 양의 weight를 가지므로 svi가 암 발병의 원인이 된다고 말할 수 있는 것일까?

![Regularization](https://www.evernote.com/shard/s25/sh/f33e1fd4-5b6b-4820-9580-8f880fb242b2/562078df2ace0d03b73c0440c28b634a/deep/0/Murphy---2012---Machine-Learning-A-Probabilistic-Perspective.pdf-(page-468-of-1098).png)


같은 방법이라도 regularization의 강도를 얼마나 주느냐에 따라 다른 결과를 얻을 수 있다. CV를 거쳐서 hyper parameter를 결정했기 때문에 이것으로부터 현실을 해석해도 되는 것일까? 이런 종류의 모델 읽기 실수는 무척 저지르기 쉽다. 언제나 이런 해석에는 주의를 기울여야 한다.[^pitfall]

[^regression-not-what-you-think]: [Regression Isn’t What You Think](http://wmbriggs.com/blog/?p=12524)
[^pitfall]: 이런 종류의 문제로 신뢰 구간, 유의 수준 등등도 있다. 진지한 연구자들조차 늘상 틀리는 개념들이다.

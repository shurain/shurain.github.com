Date: 2013-11-08
Title: StumbleUpon Evergreen Classification Challenge
Slug: stumbleupon-evergreen-classification-challenge
Category: Blog

## Introduction
지난 8월 Kaggle에서 [StumbleUpon Evergreen Classification Challenge](https://www.kaggle.com/c/stumbleupon)가 있었다.
이번 대회는 사용자에게 웹 문서를 추천해주는 서비스인 StumbleUpon에서 주최한 대회였다.
StumbleUpon이 서비스를 제공하면서 어떤 종류의 글은 발행 후 시간이 어느 정도 지나면 사람들에게 추천해주기 좋지 않은 반면 어떠한 글은 발행 후 시간과 무관하게 사람들에게 추천할 가치가 있는, 서로 다른 성격을 지닌 글이 있음을 알게 되었다.
이를 각각 "ephemeral"과 "evergreen"이라고 이름 지었는데, 대회의 목표는 웹 문서를 수집한 그 시점에 ephemeral과 evergreen의 여부를 가리는 것이었다.

자연어 처리와 관련된 프로젝트를 제대로 해 본적이 없어서 이번 대회에 도전하게 되었다.
처음 목표는 상위 20%에 드는 것이었는데 최종 결과는 기대보다 훨씬 좋아서 총 625팀 중 22위를 하게 되었다.
1위가 AUC 점수 0.88906이었고, 내가 0.88495였으니 아주 큰 차이가 있지는 않았다고 생각한다.
[사용한 방법](https://www.kaggle.com/c/stumbleupon/forums/t/6197/thank-you-and-thoughts-on-the-final-ranking)도 크게 다르지 않았던 것으로 보인다.


## Details

분류를 할 수 있도록 주어진 데이터는 크롤러가 수집한 HTML 웹 문서와 후처리를 통해 이로부터 뽑아낸 다양한 정보였다.
후처리로 뽑아낸 정보로는 URL, HTML 문서에 포함된 텍스트 정보 등의 기본적인 정보 외에도 문서 압축률, 링크 개수 등의 다양한 정보를 포함하고 있었다. 
자세한 내용은 [Get the Data](https://www.kaggle.com/c/stumbleupon/data) 페이지의 표를 참고하면 된다.

채점 기준은 [area under the ROC curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)였으며 늘 그러하듯 답안을 csv로 만들어서 제출하도록 하였다. 

## My Approach
처음에는 기본적인 data exploration을 수행하였다.
우선 주어진 데이터를 살펴보면 boilerplate 라는 이름의 피쳐가 있었는데, 여기에 HTML 문서에서 뽑아낸 텍스트 데이터가 있었다.
이 피쳐와 문서의 URL 등 몇 가지 당연히 유의미할 것으로 추정되는 피쳐가 있었으나 반대로 다른 다양한 피쳐들은 과연 쓸모가 있을지 의심스러웠는데, 실제로 몇 가지 실험을 해보니 거의 의미 없는 피쳐였다.
간단한 실험 후에 문서의 제목, URL, 본문을 주된 베이스로 사용해서 분류를 시도하기로 하였다.
이런 종류의 문제에 적합하게 TF/IDF 피쳐를 뽑아서 사용하였는데, 위에서 언급한 피쳐를 한데 모아 사용하였다.
학습은 [Stochastic gradient descent](http://scikit-learn.org/stable/modules/sgd.html)를 시작점으로 사용했다.
기본적인 사항이 결정된 뒤의 실험은 꽤 지루했는데, 다양한 조합의 피쳐와 다양한 학습 알고리즘을 사용해서 결과가 어떻게 변하는지 cross validation을 통해서 확인하였다.

최종적으로 제출한 모델은 다음과 같다.
우선 주어진 HTML 문서로부터 [boilerpipe](https://code.google.com/p/boilerpipe/)를 사용하여 본문의 텍스트만 뽑아내고,
이를 [word2vec](https://code.google.com/p/word2vec/)으로 의미 있는 phrase 단위로 묶도록 하였다.
이렇게 해서 만들어진 데이터와 URL, 제목, 본문을 합쳐서 TF/IDF 벡터를 만들어서 피쳐로 삼았다.
이 피쳐를 [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating)을 3,000회 반복해서 총 3천 벌의 데이터를 생성하고, 각 데이터를 SGD로 학습시켰다. 
이렇게 만들어진 3천 개의 모델의 예측치를 평균내어 이를 제출하였다.

## Post-mortem

이번 대회에서는 활용해본 기법이 꽤 다양했다.
Naive Bayes, logistic regression, SVM, kNN 등 기본적으로 활용할 수 있는 분류기는 전부 한 번 씩은 써본 것 같다.
대체로 random forest가 여러 도메인에서 아주 훌륭한 성능을 보이지만 내가 사용한 [scikit-learn](http://scikit-learn.org/stable/index.html)은 sparse한 데이터를 다루는 random forest 구현이 없었다.
차원 감소를 해서 몇 가지 시도를 해보았는데, PCA, K-means clustering 등으로 접근해 보았지만 득을 보지는 못하였다.
우승자는 PCA한 것을 random forest로 학습시키고 logistic regression 결과와 앙상블을 하였다고 하니 나의 접근 방향이 잘못된 것은 아니었던 것으로 보인다.
Boosting을 잘 활용하면 좋은 결과를 얻을 수 있지 않을까 싶었지만 큰 소득은 없었다.

피쳐 생성도 신경을 조금 써봤는데, word2vec 등을 활용한 phrase 생성도 있었고, 휴리스틱 기반으로 글의 댓글만 떼어내어 이를 활용한 것도 있었다.
나중에는 잘못 분류된 데이터를 살펴보며 시간을 꽤 보냈는데, 사람이 직접 만든 레이블이라 오류도 적지 않게 있는 것으로 보였다.
대회 시작 후 2주 정도 되었을 때 흥미가 확 떨어진 계기가 있었는데, 잘못된 분류를 자주 하는 데이터를 살펴보니 스포츠일러스트레이티드 사이트의 문서가 몇 개 트레이닝 데이터로 끼어 있고 이를 제대로 분류하지 못하고 있었다. 
실제 웹 페이지를 보니 사진만 잔뜩 있고 글이 거의 없는 페이지들이었다. 
이런 식으로 사실상 유의미한 분류가 불가능해 보이는 도메인이 여럿 있었다.
그리고 당연히 트레이닝 데이터와 테스트 데이터에 그런 도메인의 분포가 달랐다.
결국 이런 관찰은 나의 CV 결과를 얼마나 신뢰할 수 있는지에 대한 의구심으로 이어졌다.
퍼블릭 리더보드 점수를 높이려고 노력하다가 오버피팅하기 십상이라는 결론을 내리고 그 시점 이후로 더 점수를 올리려고 시도하지 않았다.

이런 대회에 참가하면 늘 느끼는 것 중 하나가 빠른 분류기의 중요성이다.
실험 한 번이 너무 오래 걸리면 흥미도 떨어지고 흐름도 끊기게 마련이다.
요즘은 그래서 가능하면 속도가 빠른 리니어 러너를 활용하고 차선으로 트리 기반의 기법을 애용한다.
빠르게 실험을 할 수 있으면 무엇보다 흐름이 덜 끊기고 다양한 아이디어를 실험해 볼 수 있어서 특히 이런 대회에서 매우 좋다.

평소에 늘 이런 기회가 생기면 새로운 도구를 하나씩 손에 익히려고 시도를 해보곤 하는데, 이번 대회에서는 [sofia-ml](https://code.google.com/p/sofia-ml/)를 그럭저럭 사용해볼 수 있었다.
Deep learning을 활용해보고 싶어서 [pylearn2](http://deeplearning.net/software/pylearn2/)를 살펴보긴 하였는데 실제로 활용할 수 있는 수준까지는 익히지 못하였다.

처음 시도해본 NLP 프로젝트였는데, 생각보다 성적이 좋아서 기분이 좋았다.
지난번 Kaggle 대회 시도 이후 느낀 바가 있어 계속해서 이런저런 공부를 하였는데 그 결과가 보이는 것 같다.

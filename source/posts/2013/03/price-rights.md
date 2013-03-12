Date: 2013-03-12
Title: Bayesian Approach to the Price is Right's Showdown
Slug: price-rights
Category: Blog


[지난 글](/2013/02/darkworld2.html)에서 Observing Dark Worlds 대회에 1, 2위가
사용한 방법을 설명하면서 Bayesian 방식으로 문제에 접근하는 이야기를 했었다.
이런 Bayesian 방식을 쉽게 잘 설명한 글로
[How to solve the Price is Right's Showdown](http://camdp.com/blogs/how-solve-price-rights-showdown)이라는
블로그 글이 있다.

이 글은 [The Price Is Right](http://en.wikipedia.org/wiki/The_Price_Is_Right)이라는
TV 쇼의 마지막 대결 The Showcase를 Bayesian 방식으로 풀어보는 시도에 대한 이야기하고 있다.
문제에 대한 자세한 정보는 원문을 참고하길 바란다.

전체적으로는 prior belief를 설정하고 likelihood 계산을 위한 모델 설정 뒤에
[PyMC](https://github.com/pymc-devs/pymc) 라이브러리를 사용하여 MCMC 계산을 한다.
그리고 loss function을 정의하여 그에 따른 expected loss optimization을 수행하는 전통적인 구조를 잘 보여준다.
같은 기법이 다른 문제에 적용된 사례이니 지난 글의 내용이 잘 이해가 되지 않았던 분들은 한 번 읽어보시면 도움이 될 것이다.

글의 내용은 오픈 소스 책인
[Probabilistic Programming and Bayesian Methods for Hackers in Python](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)의
내용을 따와서 많이 수정하여 만들었다고 한다.[<span id="ref1">[1]</span>](#footnote1)
아직 책의 내용을 살펴볼 기회는 없었지만 기초적인 Bayesian 기법에 대해 실제로 사용해보는 것을 위주로[<span id="ref2">[2]</span>](#footnote2)
쓰여 있다고 하니 이런 내용에 관심 있는 사람들은 한 번 보면 좋을 것이다.


<span id="footnote1">
[[1]](#ref1): 책 저자가 블로그 글쓴이
</span>

<span id="footnote2">
[[2]](#ref2): 사람들이 질려 할만한 수학은 가능하면 2순위로 미루고
</span>

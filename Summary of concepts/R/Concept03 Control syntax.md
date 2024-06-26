# In English

## Using if statement

We will use if and else statements. First, we will generate a random number using the rnorm() function and create code to determine how close this random number is.

```
rnorm(1)
```
It is a random number that is relatively close to 0.



Let's input this into a variable and determine what number it is close to.

```
x <- rnorm(1)
```

```
if(x > 1) { #If x is greater than 1~
  answer <- "Greater than 1"
}
else {
  answer <- "Less than 1 or Equal 1"
}

answer
```

In R, like other languages, you can use if else if else.




# In korean 

## if문 사용하기

if와 else 구문을 이용해볼 것이다. 먼저, rnorm() 함수를 이용해서 난수를 생성하고, 이 난수가 어디에 가까운지 판별해보는 코드를 만들 것이다. 

```
rnorm(1) 
```
0과 그나마 가까운 난수이다. 



이를 변수에 입력받고, 어떤 수에 가까운지 판별해보자. 

```
x <- rnorm(1)
```

```
if(x > 1) { #x가 1보다 크다면~
	answer <- "Greater than 1"
}
else {
	answer <- "Less than 1 or Equal 1"
}

answer
```

R에서도 다른 언어와 마찬가지로 if else if else를 사용하면 된다. 


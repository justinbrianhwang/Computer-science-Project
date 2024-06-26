## In English
Five main variable types are available in R. To check the type of a variable, use the `typeof()` function.

```
typeof(variable)
# If the output value is 'integer', it is an integer
# If the output value is 'double', it is a double
# If the output value is 'complex', it is a complex number
# If the output value is 'character', then the character
# If the output value is 'logical', it is a Logical variables
```

Integer: You can use <- (arrow or assignment operator) to assign an integer to a variable. In R, numbers are basically treated as doubles, so to treat them as integers, you must add L to the end of the number. for example,
```
Variable <- 42L
```
sets the variable to an integer.

Double: The value of a double can be assigned to a variable with <-. for example,
```
Variable <- 3.14
```
sets the variable to a real number.

Complex number: Complex numbers can also be stored in variables.
```
Variable <- 1+4i
```
You can specify a complex number value as follows.

Character: Strings are specified by enclosing them in double quotation marks.
```
Variable <- "Hello"
```
You can store a string in a variable like this:

Logical variables: Logical values ​​are expressed as T (True) and F (False). for example,
```
Variable <- T
```
sets the variable to true.


## In Korea

### R의 변수 타입

R에서는 다섯 가지 주요 변수 타입을 사용할 수 있다. 변수의 타입을 확인하려면 `typeof()` 함수를 사용한다.

```
typeof(변수)
# 출력값이 'integer'라면 정수
# 출력값이 'double'라면 실수
# 출력값이 'complex'라면 복소수
# 출력값이 'character'라면 문자
# 출력값이 'logical'이라면 논리 변수
```

정수: <- (에로우 또는 지정 작업자)를 사용하여 정수를 변수에 지정할 수 있다. R에서 숫자는 기본적으로 double로 처리되기 때문에, 정수로 처리하기 위해서는 숫자 뒤에 L을 붙여야 한다. 예를 들어, 
```
변수 <- 42L
```
은 변수를 정수로 설정한다.

실수(double): 실수는 동일하게 <-로 변수에 값을 지정할 수 있다. 예를 들어,
```
변수 <- 3.14
```
는 변수를 실수로 설정한다.

복소수(complex): 복소수도 변수에 저장할 수 있다. 
```
변수 <- 1+4i
```
와 같이 복소수 값을 지정할 수 있다.

문자: 문자열은 쌍따옴표로 묶어서 지정한다. 
```
변수 <- "안녕하세요"
```
와 같이 문자열을 변수에 저장할 수 있다.

논리 변수: 논리 값은 T (True)와 F (False)로 표현된다. 예를 들어, 
```
변수 <- T
```
는 변수를 참으로 설정한다.



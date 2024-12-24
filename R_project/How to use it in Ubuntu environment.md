# In English
## Installing R on Ubuntu: A Step-by-Step Guide

To use R in an Ubuntu environment, follow these steps:

### 1. Update System Packages
First, update the system packages.

```
sudo apt update
sudo apt upgrade
```

### 2. Add CRAN Repository
Add the Comprehensive R Archive Network (CRAN) repository to install the latest version of R.

```
sudo apt install software-properties-common
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
```


### 3. Add GPG Key
Add the GPG key to authenticate the CRAN repository packages.

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
```

### 4. Install R
Now you can install R.

```
sudo apt update
sudo apt install r-base
```

### 5. Install RStudio (Optional)
RStudio is an Integrated Development Environment (IDE) for R. To install RStudio, follow these steps.

Download the latest version of RStudio from the RStudio download page as a .deb file.
Install the downloaded .deb file (e.g., if you downloaded `rstudio-1.4.1106-amd64.deb`).

```
sudo dpkg -i rstudio-1.4.1106-amd64.deb
sudo apt-get install -f # Fix any dependency issues
```

## 6. Install Essential Development Tools (Optional)
Install essential development tools for compiling R packages.

```
sudo apt install build-essential
sudo apt install libcurl4-gnutls-dev libxml2-dev libssl-dev
```


# In korean

## Ubuntu 환경에서 R 설치 가이드

Ubuntu 환경에서 R을 사용하려면 다음 단계를 따르세요:

### 1. 시스템 패키지 업데이트
먼저, 시스템 패키지를 업데이트합니다.

```
sudo apt update
sudo apt upgrade
```

### 2. CRAN 리포지토리 추가
R의 최신 버전을 설치하기 위해 CRAN(Comprehensive R Archive Network) 리포지토리를 추가합니다.

```
sudo apt install software-properties-common
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
```


### 3. GPG 키 추가
CRAN 리포지토리의 패키지를 인증할 GPG 키를 추가합니다.

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
```

### 4. R 설치
이제 R을 설치할 수 있습니다.

```
sudo apt update
sudo apt install r-base
```

### 5. RStudio 설치 (선택 사항)
RStudio는 R의 통합 개발 환경(IDE)입니다. RStudio를 설치하려면 다음 단계를 따릅니다.

RStudio의 최신 버전을 RStudio 다운로드 페이지에서 .deb 파일로 다운로드합니다.
다운로드한 .deb 파일을 설치합니다. (예: rstudio-1.4.1106-amd64.deb 파일을 다운로드했다면)

```
sudo dpkg -i rstudio-1.4.1106-amd64.deb
sudo apt-get install -f  # 종속성 문제 해결을 위해
```

### 6. 필수 개발 도구 설치 (선택 사항)
R 패키지를 컴파일하기 위한 필수 개발 도구를 설치합니다.

```
sudo apt install build-essential
sudo apt install libcurl4-gnutls-dev libxml2-dev libssl-dev
```
이 단계를 마치면 Ubuntu 환경에서 R을 사용할 준비가 완료됩니다. R을 실행하려면 터미널에 R을 입력하면 됩니다. RStudio는 응용 프로그램 메뉴에서 실행할 수 있습니다.




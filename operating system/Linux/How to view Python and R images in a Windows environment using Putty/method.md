# In English
## Setting Up X11 Forwarding with VcXsrv and Running R and Python Scripts

### Installing and Configuring VcXsrv

1. **Download VcXsrv**:
   - Go to the [VcXsrv official download page](https://sourceforge.net/projects/vcxsrv/) and download the latest installer.

2. **Install VcXsrv**:
   - Run the downloaded installer and proceed with the default installation settings.

3. **Run XLaunch**:
   - Search for "XLaunch" in the Start menu and run it.

4. **XLaunch Configuration**:
   - **Display settings**:
     - Select "Multiple windows".
     - Set the "Display number" to something other than the default `0`, for example, `:1`.
     - Click "Next".
   
   - **Client startup**:
     - Select "Start no client".
     - Click "Next".

   - **Extra settings**:
     - Check "Clipboard" and "Native opengl".
     - Check "Disable access control".
     - Click "Next".

   - **Configuration complete**:
     - Click "Finish" to complete the setup and start VcXsrv.

### Enabling X11 Forwarding in Putty

1. **Run and Configure Putty**:
   - Run Putty.
   - Go to `Connection` > `SSH` > `X11` in the left menu.
   - Check the `Enable X11 forwarding` option.

2. **Enter Server Information and Connect**:
   - Enter the IP address and port of your server in the session settings and connect.

3. **Set the DISPLAY Environment Variable**:
   - Once connected to the server, set the `DISPLAY` environment variable to the new display number:
     ```bash
     export DISPLAY=localhost:1.0
     ```

### Generating a Histogram with R Console

#### Writing an R Script to Generate a Histogram

1. **Create an R Script**:
   - Write the following content to a file named `histogram_x11_persistent.R`:
     ```R
     # histogram_x11_persistent.R
     Sys.setenv(DISPLAY="localhost:1.0")  # Set the DISPLAY environment variable
     x11()
     hist(rnorm(100))
     # Wait for user input to close the plot window
     readline(prompt="Press [Enter] to close the plot window: ")
     dev.off()  # Close the window
     ```

#### Running the Script in an Interactive R Session

1. **Start the R Console**:
   - Connect to the server via Putty and start the R console:
     ```bash
     R
     ```

2. **Run the Histogram Script**:
   - In the R console, execute the script:
     ```R
     source("path/to/histogram_x11_persistent.R")
     ```

This will open the histogram window, which will remain open until you press Enter in the console.

### Generating a Graph with Python

#### Creating a Python Script to Generate a Graph with Matplotlib

1. **Create a Python Script**:
   - Write the following content to a file named `plot_x11_persistent.py`:
     ```python
     import matplotlib.pyplot as plt
     import os

     # Set the DISPLAY environment variable
     os.environ['DISPLAY'] = 'localhost:1.0'

     # Generate the graph
     plt.figure()
     plt.hist([i for i in range(100)])
     plt.title("Histogram")

     # Wait until the plot window is closed by the user
     plt.show(block=True)
     ```

2. **Run the Python Script**:
   - Connect to the server via Putty and run the Python script:
     ```bash
     python3 plot_x11_persistent.py
     ```

This will open the histogram window, which will remain open until you close it manually.

### Summary

1. **Install and Configure VcXsrv**:
   - Run XLaunch, select "Multiple windows", set the display number to `:1`, and complete the setup.

2. **Enable X11 Forwarding in Putty**:
   - Check the `Enable X11 forwarding` option and connect to the server.
   - Set the `DISPLAY` environment variable to `localhost:1.0`.

3. **Generate a Histogram with R**:
   - Write an R script and run it in an interactive R session.

4. **Generate a Graph with Python**:
   - Write a Python script with Matplotlib and run it.



# In Korean

## VcXsrv를 이용한 X11 포워딩 설정 및 R과 Python 스크립트 실행

### VcXsrv 설치 및 설정

1. **VcXsrv 다운로드**:
   - [VcXsrv 공식 다운로드 페이지](https://sourceforge.net/projects/vcxsrv/)로 이동하여 최신 설치 파일을 다운로드합니다.

2. **VcXsrv 설치**:
   - 다운로드한 설치 파일을 실행하여 기본 설정으로 설치를 진행합니다.

3. **XLaunch 실행**:
   - 시작 메뉴에서 "XLaunch"를 검색하여 실행합니다.

4. **XLaunch 설정**:
   - **Display settings**:
     - "Multiple windows"를 선택합니다.
     - "Display number"를 기본값인 `0`이 아닌 다른 번호로 설정합니다. 예를 들어, `:1`로 설정합니다.
     - "Next"를 클릭합니다.
   
   - **Client startup**:
     - "Start no client"를 선택합니다.
     - "Next"를 클릭합니다.

   - **Extra settings**:
     - "Clipboard"와 "Native opengl" 옵션을 체크합니다.
     - "Disable access control"을 체크합니다.
     - "Next"를 클릭합니다.

   - **Configuration complete**:
     - "Finish"를 클릭하여 설정을 완료하고 VcXsrv를 시작합니다.

### Putty에서 X11 포워딩 활성화

1. **Putty 실행 및 설정**:
   - Putty를 실행합니다.
   - 좌측 메뉴에서 `Connection` > `SSH` > `X11`로 이동합니다.
   - `Enable X11 forwarding` 옵션을 체크합니다.

2. **서버 정보 입력 및 접속**:
   - Putty의 세션에서 서버의 IP 주소와 포트를 입력한 후, 접속합니다.

3. **환경 변수 설정 확인**:
   - 서버에 접속한 후, `DISPLAY` 환경 변수를 새로 설정한 디스플레이 번호로 설정합니다:
     ```bash
     export DISPLAY=localhost:1.0
     ```

### R 콘솔을 사용하여 히스토그램 생성

#### 히스토그램을 생성하는 R 스크립트 작성

1. **R 스크립트 작성**:
   - `histogram_x11_persistent.R` 파일에 다음 내용을 작성합니다:
     ```R
     # histogram_x11_persistent.R
     Sys.setenv(DISPLAY="localhost:1.0")  # DISPLAY 환경 변수 설정
     x11()
     hist(rnorm(100))
     # 사용자 입력을 기다리기 위해 readline() 사용
     readline(prompt="Press [Enter] to close the plot window: ")
     dev.off()  # 창을 닫습니다
     ```

#### 인터랙티브 R 세션에서 스크립트 실행

1. **R 콘솔 실행**:
   - Putty를 통해 서버에 접속한 후, R 콘솔을 실행합니다:
     ```bash
     R
     ```

2. **히스토그램 스크립트 실행**:
   - R 콘솔에서 스크립트를 실행합니다:
     ```R
     source("path/to/histogram_x11_persistent.R")
     ```

이렇게 하면 스크립트가 실행되면서 히스토그램 창이 열리고, 사용자가 콘솔에서 엔터 키를 누를 때까지 창이 닫히지 않게 됩니다.

### Python을 사용하여 그래프 생성

#### Matplotlib를 사용하여 그래프 생성

1. **Python 스크립트 작성**:
   - `plot_x11_persistent.py` 파일에 다음 내용을 작성합니다:
     ```python
     import matplotlib.pyplot as plt
     import os

     # DISPLAY 환경 변수 설정
     os.environ['DISPLAY'] = 'localhost:1.0'

     # 그래프 생성
     plt.figure()
     plt.hist([i for i in range(100)])
     plt.title("Histogram")

     # 그래프 창을 닫을 때까지 대기
     plt.show(block=True)
     ```

2. **Python 스크립트 실행**:
   - Putty를 통해 서버에 접속한 후, Python 스크립트를 실행합니다:
     ```bash
     python3 plot_x11_persistent.py
     ```

이렇게 하면 스크립트가 실행되면서 히스토그램 창이 열리고, 사용자가 그래프 창을 닫을 때까지 창이 열려 있게 됩니다.

### 요약

1. VcXsrv 설치 및 설정:
   - XLaunch를 실행하여 "Multiple windows", "Display number: 1" 등의 설정을 완료하고 VcXsrv를 시작합니다.

2. Putty에서 X11 포워딩 활성화:
   - `Enable X11 forwarding` 옵션을 체크하고 서버에 접속합니다.
   - 서버에 접속한 후, `DISPLAY` 환경 변수를 `localhost:1.0`으로 설정합니다.

3. R 콘솔을 사용하여 히스토그램 생성:
   - R 스크립트를 작성하고, 인터랙티브 R 세션에서 스크립트를 실행합니다.

4. Python을 사용하여 그래프 생성:
   - Matplotlib를 사용하여 그래프를 생성하는 Python 스크립트를 작성하고, 스크립트를 실행합니다.


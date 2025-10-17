import time
import random
import sys
import os
from colorama import init, Fore, Back, Style

# Windows에서 색상 지원을 위해 초기화
init()

def print_with_delay(text, delay=0.03, color=Fore.WHITE):
    """텍스트를 타이핑하는 것처럼 출력"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_command(command, color=Fore.GREEN):
    """명령어를 출력"""
    print(f"{Fore.CYAN}user@computer:~$ {color}{command}{Style.RESET_ALL}")
    time.sleep(0.5)

def print_error(text, delay=0.02):
    """오류 메시지를 빨간색으로 출력"""
    for char in text:
        print(f"{Fore.RED}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def print_warning(text, delay=0.02):
    """경고 메시지를 노란색으로 출력"""
    for char in text:
        print(f"{Fore.YELLOW}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def print_success(text, delay=0.02):
    """성공 메시지를 초록색으로 출력"""
    for char in text:
        print(f"{Fore.GREEN}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def simulate_initial_setup():
    """초기 설정"""
    print()
    print()
    
    print_command("npm install")
    print_with_delay("npm WARN deprecated package@1.0.0: This package is deprecated", 0.02)
    print_with_delay("npm WARN deprecated legacy-peer-deps@1.0.0: This package is deprecated", 0.02)
    print_with_delay("added 1234 packages, and audited 1234 packages in 45s", 0.02)
    print_with_delay("found 2 vulnerabilities (1 low, 1 high)", 0.02)
    print_warning("run `npm audit fix` to fix them, or `npm audit` for details", 0.02)
    time.sleep(2)

def simulate_build_with_errors():
    """오류가 포함된 빌드"""
    print_command("npm run build")
    print_with_delay("> project@1.0.0 build", 0.02)
    print_with_delay("> webpack --mode production", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("webpack 5.65.0 compiled with 4 warnings in 2345 ms", 0.02)
    print_warning("WARNING in ./src/components/Button.js", 0.02)
    print_warning("Module not found: Can't resolve './styles.css' in '/app/src/components'", 0.02)
    print_warning("WARNING in ./src/utils/helper.js", 0.02)
    print_warning("Critical dependency: the request of a dependency is an expression", 0.02)
    print_error("ERROR in ./src/main.js", 0.02)
    print_error("Module parse failed: Unexpected token (15:10)", 0.02)
    print_error("You may need an appropriate loader to handle this file type.", 0.02)
    print_error("| import React from 'react';", 0.02)
    print_error("| const App = () => {", 0.02)
    print_error(">   return <div>Hello World</div>;", 0.02)
    print_error("| };", 0.02)
    print_error("| export default App;", 0.02)
    print_error("Build failed!", 0.02)
    time.sleep(3)

def simulate_error_fixing():
    """오류 수정 과정"""
    print()
    time.sleep(1)
    
    print_command("ls src/components/")
    print_with_delay("Button.js", 0.02)
    print_with_delay("Button.css", 0.02)
    print_with_delay("", 0.01)
    
    print_command("mv src/components/Button.css src/components/styles.css")
    print_with_delay("", 0.01)
    time.sleep(1)
    
    print_command("cat src/main.js")
    print_with_delay("import React from 'react';", 0.02)
    print_with_delay("const App = () => {", 0.02)
    print_with_delay("  return <div>Hello World</div>;", 0.02)
    print_with_delay("};", 0.02)
    print_with_delay("export default App;", 0.02)
    time.sleep(1)
    
    print_command("npm install --save-dev @babel/preset-react")
    print_with_delay("added 15 packages, and audited 1249 packages in 3s", 0.02)
    print_with_delay("found 0 vulnerabilities", 0.02)
    time.sleep(1)
    
    print_command("npm run build")
    print_with_delay("> project@1.0.0 build", 0.02)
    print_with_delay("> webpack --mode production", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("webpack 5.65.0 compiled successfully in 2345 ms", 0.02)
    print_with_delay("Build completed successfully!", 0.02)
    time.sleep(2)

def simulate_deployment():
    """배포 과정"""
    print_command("docker build -t myapp .")
    print_with_delay("Sending build context to Docker daemon  2.048kB", 0.02)
    print_with_delay("Step 1/8 : FROM node:16-alpine", 0.02)
    print_with_delay(" ---> abc123def456", 0.02)
    print_with_delay("Step 2/8 : WORKDIR /app", 0.02)
    print_with_delay(" ---> Running in def456ghi789", 0.02)
    print_with_delay(" ---> jkl012mno345", 0.02)
    print_with_delay("Step 3/8 : COPY package*.json ./", 0.02)
    print_with_delay(" ---> pqr678stu901", 0.02)
    print_with_delay("Step 4/8 : RUN npm install", 0.02)
    print_with_delay(" ---> Running in vwx234yza567", 0.02)
    print_with_delay("added 1234 packages, and audited 1234 packages in 2s", 0.02)
    print_with_delay(" ---> bcd890efg123", 0.02)
    print_with_delay("Step 5/8 : COPY . .", 0.02)
    print_with_delay(" ---> hij456klm789", 0.02)
    print_with_delay("Step 6/8 : RUN npm run build", 0.02)
    print_with_delay(" ---> Running in nop012qrs345", 0.02)
    print_with_delay("webpack 5.65.0 compiled successfully", 0.02)
    print_with_delay(" ---> tuv678wxy901", 0.02)
    print_with_delay("Step 7/8 : EXPOSE 3000", 0.02)
    print_with_delay(" ---> zab234cde567", 0.02)
    print_with_delay("Step 8/8 : CMD [\"npm\", \"start\"]", 0.02)
    print_with_delay(" ---> Running in fgh890ijk123", 0.02)
    print_with_delay(" ---> lmn456opq789", 0.02)
    print_with_delay("Successfully built lmn456opq789", 0.02)
    print_with_delay("Successfully tagged myapp:latest", 0.02)
    time.sleep(2)

def simulate_runtime_error():
    """런타임 오류"""
    print_command("docker run -p 3000:3000 myapp")
    print_with_delay("> project@1.0.0 start", 0.02)
    print_with_delay("> node server.js", 0.02)
    print_with_delay("", 0.01)
    print_error("Error: Cannot find module './config/database'", 0.02)
    print_error("    at Function.Module._resolveFilename (node:internal/modules/cjs/loader:933:19)", 0.02)
    print_error("    at Function.Module._load (node:internal/modules/cjs/loader:778:32)", 0.02)
    print_error("    at Module.require (node:internal/modules/cjs/require:63:25)", 0.02)
    print_error("    at require (node:internal/modules/cjs/helpers:108:18)", 0.02)
    print_error("    at Object.<anonymous> (/app/server.js:5:15)", 0.02)
    print_error("    at Module._compile (node:internal/modules/cjs/loader:1103:30)", 0.02)
    print_error("    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1203:10)", 0.02)
    print_error("    at Module.load (node:internal/modules/cjs/loader:1025:25)", 0.02)
    print_error("    at Function.Module._load (node:internal/modules/cjs/loader:778:32)", 0.02)
    print_error("    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:77:25)", 0.02)
    print_error("    at /usr/local/bin/node (node:internal/bootstrap/node:676:18)", 0.02)
    print_error("    at /usr/local/bin/node (node:internal/bootstrap/node:689:3)", 0.02)
    time.sleep(3)

def simulate_debugging():
    """디버깅 과정"""
    print()
    time.sleep(1)
    
    print_command("ls -la")
    print_with_delay("total 32", 0.02)
    print_with_delay("drwxr-xr-x 1 root root 4096 Dec 20 10:30 .", 0.02)
    print_with_delay("drwxr-xr-x 1 root root 4096 Dec 20 10:30 ..", 0.02)
    print_with_delay("-rw-r--r-- 1 root root  1234 Dec 20 10:30 server.js", 0.02)
    print_with_delay("-rw-r--r-- 1 root root   567 Dec 20 10:30 package.json", 0.02)
    print_with_delay("drwxr-xr-x 1 root root 4096 Dec 20 10:30 src", 0.02)
    print_with_delay("drwxr-xr-x 1 root root 4096 Dec 20 10:30 config", 0.02)
    time.sleep(1)
    
    print_command("ls config/")
    print_with_delay("database.js", 0.02)
    print_with_delay("settings.js", 0.02)
    time.sleep(1)
    
    print_command("cat server.js")
    print_with_delay("const express = require('express');", 0.02)
    print_with_delay("const app = express();", 0.02)
    print_with_delay("const port = process.env.PORT || 3000;", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("const db = require('./config/database');", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("app.get('/', (req, res) => {", 0.02)
    print_with_delay("  res.send('Hello World!');", 0.02)
    print_with_delay("});", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("app.listen(port, () => {", 0.02)
    print_with_delay("  console.log(`Server running on port ${port}`);", 0.02)
    print_with_delay("});", 0.02)
    time.sleep(1)
    
    print_command("cat config/database.js")
    print_with_delay("module.exports = {", 0.02)
    print_with_delay("  host: process.env.DB_HOST || 'localhost',", 0.02)
    print_with_delay("  port: process.env.DB_PORT || 5432,", 0.02)
    print_with_delay("  database: process.env.DB_NAME || 'myapp',", 0.02)
    print_with_delay("  username: process.env.DB_USER || 'postgres',", 0.02)
    print_with_delay("  password: process.env.DB_PASS || 'password'", 0.02)
    print_with_delay("};", 0.02)
    time.sleep(1)
    
    print_with_delay("", 0.02)
    time.sleep(1)
    
    print_command("node -e \"console.log(require('./config/database'))\"")
    print_with_delay("{ host: 'localhost', port: 5432, database: 'myapp', username: 'postgres', password: 'password' }", 0.02)
    time.sleep(1)
    
    print_with_delay("", 0.02)
    print_with_delay("", 0.02)
    time.sleep(1)

def simulate_final_success():
    """최종 성공"""
    print_command("docker run -p 3000:3000 myapp")
    print_with_delay("> project@1.0.0 start", 0.02)
    print_with_delay("> node server.js", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("Server running on port 3000", 0.02)
    print_with_delay("", 0.02)
    time.sleep(2)

def simulate_testing():
    """테스트 실행"""
    print_command("npm test")
    print_with_delay("> project@1.0.0 test", 0.02)
    print_with_delay("> jest", 0.02)
    print_with_delay("", 0.01)
    print_with_delay(" FAIL  src/__tests__/api.test.js", 0.02)
    print_error("  ● API endpoint test", 0.02)
    print_error("", 0.01)
    print_error("    expect(received).toBe(expected)", 0.02)
    print_error("", 0.01)
    print_error("    Expected: 200", 0.02)
    print_error("    Received: 404", 0.02)
    print_error("", 0.01)
    print_error("      4 | describe('API endpoint test', () => {", 0.02)
    print_error("      5 |   it('should return 200 for valid request', () => {", 0.02)
    print_error("    > 6 |     expect(response.status).toBe(200);", 0.02)
    print_error("         |                              ^", 0.02)
    print_error("      7 |   });", 0.02)
    print_error("      8 | });", 0.02)
    print_error("", 0.01)
    print_with_delay(" PASS  src/__tests__/utils.test.js", 0.02)
    print_with_delay(" PASS  src/__tests__/main.test.js", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("Test Suites: 2 passed, 1 failed, 3 total", 0.02)
    print_with_delay("Tests:       14 passed, 1 failed, 15 total", 0.02)
    print_with_delay("Snapshots:   0 total", 0.02)
    print_with_delay("Time:        2.345 s", 0.02)
    time.sleep(2)

def simulate_test_fix():
    """테스트 수정"""
    print()
    time.sleep(1)
    
    print_command("cat src/__tests__/api.test.js")
    print_with_delay("const request = require('supertest');", 0.02)
    print_with_delay("const app = require('../server');", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("describe('API endpoint test', () => {", 0.02)
    print_with_delay("  it('should return 200 for valid request', () => {", 0.02)
    print_with_delay("    const response = request(app).get('/api/users');", 0.02)
    print_with_delay("    expect(response.status).toBe(200);", 0.02)
    print_with_delay("  });", 0.02)
    print_with_delay("});", 0.02)
    time.sleep(1)
    
    print_command("cat src/server.js")
    print_with_delay("const express = require('express');", 0.02)
    print_with_delay("const app = express();", 0.02)
    print_with_delay("const port = process.env.PORT || 3000;", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("app.get('/', (req, res) => {", 0.02)
    print_with_delay("  res.send('Hello World!');", 0.02)
    print_with_delay("});", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("app.listen(port, () => {", 0.02)
    print_with_delay("  console.log(`Server running on port ${port}`);", 0.02)
    print_with_delay("});", 0.02)
    time.sleep(1)
    
    print_with_delay("🔍 문제 발견: `/api/users` 엔드포인트가 없습니다!", 0.02)
    time.sleep(1)
    
    print_command("echo 'app.get(\"/api/users\", (req, res) => { res.json([{id: 1, name: \"John\"}]); });' >> src/server.js")
    print_with_delay("", 0.01)
    time.sleep(1)
    
    print_command("npm test")
    print_with_delay("> project@1.0.0 test", 0.02)
    print_with_delay("> jest", 0.02)
    print_with_delay("", 0.01)
    print_with_delay(" PASS  src/__tests__/utils.test.js", 0.02)
    print_with_delay(" PASS  src/__tests__/main.test.js", 0.02)
    print_with_delay(" PASS  src/__tests__/api.test.js", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("Test Suites: 3 passed, 3 total", 0.02)
    print_with_delay("Tests:       15 passed, 15 total", 0.02)
    print_with_delay("Snapshots:   0 total", 0.02)
    print_with_delay("Time:        2.345 s", 0.02)
    print_with_delay("Ran all test suites.", 0.02)
    print_with_delay("", 0.02)
    time.sleep(2)

def main():
    """메인 함수"""
    print(f"{Fore.CYAN}=== 터미널 ==={Style.RESET_ALL}")
    print()
    
    # 초기 설정
    simulate_initial_setup()
    print()
    
    simulate_build_with_errors()
    print()
    
    simulate_error_fixing()
    print()
    
    simulate_deployment()
    print()
    
    simulate_runtime_error()
    print()
    
    simulate_debugging()
    print()
    
    simulate_testing()
    print()
    
    simulate_test_fix()
    print()
    
    simulate_final_success()
    print()

if __name__ == "__main__":
    main() 
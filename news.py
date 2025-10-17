#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import random
import string
import sys
import time
from datetime import datetime, timedelta
from itertools import cycle


def enable_windows_ansi_colors_if_possible() -> None:
    """
    Try enabling ANSI escape processing on Windows 10+ consoles so that
    color codes render correctly without extra dependencies.
    """
    if os.name != "nt":
        return
    try:
        import msvcrt  # noqa: F401
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            new_mode = ctypes.c_uint32(mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
            kernel32.SetConsoleMode(handle, new_mode)
    except Exception:
        # Best-effort only; fall back to no color if needed
        pass


class Ansi:
    RESET = "\033[0m"
    DIM = "\033[2m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"


def ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def format_level(level: str) -> str:
    mapping = {
        "INFO": Ansi.CYAN,
        "WARN": Ansi.YELLOW,
        "ERROR": Ansi.RED,
        "OK": Ansi.GREEN,
        "DEBUG": Ansi.GRAY,
    }
    color = mapping.get(level, "")
    return f"{Ansi.BOLD}{color}{level}{Ansi.RESET}"


def print_log(level: str, message: str) -> None:
    print(f"[{ts()}] [{format_level(level)}] {message}")


TOPICS = [
    "경제", "증시", "빅테크", "인공지능", "반도체", "환율", "암호화폐", "정치", "국제", "스타트업",
    "원자재", "원유", "부동산", "고용", "소비", "테슬라", "삼성전자", "애플", "엔비디아", "바이오",
]

NEWS_SOURCES = [
    "연합", "로이터", "블룸버그", "WSJ", "CNBC", "가디언", "뉴욕타임즈", "한경", "매경", "조선비즈",
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120",
]

PROXIES = [
    "192.168.0.12:8080", "10.0.0.3:3128", "203.0.113.52:8000", "198.51.100.24:1080",
]


def random_query() -> str:
    topic = random.choice(TOPICS)
    tail = random.choice([
        "속보", "브리핑", "전망", "실시간", "분석", "이슈", "모멘텀", "컨센서스", "어닝", "리포트",
    ])
    return f"{topic} {tail} site:news"


def random_title(topic: str) -> str:
    verb = random.choice(["급등", "하락", "반등", "확대", "둔화", "호조", "부진", "상승", "회복", "변동"])
    suffix = random.choice(["전망", "원인 분석", "시장 반응", "핵심 포인트", "단독"])
    return f"{topic} {verb} {suffix}"


def make_progress_bar(ratio: float, width: int = 28) -> str:
    filled = int(ratio * width)
    return f"[{Ansi.GREEN}{'█' * filled}{Ansi.RESET}{'·' * (width - filled)}] {int(ratio * 100):3d}%"


def simulate_spinner(text: str, duration_s: float = 1.6, fps: int = 16) -> None:
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    spinner = cycle(frames)
    steps = max(1, int(duration_s * fps))
    for i in range(steps):
        frame = next(spinner)
        sys.stdout.write(f"\r{Ansi.GRAY}{frame}{Ansi.RESET} {text}")
        sys.stdout.flush()
        time.sleep(1.0 / fps)
    sys.stdout.write("\r" + " " * (len(text) + 4) + "\r")
    sys.stdout.flush()


def jitter(min_s: float, max_s: float) -> float:
    return random.uniform(min_s, max_s)


def random_status_code() -> int:
    # Weighted distribution toward 200 with occasional errors
    return random.choices([200, 200, 200, 200, 200, 304, 429, 500, 502, 503],
                          weights=[65, 15, 8, 3, 2, 3, 2, 1, 1, 0.5], k=1)[0]


def random_id(n: int = 6) -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=n))


def format_since(past: datetime) -> str:
    delta = datetime.now() - past
    if delta < timedelta(minutes=1):
        return f"{int(delta.total_seconds())}초 전"
    if delta < timedelta(hours=1):
        return f"{int(delta.total_seconds() // 60)}분 전"
    if delta < timedelta(days=1):
        return f"{int(delta.total_seconds() // 3600)}시간 전"
    return f"{delta.days}일 전"


def run_fake_search(args: argparse.Namespace) -> None:
    enable_windows_ansi_colors_if_possible()

    print()
    print(f"{Ansi.BOLD}가짜 Google 뉴스 수집기 (데모){Ansi.RESET}")
    print(f"{Ansi.DIM}Ctrl+C 로 종료. 실제로 크롤링하지 않으며 콘솔 데모만 표시합니다.{Ansi.RESET}")
    print()

    query_count = 0
    last_ok = datetime.now()

    try:
        while True:
            query = random_query()
            ua = random.choice(USER_AGENTS)
            proxy = random.choice(PROXIES)
            req_id = random_id()

            print_log("DEBUG", f"요청 준비 id={req_id} UA=... Proxy={proxy}")
            simulate_spinner(f"Google에 질의 중: '{query}'", duration_s=jitter(0.8, 2.0) * args.speed)

            status = random_status_code()
            latency_ms = int(jitter(120, 1200) * args.speed * 1000)

            if status == 200:
                last_ok = datetime.now()
                print_log("OK", f"HTTP 200 ({latency_ms}ms) 질의 성공: '{query}'")
                found = random.randint(3, 12)
                print_log("INFO", f"추출된 기사 {found}건 (정규화/중복제거 적용)")

                for i in range(found):
                    topic = random.choice(TOPICS)
                    title = random_title(topic)
                    src = random.choice(NEWS_SOURCES)
                    published = datetime.now() - timedelta(minutes=random.randint(1, 180))
                    print(f"  {Ansi.BLUE}•{Ansi.RESET} {title} {Ansi.DIM}- {src}, {format_since(published)}{Ansi.RESET}")
                    time.sleep(jitter(0.02, 0.08) * args.speed)

                # Fake parse/progress
                print_log("DEBUG", "엔티티 추출/토픽 모델링 중…")
                for step in range(1, 11):
                    bar = make_progress_bar(step / 10.0)
                    sys.stdout.write("\r  " + bar)
                    sys.stdout.flush()
                    time.sleep(jitter(0.03, 0.09) * args.speed)
                sys.stdout.write("\r" + " " * 60 + "\r")
                sys.stdout.flush()

                # Cache write
                print_log("INFO", f"캐시 저장 완료 bucket=news/key={req_id}")

            elif status == 304:
                print_log("WARN", f"HTTP 304 Not Modified ({latency_ms}ms) 변경 없음: '{query}'")

            elif status == 429:
                backoff_s = round(jitter(1.2, 4.5) * args.speed, 1)
                print_log("WARN", f"HTTP 429 Too Many Requests ({latency_ms}ms) 백오프 {backoff_s}s")
                simulate_spinner("레이트 리밋 회피: 프록시/UA 순환", duration_s=min(backoff_s, 3.0))
                print_log("DEBUG", f"프록시 교체 → {random.choice(PROXIES)} | UA 교체")
                time.sleep(max(0.2, backoff_s - 0.6))

            else:
                print_log("ERROR", f"HTTP {status} ({latency_ms}ms) 서버 또는 네트워크 오류")
                retry_s = round(jitter(0.8, 2.0) * args.speed, 1)
                print_log("INFO", f"재시도 대기 {retry_s}s (지수 백오프 시뮬레이션)")
                time.sleep(retry_s)

            query_count += 1
            since_ok = int((datetime.now() - last_ok).total_seconds())
            qps = round(random.uniform(0.4, 1.6) / args.speed, 2)
            print_log("DEBUG", f"누적 질의 {query_count}건 | 최근 성공 {since_ok}s 전 | QPS≈{qps}")

            # Idle jitter between loops
            time.sleep(jitter(args.delay_min, args.delay_max) * args.speed)

    except KeyboardInterrupt:
        print()
        print_log("INFO", "종료 요청 수신. 리소스 해제 및 마무리 중…")
        time.sleep(0.3)
        print_log("OK", "정상 종료되었습니다. 좋은 하루 되세요!")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="구글 뉴스 크롤링처럼 보이는 콘솔 데모 (실제 크롤링 안 함)",
    )
    parser.add_argument(
        "--delay-min",
        type=float,
        default=0.15,
        help="루프 최소 휴지 시간(초)",
    )
    parser.add_argument(
        "--delay-max",
        type=float,
        default=0.6,
        help="루프 최대 휴지 시간(초)",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=1.0,
        help="전체 동작 속도 배율 (낮출수록 빠르게 보임)",
    )

    args = parser.parse_args(argv)
    # Sanitize
    if args.delay_min < 0:
        args.delay_min = 0.0
    if args.delay_max < args.delay_min:
        args.delay_max = max(args.delay_min, 0.01)
    if args.speed <= 0:
        args.speed = 0.8
    return args


def main() -> None:
    args = parse_args(sys.argv[1:])
    run_fake_search(args)


if __name__ == "__main__":
    main()


